class Track:
    id: int
    name: str
    city: str
    country: str
    outdoor: bool
    altitude: int

    def __init__(self) -> None:
        pass

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    # get_events() (returns a list of Event’s for this track)
    def get_events(self) -> list:
        pass