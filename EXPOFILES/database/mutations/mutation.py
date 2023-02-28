import psycopg2
import psycopg2.extensions
import psycopg2.errors
from database.queries.query import getMedByName
from datetime import datetime

from database.dbUtils import executeQuery


def createConfirm(conn: psycopg2.extensions.connection, medName: str, taken: bool=False):

    med = getMedByName(conn, medName)
    
    string = f"INSERT INTO public.confirmations (medname,taken,medicationid,created_at) \
	                VALUES ('{medName}',{taken},'{med.id}',NOW());"
    data = executeQuery(conn, string)

    print(f'RESULTING DATA: {data}')

    return

def createMedicene(conn: psycopg2.extensions.connection, medName: str, dateFilled: datetime, refills: int, refillDate: datetime, timesPerDay: int, timesPerWeek: int, folderPath: str):
    dateFilledStr: str = dateFilled.strftime("%\d/%m/%Y")
    refillDateStr: str = refillDate.strftime("%\d/%m/%Y")


    sql = f"INSERT INTO public.medications (medname, datefilled, refillsleft, refilldate, timesperday, timesperweek, folderpath, created_at) \
                    VALUES ('{medName}', TO_DATE('{dateFilledStr}', YYYYMMDD), {refills}, TO_DATE('{refillDateStr}', YYYYMMDD), {timesPerDay}, {timesPerWeek}, '{folderPath}', NOW());"

    data = executeQuery(conn, sql)

    print(f'RESULTING DATA: {data}')

    return

def alterMedicene(conn: psycopg2.extensions.connection, id: int, medName: str, dateFilled: datetime, refills: int, refillDate: datetime, timesPerDay: int, timesPerWeek: int, folderPath: str):
    dateFilledStr: str = dateFilled.strftime("%\d/%m/%Y")
    refillDateStr: str = refillDate.strftime("%\d/%m/%Y")


    sql = f"UPDATE medications \
            SET medname = '{medName}', \
            datefilled = TO_DATE('{dateFilledStr}', YYYYMMDD), \
            refillsleft = {refills}, \
            refilldate = TO_DATE('{refillDateStr}', YYYYMMDD), \
            timesperday = {timesPerDay}, \
            timesperweek = {timesPerWeek}, \
            folderpath = '{folderPath}' \
            WHERE id = {id}"

    data = executeQuery(conn, sql)

    print(f'RESULTING DATA: {data}')

    return
