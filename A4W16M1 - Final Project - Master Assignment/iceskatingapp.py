import os
import re
import sys
import json
import sqlite3

from skater import Skater
from track import Track
from event import Event


def main():
    # Prepare the script (such as resetting the database)
    prepare()

    # Create a database object
    db = Database()

    # Our test skater
    s = Skater(
        id=-1,
        first_name='Bob',
        last_name='Bobson',
        nationality='NL',
        gender='Male',
        date_of_birth='01-01-2000',
        database=db
    )

    # Prepare an insert query which we can execute later.
    db.db_insert_prep("skaters", "first_name, last_name, nationality, gender, date_of_birth")

    # Execute the prepared query with own values, so we can insert values into our database
    db.execute_query([s.first_name, s.last_name, s.nationality, s.gender, s.date_of_birth])
    db.execute_query([s.first_name, s.last_name, s.nationality, s.gender, s.date_of_birth])

    # Fetch row from table based on specific id
    db.db_fetch("skaters", "id", "1")

    # Fetch all rows of a specific table
    db.db_fetch("skaters")

    # t = Track(
    #     id=1,
    #     name='Sample Track',
    #     city='Sample City',
    #     country='Sample Country',
    #     outdoor=True,
    #     altitude=1000
    # )

    e = Event(
        id=1,
        name='Sample Event',
        track_id=1,
        date='01-01-2023',
        distance=5000,
        duration=300000,
        laps=25,
        winner='Bob',
        category='Human'
    )

    db.db_insert_prep("event_skaters", "event_id, skater_id")
    db.execute_query([e.id, s.id])
    db.db_fetch("event_skaters")


def prepare():
    conn = sqlite3.connect(os.path.join(sys.path[0], 'iceskatingapp.db'))

    conn.execute('''DELETE FROM skaters''')
    conn.execute('''DELETE FROM event_skaters''')
    conn.execute('''UPDATE sqlite_sequence SET seq = 0 WHERE name = "skaters"''')
    conn.execute('''UPDATE sqlite_sequence SET seq = 0 WHERE name = "event_skaters"''')
    conn.commit()
    conn.close()


class Database:
    def __init__(self):
        self.db_file = os.path.join(sys.path[0], 'iceskatingapp.db')
        self.conn = self.db_connect()
        self.query = ""
        self.lastrowid = -1

    def db_connect(self):
        if not os.path.exists(self.db_file):
            print(f"Error - Database file {self.db_file} does not exist")
            return

        conn = sqlite3.connect(self.db_file)

        if conn is None:
            print(f"Error - Failed to connect to {os.path.basename(self.db_file)}")
        else:
            print(f"Successfully connected to: {os.path.basename(self.db_file)}")

        return conn

    def db_insert_prep(self, table, columns):
        num_ques = len(columns.split(", "))
        value_promise = ("?," * (num_ques - 1)) + "?"
        self.query = f"INSERT INTO {table} ({columns}) VALUES ({value_promise})"

        print(self.query)

    def db_fetch(self, table, where=None, id=None, silent=False):
        c = self.conn.cursor()

        self.query = f"SELECT * FROM {table}"

        if where and id is not None:
            self.query += f" WHERE {where}=?"

        if id is not None:
            values = (id,)
        else:
            values = ()

        c.execute(self.query, values)

        self.lastrowid = c.lastrowid

        if not silent:
            print(self.query)

            # Fetch column names and print them joined by ' | '
            names = [description[0] for description in c.description]
            header = ' | '.join(f"{name:<20}" for name in names)
            print("\n")

            # Print the column names
            print(header)

            # Print a dashed line of the same width as the header
            print('-' * len(header))

            # Fetch and print all rows
            rows = c.fetchall()
            if len(rows) == 0:
                print("No rows")
            else:
                for row in rows:
                    print(' | '.join(
                        f"{str(r) if r is not None else str(type(r)):<20}" for r in row))  # Format items and concatenate
                print("\n")
        c.close()

    def execute_query(self, values: list):
        c = self.conn.cursor()
        c.execute(self.query, values)
        self.lastrowid = c.lastrowid
        c.connection.commit()
        c.close()


if __name__ == "__main__":
    main()
