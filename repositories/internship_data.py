import psycopg
from psycopg.rows import dict_row
from db import DB

def all_data(): # fancy comment that this is returned
    with psycopg.connect( # under this block then we connect SQL to python 
        conninfo = DB,
        row_factory = dict_row,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                '''
                SELECT 
                    *
                FROM 
                    internships
                ORDER BY 
                    deadline
                ;
                '''
                )
            return cur.fetchall() # putting this in a array of dict instead of an array of tuples

def internship(id:int):
    with psycopg.connect(
        conninfo = DB,
        row_factory = dict_row,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                '''
                SELECT 
                    * 
                FROM 
                    internships
                WHERE
                    id = %s;
                ''', [id]
                )
            return cur.fetchone()