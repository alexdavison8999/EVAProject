import os
import sys
import psycopg2
import psycopg2.extensions

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

def executeQuery(conn: psycopg2.extensions.connection, sql_string: str):
    """
    Executes the sql query pased in the `sql_string` argument

    Inputs:
        `conn`:         Postgres connection object
        `sql_string`:   SQL string statement
    """
    # Initialize cursor object
    cursor = conn.cursor()
    cursor.execute(sql_string)

    # Data is returned as a tuple
    data = cursor.fetchall()

    # Commit transaction (I think we need to do this after every statement)
    conn.commit()

    return data

def medicationsQuery(conn: psycopg2.extensions.connection) -> list[Medication]:
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
                        created_at >= (NOW() - INTERVAL '7 days');"

    data = executeQuery(conn, sql_string)

    medications_list = tuplesToMedicationList(data)

    return medications_list

def timesList(conn: psycopg2.extensions.connection) -> list[str]:
    """
    Queries the `medications` table for active (?) medications and, 
    based on their `timesPerDay` and `timesPerWeek` fields, create a list
    of HH:MM times that the EVA must perform a confirmation check

    Inputs:
        `conn`:       Postgres connection object

    Outputs:
        `times_list`: A list of times in which to open the confirmation UI 
    """
    times_list = []

    sql_string = "SELECT \
                    * \
                    FROM \
                        medications \
                    WHERE \
                        created_at >= (NOW() - INTERVAL '7 days');"

    data = executeQuery(conn, sql_string)

    meds: list[Medication] = tuplesToMedicationList(data)

    # TODO: Write logic for creating alert times. Should this be
    # something where the user inputs when they want to be notified
    # for each medication, or should they set a morning, middle, and evening
    # time that we can use for all medications if it is the correct time/day
    # to take the medication

    return ['12:54', '12:59', '13:00', '18:30', '19:00']

    return times_list

def confirmationsQuery(conn: psycopg2.extensions.connection):
    """
    Queries the `confirmations` table for all medications.

    Inputs:
        `conn`:       Postgres connection object
    """
    pass

def getMedByNameAndId(conn: psycopg2.extensions.connection, medName: str, medicationId: str):
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
                                    medicationid = 1 \
                                AND \
                                    created_at >= (NOW() - INTERVAL '{interval}'))\
                        ) AS percentage \
                    FROM \
                        confirmations \
                    WHERE \
                        medname = '{medName}' \
                        AND \
                            medicationid = 1 \
                        AND \
                            taken = true \
                        AND \
                            created_at >= (NOW() - INTERVAL '{interval}');"

    # TODO: Move code below to its own function so we can set up the queries 
    # here and execute them elsewhere. Something like the function returns 
    # our value, we store it in percent_val, and then return percent_val

    # Initialize cursor object
    cursor = conn.cursor()
    cursor.execute(sql_string)

    # Data is returned as a tuple
    data = cursor.fetchone()

    # Commit transaction (I think we need to do this after every statement)
    conn.commit()

    percent_val = data[0]

    print(f'% from past {interval}: {percent_val:.4g}%')

    return percent_val