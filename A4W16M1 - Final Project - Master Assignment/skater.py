import importlib
import os
import sys
import sqlite3
from datetime import datetime


class Skater:
    def __init__(self, id: int, first_name: str, last_name: str, nationality: str,
                 gender: str, date_of_birth: datetime.date, database) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.database = database
        self.db_conn = self.database.db_connect()

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    def get_age(self, date: datetime = datetime.now()) -> int:
        if isinstance(self.date_of_birth, str):
            self.date_of_birth = datetime.strptime(self.date_of_birth, "%m-%d-%Y").date()
        return date.year - self.date_of_birth.year

    def get_events(self) -> list:
        return self.__repr__()

    def insert_skater(self):
        # Create a database connection
        insert_sql = '''INSERT INTO skaters (first_name, last_name, nationality, gender, date_of_birth) VALUES (?, ?, ?, ?, ?)'''
        c = self.db_conn.cursor()

        c.execute(insert_sql, (self.first_name, self.last_name, self.nationality, self.gender, self.date_of_birth))
        self.id = c.lastrowid

        c.connection.commit()
        c.close()

        self.fetch_scater()

    def fetch_scater(self):
        # Create a database connection
        c = self.db_conn.cursor()
        c.execute("SELECT * FROM skaters")

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
