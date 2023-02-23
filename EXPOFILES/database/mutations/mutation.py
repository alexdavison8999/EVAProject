import psycopg2
import psycopg2.extensions
import psycopg2.errors
from database.queries.query import getMedByName

from database.dbUtils import executeQuery


def createConfirm(conn: psycopg2.extensions.connection, medName: str, taken: bool=False):

    med = getMedByName(conn, medName)
    
    string = f"INSERT INTO public.confirmations (medname,taken,medicationid,created_at) \
	                VALUES ('{medName}',{taken},'{med.id}',NOW());"
    data = executeQuery(conn, string)

    print(f'RESULTING DATA: {data}')

    return
