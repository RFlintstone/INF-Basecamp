import datetime


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

    def __init__(self) -> None:
        pass

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    # add_skater(skater: Skater) (adds skater to event table event_skaters via the id of the passed
    # skater object and the id of this event
    def add_skater(self, skater) -> None:
        pass

    # get_skaters() (returns a list of Skaters
    # search in table event_skaters for all skater_id’s on this event, search all skaters with those id’s
    def get_skaters(self) -> list:
        pass

    # get_track () (returns Track object)
    # def get_track(self) -> Track:
    #     pass

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
        temp_time = datetime.datetime.fromtimestamp(self.duration/1000.0)  # Convert milliseconds to seconds
        return temp_time.strftime(to_format)