import psycopg2
import psycopg2.extensions

from constants.database import *

def connectToEvaDB(
        host: str=PG_HOST,
        database: str=PG_DB,
        user: str=PG_USER,
        password: str=PG_PASSWORD
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

            booln = 'SELECT' in sql_string 
            print(f'QUERY? {booln}, ONEORALL: {oneOrAll}')

            # Commit transaction (I think we need to do this after every statement)
            if 'SELECT' in sql_string:
                records = []
                if oneOrAll == 'one':
                    data = cursor.fetchone()
                else:
                    data = cursor.fetchall()
                    for row in data:
                        records.append(row)
                    data = records
                cursor.close()
                return data
            else:
                conn.commit()
                affected = f"{cursor.rowcount} rows affected."
                cursor.close()
                return affected

        except psycopg2.DatabaseError as e:
            print(f"ERROR IN EXECUTION, ROLLING BACK: {e}")
            conn.rollback()

    else:
        print(f"Invalid argument for oneOrAll, got {oneOrAll} but expected to be in ['one','all']")

    return data