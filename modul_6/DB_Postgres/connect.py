import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        """ create a database connection to a SQLite database """
        conn = psycopg2.connect(host='localhost', database="test", user="postgres", password="0000")
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f'failed connection {err}')


