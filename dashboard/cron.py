import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_members(conn):
    """
    Query all rows in the dashboard_gymcheckin table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM dashboard_gymcheckin")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def check_out_all_members(conn):
    cur = conn.cursor()
    cur.execute("UPDATE dashboard_gymcheckin "
                    "SET status = 0 "
                    "WHERE id IN (SELECT id FROM dashboard_gymcheckin WHERE status = 1);")


def daily_checkout_scheduled_job():
    database = "/Users/kentsay/Dropbox/playground/django/gymadmin/db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Query all tasks")
        select_all_members(conn)
        print("Check out all members")
        check_out_all_members(conn)
