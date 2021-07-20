from typing import Counter
import psycopg2
from psycopg2 import Error
from config import config


def connect():
    # Connect to postgreSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to postgreSQL server
        print('Connecting to database server...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # excute a statement
        print('PostgreSQL database version: ')
        cur.execute('SELECT version();')

        # display database version
        db_version = cur.fetchone()
        print("You are connect to",db_version,"\n")

        """
        query syntax
        """
        cur.execute('SELECT * From "Sales";')
        record = cur.fetchall()
        print(record)

        # close communication with database server
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        print('Database connection closed')

if __name__ == '__main__':
    connect()
