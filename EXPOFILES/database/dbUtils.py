import psycopg2

def connect():
    return psycopg2.connect(
    host='localhost',
    database='evadb',
    user='evadb',
    password='evadb100'
)