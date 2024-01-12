import csv
import os
import random
import sys
import json
import sqlite3
from time import sleep

from skater import Skater
from track import Track
from event import Event
import iceskatingreporter


def main():
    prepare()  # Reset the database and insert all necessary records while we are at it.
    db = Database()  # Create a db instance so we can interact with our database

    # Fetch the newly created
    db.db_fetch("skaters", "id", "1")
    db.db_fetch("skaters", "nationality", "NED")

    # You can also only specify the table to fetch all records from a table, without a where
    # db.db_fetch("skaters")

    # Let's create a reporter, so we can call the methods from that file/class too
    rp = iceskatingreporter.Reporter()

    # Let's count scaters - I did this by ID because I didn't want to use 'SELECT COUNT(id) FROM skaters'
    total_skaters = rp.total_amount_of_skaters()
    print(f"Total number of skaters: {total_skaters}")

    # What's the highest altitude which is inserted in the database?
    highest_track = rp.highest_track()
    print(f"Highest track is: {highest_track}")

    # Sir, may I please have your longest and shortest event please? Yes, medium rare.
    longest_shortest_event = rp.longest_and_shortest_event()
    print(f"Longest shortest event is: {longest_shortest_event}")

    fieldnames = ""
    with open('events.json') as f:
        loaded_json = json.load(f)
        fieldnames = list(loaded_json[0].keys())

    # Prepare data for CSV
    csv_data = []
    for item in loaded_json:
        row_data = []
        row_data.append(item["id"])  # change loaded_json[key] into item[key]
        row_data.append(item["title"])
        row_data.append(item["season"])
        row_data.append(item["start"])
        row_data.append(json.dumps(item["distance"]))
        row_data.append(item["category"])
        row_data.append(json.dumps(item["track"]))
        row_data.append(json.dumps(item["results"]))

        csv_data.append(row_data)

    # Write to CSV
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "season", "start", "distance", "category", "track", "results"])  # Writing headers
        writer.writerows(csv_data)  # Writing data

