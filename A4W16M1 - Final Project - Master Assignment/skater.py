from datetime import datetime

class Skater:
    def __init__(self, id: int, first_name: str, last_name: str, nationality: str,
                 gender: str, date_of_birth: datetime.date) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    def get_age(self, date: datetime = datetime.now()) -> int:
        if isinstance(self.date_of_birth, str):
            self.date_of_birth = datetime.strptime(self.date_of_birth, "%m-%d-%Y").date()
        return date.year - self.date_of_birth.year

    def get_events(self) -> list:
        return self.__repr__()