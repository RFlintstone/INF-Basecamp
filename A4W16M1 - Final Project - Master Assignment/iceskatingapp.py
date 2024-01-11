import os
import re
import sys
import json
import sqlite3

from skater import Skater
from track import Track
from event import Event


def main():
    prepare()

    db = Database()

    s = Skater(
        id=-1,
        first_name='Bob',
        last_name='Bobson',
        nationality='NL',
        gender='Male',
        date_of_birth='01-01-2000',
        database=db
    )
    s.insert_skater()

    # s.print_all_attributes_but_fancy("Overview")

    # t = Track(
    #     id=1,
    #     name='Sample Track',
    #     city='Sample City',
    #     country='Sample Country',
    #     outdoor=True,
    #     altitude=1000
    # )
    #
    # t.print_all_attributes_but_fancy("Overview")
    #
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

    # e.print_all_attributes_but_fancy("Overview")

    e.add_skater(s)


def prepare():
    conn = sqlite3.connect(os.path.join(sys.path[0], 'iceskatingapp.db'))

    conn.execute('''DELETE FROM skaters''')
    conn.execute('''DELETE FROM event_skaters''')
    conn.execute('''UPDATE sqlite_sequence SET seq = 0 WHERE name = "skaters"''')
    conn.execute('''UPDATE sqlite_sequence SET seq = 0 WHERE name = "event_skaters"''')
    conn.commit()
    conn.close()


class Database:
    def db_connect(self):
        db_file = os.path.join(sys.path[0], 'iceskatingapp.db')

        if not os.path.exists(db_file):
            print(f"Error - Database file {db_file} does not exist")
            return

        conn = sqlite3.connect(db_file)

        if conn is None:
            print(f"Error - Failed to connect to {os.path.basename(db_file)}")
        else:
            print(f"Successfully connected to: {os.path.basename(db_file)}")
        return conn


if __name__ == "__main__":
    main()
