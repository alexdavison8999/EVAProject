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