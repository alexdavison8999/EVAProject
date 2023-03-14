import psycopg2
import psycopg2.extensions
import psycopg2.errors
from database.classes.medications import Medication
from database.queries.query import getMedByName
from datetime import datetime

from database.dbUtils import executeQuery


def createConfirm(
    conn: psycopg2.extensions.connection, medName: str, taken: bool = False
):
    med = getMedByName(conn, medName)

    string = f"INSERT INTO public.confirmations (medname,taken,medicationid,created_at) \
	                VALUES ('{medName}',{taken},'{med.id}',NOW());"
    data = executeQuery(conn, string)

    print(f"RESULTING DATA: {data}")

    return


def createMedicine(
    conn: psycopg2.extensions.connection,
    medName: str,
    dateFilled: datetime,
    refills: int,
    refillDate: datetime,
    timesPerDay: int,
    timesPerWeek: int,
    folderPath: str,
):
    dateFilledStr: str = dateFilled.strftime("%\d/%m/%Y")
    refillDateStr: str = refillDate.strftime("%\d/%m/%Y")

    sql = f"INSERT INTO public.medications \
            (medname, datefilled, refillsleft, refilldate, \
            timesperday, timesperweek, folderpath, created_at) \
            VALUES ('{medName}', TO_DATE('{dateFilledStr}', YYYYMMDD),\
            {refills}, TO_DATE('{refillDateStr}', YYYYMMDD), {timesPerDay}, {timesPerWeek}, '{folderPath}', NOW());"

    data = executeQuery(conn, sql)

    print(f"RESULTING DATA: {data}")

    return


def alterMedicine(
    conn: psycopg2.extensions.connection,
    med: Medication,
    fieldToEdit: str,
    newVal: str,
) -> dict:
    attr_list = [a for a in dir(med) if not a.startswith("__")]
    for attr in attr_list:
        if fieldToEdit == attr:
            if fieldToEdit in ["refillDate", "dateFilled"]:
                continue
            else:
                setattr(med, attr, newVal)

    dateFilledStr: str = med.dateFilled.strftime("%Y-%m-%d")
    refillDateStr: str = med.refillDate.strftime("%Y-%m-%d")

    sql = f"UPDATE medications \
            SET medname = '{med.medName}', \
            datefilled = '{newVal if fieldToEdit == 'dateFilled' else dateFilledStr}', \
            refillsleft = '{med.refillsLeft}', \
            refilldate = '{newVal if fieldToEdit == 'refillDate' else refillDateStr}', \
            timesperday = '{med.timesPerDay}', \
            timesperweek = '{len(med.timesPerWeek)}' \
            WHERE id = '{med.id}'"

    data = executeQuery(conn, sql)

    if data == "0" or data is None:
        return {"errors": "Unable to update medication"}

    return {fieldToEdit: newVal}
