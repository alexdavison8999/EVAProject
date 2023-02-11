import psycopg2
import psycopg2.extensions

def medicationsQuery(conn: psycopg2.extensions.connection):
    """
    Queries the `medications` table for all medications.

    Inputs:
        `conn`:       Postgres connection object
    """
    pass

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

def getPercentConfirmsPerTimePeriod(conn: psycopg2.extensions.connection, medName: str) -> float:
    """
    Returns the percentage of confirmations in the past week that
    are marked as taken for medication `medName`

    Inputs:
        `conn`:       Postgres connection object
        `medName`:    Name of medication to check
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
                                    created_at >= (NOW() - INTERVAL '7 days'))\
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
                            created_at >= (NOW() - INTERVAL '7 days');"

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

    print(f'{percent_val:g}')
    print(f'{percent_val:.4g}')

    return percent_val