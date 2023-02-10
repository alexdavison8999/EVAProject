import psycopg2

def connect(
        host: str='localhost',
        database: str='evadb',
        user: str='evadb',
        password: str='evadb100'
    ):
    """
    Creates a dataase connection to the `evadb` database.
    Inputs:
        host:       host to connect to
        database:   name of the database
        user:       name of the user
        password:   users password

    """
    return psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

def medicationsQuery():
    """
    Queries the `medications` table for all medications.
    """
    pass

def confirmationsQuery():
    """
    Queries the `medications` table for all medications.
    """
    pass

def getMedByIdAndName():
    """
    Queries the `medications` table for all medications.
    """
    pass

def getConfirmationsByMedName():
    """
    Queries the `medications` table for all medications.
    """
    pass

def getPercentConfirmsPastWeek(conn, medName: str) -> float:
    """
    Returns the percentage of confirmations in the past week that
    are marked as taken for medication `medName`
    Inputs:
        conn:       Postgres connection object
        medName:    Name of medication to check
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
    # Initialize cursor object
    cursor = conn.cursor()
    cursor.execute(sql_string)

    # Data is returned as a tuple
    data = cursor.fetchone()

    # Commit transaction (I think we need to do this after every statement)
    conn.commit()

    percent_val = data[0]

    return percent_val
