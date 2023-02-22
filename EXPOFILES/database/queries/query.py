from datetime import datetime
from typing import Union
import psycopg2
import psycopg2.extensions
import psycopg2.errors
from constants.confirmations import *

from database.classes.medications import Medication

# TODO: Move to another file 
def tuplesToMedicationList(data: list[tuple]) -> list[Medication]:
    """
    Converts tuple list to a list of `Medications`.

    Inputs:
        `data`:       The list of tuples from a query
    """
    return_list = []

    if len(data) > 0:
        for tuple in data:
            return_list.append(Medication(tuple))

    return return_list

def executeQuery(conn: psycopg2.extensions.connection, sql_string: str, oneOrAll: str = 'all'):
    """
    Executes the sql query pased in the `sql_string` argument

    Inputs:
        `conn`:         Postgres connection object
        `sql_string`:   SQL string statement
        `oneOrAll`:     Determines whether to fetchone (`one`) or fetchall (`all`), default `all`
    """
    data = None
    if oneOrAll in ['one','all']:

        cursor = conn.cursor()
        try:
            cursor.execute(sql_string)

            # Commit transaction (I think we need to do this after every statement)
            conn.commit()

            if oneOrAll == 'one':
                data = cursor.fetchone()
            else:
                data = cursor.fetchall()
        except:
            print("ERROR IN EXECUTION, ROLLING BACK")
            conn.rollback()

    else:
        print(f"Invalid argument for oneOrAll, got {oneOrAll} but expected to be in ['one','all']")

    return data

def medicationsQuery(conn: psycopg2.extensions.connection) -> Union[list[Medication], None]:
    """
    Queries the `medications` table for all medications.

    Inputs:
        `conn`:       Postgres connection object
    """
    medications_list = []

    sql_string = "SELECT \
                    * \
                    FROM \
                        medications \
                    WHERE \
                        created_at >= (NOW() - INTERVAL '100 days');"

    data = executeQuery(conn, sql_string)

    medications_list = tuplesToMedicationList(data)

    return medications_list

def timesList(conn: psycopg2.extensions.connection) -> dict[list[str]]:
    """
    Queries the `medications` table for active (?) medications and, 
    based on their `timesPerDay` and `timesPerWeek` fields, create a list
    of HH:MM times that the EVA must perform a confirmation check

    Inputs:
        `conn`:       Postgres connection object

    Outputs:
        `times_list`: A list of times in which to open the confirmation UI 
    """
    date = datetime.now()

    sql_string = "SELECT \
                    * \
                    FROM \
                        medications \
                    WHERE \
                        created_at >= (NOW() - INTERVAL '100 days');"

    data = executeQuery(conn, sql_string)

    meds: list[Medication] = tuplesToMedicationList(data)
    
    meds_to_add: list[Medication] = []

    day_of_week = date.strftime("%A")

    for med in meds:
        for day in med.timesPerWeek:
            if day_of_week == day:
                meds_to_add.append(med)

    morning_conf = f'{MORNING_CONFIRM_H}:{MORNING_CONFIRM_M}'
    midday_conf = f'{MIDDAY_CONFIRM_H}:{MIDDAY_CONFIRM_M}'
    afternoon_conf = f'{AFTERNOON_CONFIRM_H}:{AFTERNOON_CONFIRM_M}'

    confirm_tuples = {
        morning_conf: [],
        midday_conf: [],
        afternoon_conf: []
    }
    
    if len(meds_to_add) > 0:
        for med in meds_to_add:
            if med.timesPerDay == 3:
                confirm_tuples[morning_conf].append(med.medName)
                confirm_tuples[midday_conf].append(med.medName)
                confirm_tuples[afternoon_conf].append(med.medName)
            elif med.timesPerDay == 2:
                confirm_tuples[morning_conf].append(med.medName)
                confirm_tuples[afternoon_conf].append(med.medName)
            elif med.timesPerDay == 1:
                confirm_tuples[afternoon_conf].append(med.medName)
            else:
                print(f"Invalid number of times to check medication {med.medName}")

    return confirm_tuples

def confirmationsQuery(conn: psycopg2.extensions.connection):
    """
    Queries the `confirmations` table for all medications.

    Inputs:
        `conn`:       Postgres connection object
    """
    pass

def getMedByName(conn: psycopg2.extensions.connection, medName: str):
    """
    Queries the `medications` a medication given an medicationId and a medName.

    Inputs:
        `conn`:       Postgres connection object
        `medName`:    Name of medication to check
    """
    pass

def getConfirmationsByMedName(conn: psycopg2.extensions.connection, medName: str, timeLimit: int = 0):
    """
    Queries the `confirmations` table for confirmations by a med name.

    Inputs:
        `conn`:       Postgres connection object
        `medName`:    Name of medication to check
    """
    pass

def getPercentConfirmsPerTimePeriod(conn: psycopg2.extensions.connection, medName: str, interval: str = '7 days') -> float:
    """
    Returns the percentage of confirmations in the past week that
    are marked as taken for medication `medName`

    Inputs:
        `conn`:         Postgres connection object
        `medName`:      Name of medication to check
        `interval`:     Optional parameter to set the time interval for the query, default is 7 days

    Outputs:
        `percent_val`:  Percentage over the `interval` that the user confirmed the medication as `taken`
    """
    percent_val = 0
    sql_string = f"SELECT\
                    ( \
                        100.0 * COUNT(*) / \
                        ( SELECT COUNT(*) \
                            FROM \
                                confirmations \
                            WHERE \
                                medname = '{medName}'\
                                AND \
                                    created_at >= (NOW() - INTERVAL '{interval}'))\
                        ) AS percentage \
                    FROM \
                        confirmations \
                    WHERE \
                        medname = '{medName}' \
                        AND \
                            taken = true \
                        AND \
                            created_at >= (NOW() - INTERVAL '{interval}');"

    # TODO: Move code below to its own function so we can set up the queries 
    # here and execute them elsewhere. Something like the function returns 
    # our value, we store it in percent_val, and then return percent_val

    try: 
        data = executeQuery(conn, sql_string, 'one')
        percent_val = data[0]
    except:
        percent_val = -1

    print(f'% from past {interval}: {percent_val:.4g}%')

    return percent_val