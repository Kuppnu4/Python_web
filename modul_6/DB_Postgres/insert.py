import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection

fake = Faker('uk-UA')
COUNT = 5_000


def insert_data (conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param sql_expression: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    try:
        for _ in range(COUNT):
            c.execute(sql_expression, (fake.name(), fake.email(), fake.password(), randint(19, 74)))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_insert_users_data = """
    INSERT INTO users (name, email, password, age) VALUES (%s, %s, %s, %s);
    """
    try:
        with create_connection() as conn:
            if conn is not None:
                insert_data(conn, sql_insert_users_data)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)