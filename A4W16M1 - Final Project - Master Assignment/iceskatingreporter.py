from datetime import datetime

from operator import attrgetter

from event import Event
from skater import Skater
from track import Track


class Reporter:

    def total_amount_of_skaters(self) -> int:
        return Skater.get_lastid()

    def highest_track(self) -> Track:
        return max(Track.get_events(), key=attrgetter('altitude'))

    def longest_and_shortest_event(self) -> tuple[Event, Event]:
        events_sorted = sorted(Event.get_events(), key=attrgetter('duration'))
        return events_sorted[-1], events_sorted[0]

        # Which event has the most laps for the given track_id -> tuple[Event, ...]
        def events_with_most_laps_for_track(self, track_id: int) -> tuple[Event, ...]:
            pass

        # Which skaters have made the most events -> tuple[Skater, ...]
        # Which skaters have made the most succesful events -> tuple[Skater, ...]
        def skaters_with_most_events(self, only_wins: bool = False) -> tuple[Skater, ...]:
            pass

    def tracks_with_most_events(self) -> tuple[Track, ...]:
        track_events = [(i, len(i.get_events())) for i in Track.get_tracks()]
        max_events = max(i[1] for i in track_events)
        return tuple(i[0] for i in track_events if i[1] == max_events)

    def get_first_event(self, outdoor_only: bool = False) -> Event:
        track_events = Event.get_events().sort(key = attrgetter('date'))
        if outdoor_only:
            track_events = [i for i in track_events if i.track.outdoor]
        return track_events[0]

        # Which track had the latest event? -> event
        # Which track had the latetstoutdoor event? -> event
        def get_latest_event(self, outdoor_only: bool = False) -> Event:
            pass

        # Which skaters have raced track Z between period X and Y? -> tuple[Skater, ...]
        # Based on given parameter `to_csv = True` should generate CSV file as  `Skaters on Track Z between X and Y.csv`
        # example: `Skaters on Track Kometa between 2021-03-01 and 2021-06-01.csv`
        # date input always in format: YYYY-MM-DD
        # otherwise it should just return the value as tuple(Skater, ...)
        # CSV example (this are also the headers):
        #   id, first_name, last_name, nationality, gender, date_of_birth
        def get_skaters_that_skated_track_between(self, track: Track, start: datetime, end: datetime,
                                                  to_csv: bool = False) -> tuple[Skater, ...]:
            pass

        # Which tracks are located in country X? ->tuple[Track, ...]
        # Based on given parameter `to_csv = True` should generate CSV file as  `Tracks in country X.csv`
        # example: `Tracks in Country USA.csv`
        # otherwise it should just return the value as tuple(Track, ...)
        # CSV example (this are also the headers):
        #   id, name, city, country, outdoor, altitude
        def get_tracks_in_country(self, country: str, to_csv: bool = False) -> tuple[Track, ...]:
            pass

        # Which skaters have nationality X? -> tuple[Skater, ...]
        # Based on given parameter `to_csv = True` should generate CSV file as  `Skaters with nationality X.csv`
        # example: `Skaters with nationality GER.csv`
        # otherwise it should just return the value as tuple(Skater, ...)
        # CSV example (this are also the headers):
        #   id, first_name, last_name, nationality, gender, date_of_birth
        def get_skaters_with_nationality(self, nationality: str, to_csv: bool = False) -> tuple[Skater, ...]:
            pass
