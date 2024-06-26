import importlib
import os
import sys
import sqlite3
from datetime import datetime


class Skater:
    _last_id = 0

    def __init__(self, id: int, first_name: str, last_name: str, nationality: str,
                 gender: str, date_of_birth: datetime.date, database) -> None:
        self.database = database
        self.database.db_fetch(table="skaters", silent=True)

        self.id = self.database.lastrowid
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth

        Skater._last_id += 1

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    def get_age(self, date: datetime = datetime.now()) -> int:
        if isinstance(self.date_of_birth, str):
            self.date_of_birth = datetime.strptime(self.date_of_birth, "%m-%d-%Y").date()
        return date.year - self.date_of_birth.year

    def get_events(self) -> list:
        return self.__repr__()

    @classmethod # I opted in for classmethod because it lets 'get_lastid()' work with information that's the same for all Skater objects, not just one individual one.
    def get_lastid(self) -> int:
        return self._last_id

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
