# Arch 4

## Assignment: A4W13A1 - Car parking final

### Creation Date: 11-14-2023

### What did I learn?
I learned that you need to commit your changed with sqllite3 otherwhise it won't properly update the database.

### How did I learn it?
Mostly through trial and error and a bit of research.

### Why/how did I solve it?
With the car parking assessment I created a 'quick-test.py' file, so I could easily check if the code what was being run by codegrade was passing in the IDE. If it was then I pretty much knew Codegrade would accept it as well. (Although there were instances where the behaviour was different)

## Code Snippet
```python
# Drop and create database for a new run using __init__  
def __init__(self, id: chr, capacity: int = 10, hourly_rate: float = 2.50, parked_cars=None):
    """
    :param id: The unique identifier for the CarParkingMachine. It should be a single character.
    :param capacity: The maximum number of cars that can be parked in the CarParkingMachine. Default value is 10.
    :param hourly_rate: The hourly rate of parking in the CarParkingMachine. Default value is 2.50.
    :param parked_cars: A dictionary that stores the parked cars and their corresponding parking details.
                       If not provided, an empty dictionary will be used.
    """
    # check if parked_cars is None and set it to an empty dict if it is
    if parked_cars is None:
        parked_cars = {}

    self.id = id
    self.capacity = capacity
    self.hourly_rate = hourly_rate
    self.parked_cars = parked_cars
    self.parked_cars_stored = []
    self.logger = CarParkingLogger(id)
    self.json_file = f"{id}_state.json"
    self.db_conn = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
    self.db_conn.execute('''DROP TABLE IF EXISTS parkings;''')
    self.db_conn.execute(
        '''CREATE TABLE IF NOT EXISTS parkings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_parking_machine TEXT NOT NULL,
            license_plate TEXT NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT DEFAULT NULL,
            parking_fee NUMERIC DEFAULT 0 
        );'''
    )
    self.check_table_exists(self.db_conn, "parkings")
```
