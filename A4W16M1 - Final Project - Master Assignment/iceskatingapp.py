import os
import re
import sys
import json
import sqlite3

from skater import Skater
from track import Track
from event import Event


def main():
    s = Skater(
        id=1,
        first_name='Bob',
        last_name='Bobson',
        nationality='NL',
        gender='Male',
        date_of_birth='01-01-2000'
    )

    s.print_all_attributes_but_fancy("Overview")

    t = Track(
        id=1,
        name='Sample Track',
        city='Sample City',
        country='Sample Country',
        outdoor=True,
        altitude=1000
    )

    t.print_all_attributes_but_fancy("Overview")

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

    e.print_all_attributes_but_fancy("Overview")

    e.add_skater(s)


if __name__ == "__main__":
    main()
