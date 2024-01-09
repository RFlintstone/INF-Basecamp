import datetime
import os
import sqlite3
import sys

from skater import Skater
from track import Track

class Event:
    id: int
    name: str
    track_id: int
    date: datetime
    distance: int
    duration: float
    laps: int
    winner: str
    category: str

    def __init__(self, id: int, name: str, track_id: int, date: datetime, distance: int, duration: float, laps: int, winner: str, category: str) -> None:
        self.id = id
        self.name = name
        self.track_id = track_id
        self.date = date
        self.distance = distance
        self.duration = duration
        self.laps = laps
        self.winner = winner
        self.category = category
        self.db_conn = sqlite3.connect(os.path.join(sys.path[0], 'iceskatingapp.db'))


    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    # add_skater(skater: Skater) (adds skater to event table event_skaters via the id of the passed
    # skater object and the id of this event
    def add_skater(self, skater: Skater) -> None:
        skater.print_all_attributes_but_fancy("Adding Skater")
        c = self.db_conn.cursor()

        # Create a new record in the 'event_skaters' table with the current event's ID and the skater's ID
        c.execute("INSERT INTO event_skaters (event_id, skater_id) VALUES (?, ?)", (self.id, skater.id))
        last_id = c.lastrowid

        self.db_conn.commit()
        c.close()

        self.fetch_event_skaters(last_id)

    def fetch_event_skaters(self, skater_id: int) -> None:
        c = self.db_conn.cursor()
        c.execute("SELECT * FROM event_skaters WHERE skater_id = ?", (skater_id,))

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


    # get_skaters() (returns a list of Skaters
    # search in table event_skaters for all skater_id’s on this event, search all skaters with those id’s
    def get_skaters(self) -> list:
        pass

    # get_track () (returns Track object)
    def get_track(self) -> Track:
        pass

    # convert_date(to_format: string) (returns converted date of this event in the provided datetime
    # format)
    # (example: %M:%S will return minutes:seconds, options are: %M = minutes, %S = seconds)
    def convert_date(self, to_format: str) -> str:
        if isinstance(self.date, str):
            self.date = datetime.datetime.strptime(self.date, "%d-%m-%Y")

        return self.date.strftime(to_format)

    # convert_duration(to_format: string) (returns converted duration in the provided datetime
    # format)
    # (example: %M:%S will return minutes:seconds, options are: %M = minutes, %S = seconds)
    def convert_duration(self, to_format: str) -> str:
        temp_time = datetime.datetime.fromtimestamp(self.duration / 1000.0)  # Convert milliseconds to seconds
        return temp_time.strftime(to_format)

    def print_all_attributes_but_fancy(self, task_name: str = "") -> None:
        name = type(self).__name__
        if task_name is not None and task_name != "":
            name = f"{type(self).__name__} - {task_name}"

        print(name.center(34, '='))

        if len(self.__dict__.keys()) > 0:
            max_length = max(len(key) for key in self.__dict__)  # Find the maximum length of keys
            for key, value in self.__dict__.items():
                print(key.ljust(max_length), "->", value)
        else:
            print("No attributes")
