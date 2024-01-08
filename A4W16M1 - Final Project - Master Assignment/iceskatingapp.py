import os
import sys
import json
import sqlite3

from skater import Skater
# from track import Track
from event import Event


def main():
    s = Skater(
        id=1,
        first_name='First name',
        last_name='Last name',
        nationality='Nationality',
        gender='Gender',
        date_of_birth='01-01-2000'
    )

    # Print age
    # age = s.get_age()
    # print(age)

    e = Event()

    # e.date = "01-01-2000"
    # print(e.date)
    # print(e.convert_date("%Y-%m-%d"))

    # e.duration = 300000
    # print(e.convert_duration("%M:%S"))




if __name__ == "__main__":
    main()