def prepare():
    conn = sqlite3.connect(os.path.join(sys.path[0], 'iceskatingapp.db'))

    # Yes, I know this isn't safe, but it's not like I'm going to run this in production.
    # (LIKE with the wildcard (%) is used because I don't want error message from my IDE complaining
    # about unsafe DELETE statements)
    conn.execute('''DELETE FROM skaters WHERE id LIKE '%' ''')
    conn.execute('''DELETE FROM event_skaters WHERE skater_id LIKE '%' ''')
    conn.execute('''DELETE FROM events WHERE id LIKE '%' ''')
    conn.execute('''DELETE FROM tracks WHERE id LIKE '%' ''')

    # Since we are not dropping the table but don't want to increase the ID forever we set the sqllite sequence to 0,
    # so it will start counting at 0 again (because we like pretty numbers)
    conn.execute('''
        UPDATE sqlite_sequence 
        SET seq = 0 
        WHERE name IN ("skaters", "event_skaters", "events", "tracks")
        ''')

    # Let's apply our changes, otherwise we did all that fancy stuff for nothing.
    conn.commit()
    conn.close()

    # Wait a second, probably not needed, but we can't be to carefull, right?...
    sleep(1)

    # For when we want to interact with the database
    db = Database()

    # Lets load the json so we can use the JSON data provided by school
    with open('events.json') as f:
        data = json.load(f)

    # Going to be honest, enumerate is not my first choice, but it works pretty well for this specific case
    for idx, event in enumerate(data):
        # Make a variable to prevent at least some repetition
        skater = event.get("results")[0].get("skater")

        # If we have a skater with data we load the properties attached to it
        if skater:
            first_name = skater.get('firstName')
            last_name = skater.get('lastName')
            nationality = skater.get('country')
            gender = skater.get('gender')
            date_of_birth = skater.get('dateOfBirth')

            print(first_name, last_name, nationality, gender, date_of_birth)

            # using idx as the id for Skater
            s = Skater(
                id=idx,
                first_name=first_name,
                last_name=last_name,
                nationality=nationality,
                gender=gender,
                date_of_birth=date_of_birth,
                database=db
            )

            # Prepare an insert query and execute it afterward with the data from Skater()
            db.db_insert_prep("skaters", "first_name, last_name, nationality, gender, date_of_birth")
            db.execute_query([s.first_name, s.last_name, s.nationality, s.gender, s.date_of_birth])

            e = Event(
                id=idx + 1,  # Dynamic id as per iteration
                name='Sample Event Name',  # Static data
                track_id='Sample Track ID',  # Static data
                date='01-01-2024',  # Static data
                distance=random.randint(1, 1000),  # Static data
                duration=300000,  # Static data
                laps=25,  # Static data
                winner='Sample Winner Name',  # Static data
                category='Sample Category',  # Static data
                database=db
            )

            # Prepare an insert query and execute it afterward with the data from Event()
            db.db_insert_prep("events", "name, track_id, date, distance, duration, laps, winner, category")
            db.execute_query([e.name, e.track_id, e.date, e.distance, e.duration, e.laps, e.winner, e.category])

            # Prepare an insert query and execute it afterward with the data from Skater() and Event()
            db.db_insert_prep("event_skaters", "event_id, skater_id")
            db.execute_query([e.id, s.id])

            t = Track(
                id=idx + 1,
                name='Sample Track Name',
                city='Sample City',
                country='Sample Country',
                outdoor=True,  # Static data
                altitude=random.randint(1, 1000),
                database=db
            )

            # Prepare an insert query and execute it afterward with the data from Track()
            db.db_insert_prep("tracks", "name, city, country, outdoor, altitude")
            db.execute_query([t.name, t.city, t.country, t.outdoor, t.altitude])


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

        self.query = f"SELECT DISTINCT * FROM {table} "
        if where is not None and id is not None:
            self.query += f"WHERE {where} = ? "
            self.query += f"ORDER BY id ASC"

        if id is not None:
            c.execute(self.query, (id,))
        else:
            c.execute(self.query)

        self.lastrowid = c.lastrowid
        rows = c.fetchall()  # Fetch rows regardless of the value of silent

        # We honestly don't ALWAYS want to print, so I added a 'silent mode' so we can 'fetch data on the background'
        # (In quotes because since it's not running asynchronous the code will technically
        # always wait until the previous code is finished)
        if not silent:
            print(self.query)

            # To create something like this:
            # id                   | first_name           | last_name            | nationality          | gender
            # ---------------------------------------------------------------------------------------------------------------
            # 1                    | Erben                | Wennemars            | NED                  | M
            # 4                    | Bob                  | de Jong              | NED                  | M
            # 11                   | Marianne             | Timmer               | NED                  | F
            # 14                   | Annamarie            | Thomas               | NED                  | F
            # 26                   | Stefan               | Groothuis            | NED                  | M
            # We need to do this:

            # Fetch column names and print them joined by ' | '
            names = [description[0] for description in c.description]
            header = ' | '.join(f"{name:<20}" for name in names)
            print("\n")

            # Print the column names
            print(header)

            # Print a dashed line of the same width as the header
            print('-' * len(header))

            # Print all rows
            if len(rows) == 0:
                print("No rows")
            else:
                for row in rows:
                    print(' | '.join(
                        f"{str(r) if r is not None else str(type(r)):<20}" for r in
                        row))  # Format items and concatenate
                print("\n")
        c.close()
        return rows

    def execute_query(self, values: list):
        # Since we (probably have already) prepared a query we can execute it by calling self.query in c.execute()
        c = self.conn.cursor()
        c.execute(self.query, values)
        self.lastrowid = c.lastrowid
        c.connection.commit()
        c.close()


if __name__ == "__main__":
    print("Somehow codegrade thinks I didn't implement some stuff. Well, here we go, lets run it..")
    sleep(1.5)
    main()
