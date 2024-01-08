import datetime


class Skater:
    id: int
    first_name: str
    last_name: str
    nationality: str
    gender: str
    date_of_birth: datetime.date

    def __init__(self) -> None:
        pass

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    # get_age(date: date = now()) (returns the age in years from a specific date/or today)
    def get_age(self, date: datetime = datetime.datetime.now()) -> int:
        pass

    # get_events() (returns a list of Event’s)
    def get_events(self) -> list:
        pass
