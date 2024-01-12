class Track:
    id: int
    name: str
    city: str
    country: str
    outdoor: bool
    altitude: int

    def __init__(self, id: int, name: str, city: str, country: str, outdoor: bool, altitude: int, database) -> None:
        self.id = id
        self.name = name
        self.city = city
        self.country = country
        self.outdoor = outdoor
        self.altitude = altitude
        Track.database = database

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

    # get_events() (returns a list of Event’s for this track)
    @classmethod
    def get_events(cls) -> list:
        track_data = cls.database.db_fetch("tracks")
        track_objects = []

        for data in track_data:
            track = Track(
                id=data[0],
                name=data[1],
                city=data[2],
                country=data[3],
                outdoor=data[4],
                altitude=data[5],
                database=cls.database
            )
            track_objects.append(track)

        return track_objects

    def print_all_attributes_but_fancy(self, task_name: str = "") -> None:
        name = type(self).__name__
        if task_name is not None and task_name != "":
            name = f"{type(self).__name__} - {task_name}"

        print(name.center(34, '='))

        if len(self.__dict__.keys()) > 0:
            max_length = max(len(key) for key in self.__dict__)
            for key, value in self.__dict__.items():
                print(key.ljust(max_length), "->", value)
        else:
            print("No attributes")