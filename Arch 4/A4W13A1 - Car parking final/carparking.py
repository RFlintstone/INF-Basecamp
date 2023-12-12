import os
import math
import json
import sys
import sqlite3
from datetime import datetime


class ParkedCar:
    """
    The ParkedCar class represents a car that is parked in a parking lot. It stores information about the license plate of the car and the time it was parked.

    Constructor:
        def __init__(self, license_plate: str, check_in: datetime):
            Initializes a new instance of the ParkedCar class.

    Methods:
        def to_json(self, action: str) -> dict:
            Converts the ParkedCar object to a JSON format.
    """

    def __init__(self, license_plate: str, check_in: datetime):
        """
        :param license_plate: The license plate of the parked car.
        :type license_plate: str
        :param check_in: The time the car is parked.
        :type check_in: datetime.datetime
        """

        self.id = None
        self.parking_fee = None
        self.check_out = None
        self.license_plate = license_plate  # license plate of the car
        self.check_in = check_in  # time the car is parked

    def to_json(self) -> dict:
        """
        Converts the ParkedCar object to a JSON format.
        :param action: The action associated with the ParkedCar object (e.g., "check_in", "check_out").
        :return: A dictionary representing the ParkedCar object in JSON format.
        """

        return {
            'license_plate': self.license_plate,
            'check-in': self.check_in.strftime("%m-%d-%Y %H:%M:%S") if self.check_in else None,
            'check-out': self.check_out.strftime("%m-%d-%Y %H:%M:%S") if self.check_out else None,
        }


class CarParkingLogger:
    """
    Car Parking Logger
    ================
    A class to handle logging and calculations for a car parking system.

    Methods
    -------
    __init__(id: str, log_file: str = "carparklog.txt")
        Initializes a new instance of the CarParkingLogger class.

    get_total_car_fee(license_plate: str) -> float
        Calculates the total fee accumulated by a car with the given license plate number.

    get_machine_fee_by_day(cpm_name: str, date: str) -> float
        Calculates the total fee for a specific car parking machine on a given day.

    add_check_in(cpm_name: str, license_plate: str, action: str) -> str
        Adds a check-in to the log file.

    add_check_out(cpm_name: str, license_plate: str, action: str, parking_fee: float) -> str
        Adds a check-out entry to the log file.

    open_log_file() -> TextIOWrapper
        Opens and returns the log file.

    read_log_file() -> str
        Reads the content of the log file and returns it.

    write_to_log_file(new_line: str) -> bool
        Writes a new line to the log file.

    Attributes
    ----------
    id: str
        The ID of the car parking logger.

    log_file: str
        The name of the log file.
    """

    def __init__(self, id: str, log_file: str = "carparklog.txt"):
        """
        Initialize a new instance of the CarParkingLogger class.

        :param id: A string representing the ID of the car parking logger.
        :param log_file: A string representing the name of the log file. Default value is "carparklog.txt".
        """
        self.id = id
        self.log_file = log_file

    def get_total_car_fee(self, license_plate: str):
        """
        :param license_plate: The license plate number of the car.
        :return: The total fee accumulated by the car with the given license plate.

        This method calculates the total fee accumulated by a car with the given license plate number. It reads a log file line by line and searches for the license plate number. If found, it extracts the parking fee from the line and adds it to the total fee. The method then rounds the total fee to 2 decimal places and returns it.

        Example usage:
        car_parking_logger = CarParkingLogger()
        license_plate_number = "ABC123"
        total_fee = car_parking_logger.get_total_car_fee(license_plate_number)
        print(total_fee)  # Output: 15.5
        """
        # open the log file in read mode
        log_file = open(self.log_file, "r")

        # read the file line by line and calculate the total fee for the given license plate
        total_fee = 0
        for line in log_file:
            if license_plate in line:
                line_parts = line.split(";")
                for part in line_parts:
                    if "parking_fee=" in part:
                        fee = float(part.split("=")[1])
                        total_fee += fee

        # close the file
        log_file.close()

        # round the total fee to 2 decimals and return it
        rounded_total_car_fee = round(total_fee, 2)
        return rounded_total_car_fee

    def get_machine_fee_by_day(self, cpm_name: str, date: str):
        """
        :param cpm_name: The name of the car parking machine to calculate the fee for.
        :param date: The date for which the fee should be calculated in the format 'YYYY-MM-DD'.
        :return: The total fee for the given day and machine.

        This method calculates the total fee for a specific car parking machine on a given day. It reads a log file
        and searches for lines that match the specified car parking machine name and date. It then extracts the
        parking fee from each matching line and calculates the total fee by summing them up. The rounded total fee is
        returned.

        Example usage:
            parking_logger = CarParkingLogger()
            machine_fee = parking_logger.get_machine_fee_by_day('CPM1', '2021-01-01')
            print(machine_fee)  # Output: 15.0
        """
        # replace spaces with underscores
        cpm_name = cpm_name.replace(" ", "_")

        # open the log file in read mode
        log_file = open(self.log_file, "r")

        # read the file line by line and calculate the total fee for the given day and machine
        total_fee = 0
        for line in log_file:
            if f"cpm_name={cpm_name}" in line and date in line:
                line_parts = line.split(";")
                for part in line_parts:
                    if "parking_fee=" in part:
                        fee = float(part.split("=")[1])
                        total_fee += fee

        # close the file
        log_file.close()

        # round the total fee to 2 decimals and return it
        rounded_total_car_fee = round(total_fee, 2)
        return rounded_total_car_fee

    def add_check_in(self, cpm_name: str, license_plate: str, action: str):
        """
        :param cpm_name: The name of the car parking meter.
        :param license_plate: The license plate of the car.
        :param action: The action performed, such as check-in or check-out.
        :return: The name of the car parking meter.

        This method adds a check-in to the log file. It gets the current date and time and formats them.
        It then replaces spaces with underscores in the car parking meter name, license plate, and action.
        Finally, it writes the line to the log file and reads the log file again.

        Example usage:
            parking_logger = CarParkingLogger()
            cpm_name = "CPM1"
            license_plate = "ABC123"
            action = "check-in"
            parking_logger.add_check_in(cpm_name, license_plate, action)
        """
        # get the current date and time and format them
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        # replace spaces with underscores, just in case
        cpm_name = cpm_name.replace(" ", "_")
        license_plate = license_plate.replace(" ", "_")
        action = action.replace(" ", "_")

        # write the line to the log file
        write = self.write_to_log_file(
            f"{date} {time};"
            f"cpm_name={cpm_name};"
            f"license_plate={license_plate};"
            f"action={action}\n"
        )

        # check if writing was successful and read the log file
        if write:
            self.read_log_file()

        # return the cpm_name which we could use to check if the check-in was successful
        return cpm_name

    def add_check_out(self, cpm_name: str, license_plate: str, action: str, parking_fee: float):
        """
        :param cpm_name: The name of the car parking machine
        :param license_plate: The license plate of the car
        :param action: The action performed (e.g. check-out)
        :param parking_fee: The parking fee charged
        :return: The name of the car parking machine

        This method adds a check-out entry to the log file. It takes the car parking machine name, license plate,
        action, and parking fee as parameters. It gets the current date and time, formats them, and replaces any
        spaces in the parameters with underscores. It then writes the formatted line to the log file using the
        write_to_log_file method. After writing, it checks if writing was successful and reads the log file using
        the read_log_file method. Finally, it returns the car parking machine name as confirmation of the successful
        check-out.
        """
        # get the current date and time and format them
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        # replace spaces with underscores, just in case
        cpm_name = cpm_name.replace(" ", "_")
        license_plate = license_plate.replace(" ", "_")
        action = action.replace(" ", "_")

        # write the line to the log file
        write = self.write_to_log_file(
            f"{date} {time};"
            f"cpm_name={cpm_name};"
            f"license_plate={license_plate};"
            f"action={action};parking_fee={parking_fee:.2f}\n"
        )

        # check if writing was successful and read the log file
        if write:
            self.read_log_file()

        # return the cpm_name which we could use to check if the check-out was successful
        return cpm_name

    def open_log_file(self):
        """
        Open and return the log file.
        Checks if the log file exists, if not, creates it. Then opens the log file in "a" (append) mode.

        :return: The opened log file.
        """
        # check if the log file exists, if not create it
        if not os.path.exists(self.log_file):
            open(self.log_file, "w").close()

        # open the log file
        log_file = open(self.log_file, "a")

        # return the file, so we can use it to write to it
        return log_file

    def read_log_file(self):
        """
        Reads the content of a log file and returns it.

        :param self: The instance of the CarParkingLogger class.
        :return: The content of the log file.
        """
        # Open the log file and read the content
        with open(self.log_file) as f:
            file_content = f.read()

        # Print the content
        print(file_content)

        # Return the content
        return file_content

    def write_to_log_file(self, new_line: str):
        """
        Write a new line to the log file.

        :param new_line: The new line to be written to the log file.
        :type new_line: str
        :return: True if writing was successful.
        :rtype: bool
        """
        # open the log file
        with self.open_log_file() as log_file:
            # use seek to start writing at the beginning of the file and write the new line
            log_file.seek(0)
            log_file.write(new_line)

            # truncate the file to the current position and close the file
            log_file.truncate()
            log_file.close()

        # return True to indicate that writing was successful
        return True


class CarParkingMachine:
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

    def check_table_exists(self, db_conn, table_name):
        """
        Check if a table exists in the specified database.

        :param db_conn:
        :param table_name:
        :return: none
        """
        cursor = db_conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")

        query_result = cursor.fetchone()
        if query_result:
            print(f"Table '{table_name}' exists.")
        else:
            print(f"Table '{table_name}' does not exist.")
        cursor.close()

    # This method will search for a parked_car in the database based on the row ID and return a ParkedCar object with
    # the data
    def find_by_id(self, id) -> ParkedCar:
        # Create a cursor and prepare the SQL statement
        cursor = self.db_conn.cursor()
        sql = '''
            SELECT * FROM parkings
            WHERE id = ?
            LIMIT 1;
            '''

        # Execute the SQL statement, fetch the row and close the cursor
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        cursor.close()

        # Set the license_plate and check_in variables from the row
        license_plate = list(row)[2]
        check_in_str = list(row)[3]

        # Correctly format the check_in string to a datetime object
        check_in = datetime.strptime(check_in_str, "%m-%d-%Y %H:%M:%S")

        # Return a ParkedCar object with the license_plate and check_in
        if row:
            return ParkedCar(license_plate, check_in)
        else:
            return None

    # This method will search for the last row for a given license_plate that has NOT checked-out yet (return row ID
    # if found)
    def find_last_checkin(self, license_plate) -> int:
        # Create a cursor and prepare the SQL statement
        cursor = self.db_conn.cursor()
        sql = '''
              SELECT id FROM parkings
              WHERE license_plate = ? AND check_out IS NULL
              ORDER BY id DESC
              LIMIT 1;
              '''

        # Execute the SQL statement, fetch the row and close the cursor
        cursor.execute(sql, (license_plate,))
        row = cursor.fetchone()
        cursor.close()

        # Return the row ID if found, otherwise return None
        if row is None:
            return None
        else:
            return row[0]

    # This method will insert details of a created ParkedCar object and put the new row ID (from database) on the
    # object, return the object with this new row ID
    def insert(self, parked_car: ParkedCar) -> ParkedCar:
        # Get the full car details in JSON format and extract the license_plate and check_in
        full_car = parked_car.to_json()

        # Create a list of the values from the JSON data
        values = []
        for key, value in full_car.items():
            if value is not None:
                values.append(value)
            else:
                values.append(None)
            print(f"{key}: {value}")

        # Prepare the SQL statement and execute it with the values from the list we just created
        sql = '''INSERT INTO parkings (car_parking_machine, license_plate, check_in, check_out) VALUES (?, ?, ?, ?)'''
        cursor = self.db_conn.cursor()
        cursor.execute(
            sql, (self.id, values[0], values[1], values[2])
        )

        parked_car.id = cursor.lastrowid

        # Close connection
        cursor.connection.commit()
        cursor.close()

        # Fetch all rows
        self.fetch_data()

    # This method will update details of a ParkedCar object inside the database (update based on ParkedCar.id <-
    # Database Row ID)
    def update(self, parked_car: ParkedCar) -> None:
        # Depending on your ParkedCar object implementation, generate the values to update
        car_parking_machine = self.id
        license_plate = parked_car.license_plate
        check_in = parked_car.check_in.strftime("%m-%d-%Y %H:%M:%S")
        check_out = parked_car.check_out.strftime("%m-%d-%Y %H:%M:%S") if parked_car.check_out else None
        parking_fee = float(parked_car.parking_fee) if parked_car.parking_fee is not None else None
        car_id = parked_car.id

        print("ASDASD", parked_car.to_json().get("license_plate"))
        print("ASDASDASD", car_id)
        # Prepare the SQL UPDATE query
        sql = '''
            UPDATE parkings
            SET car_parking_machine = ?, license_plate = ?, check_in = ?, check_out = ?, parking_fee = ?
            WHERE id = ?
            '''

        # Create cursor
        cursor = self.db_conn.cursor()

        # Execute the UPDATE query with the new values
        cursor.execute(sql, (car_parking_machine, license_plate, check_in, check_out, parking_fee, car_id))

        # Close the database connection
        cursor.connection.commit()
        cursor.close()

        # Fetch all rows
        self.fetch_data()

    def fetch_data(self):
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM parkings")

        # Fetch column names and print them spaced by ' | '
        names = [description[0] for description in cursor.description]
        header = ' | '.join(f"{name:<20}" for name in names)

        print("\n")

        # Print the column names
        print(header)

        # Print a dashed line of the same width as the header
        print('-' * len(header))

        # Fetch and print all rows
        rows = cursor.fetchall()
        for row in rows:
            print(' | '.join(f"{str(r) if r is not None else str(type(r)):<20}" for r in row))  # Format items and concatenate

        print("\n")
        cursor.close()

    def check_in(self, license_plate: str, check_in=None):
        """
        :param license_plate: The license plate of the car being checked in.
        :param check_in: The time of check-in. If not provided, it defaults to the current time.
        :return: True if the check-in was successful, False otherwise.
        """
        # check if the time is None and set it to datetime.now() if it is
        if check_in is None:
            check_in = datetime.now()

        # check if the garage is full
        if len(self.parked_cars) is self.capacity:
            # print that the garage is full
            print(False)
            print("Capacity reached - The garage is full")
            return False

        # check if the car is already parked
        if license_plate in self.parked_cars:
            print(f"{license_plate} is already checked in")
            return False

        # create a ParkedCar object with the license_plate and check_in time
        car = ParkedCar(license_plate, check_in.replace(microsecond=0))
        # insert the car into the database
        self.insert(car)

        # add the car to the parked_cars dict
        self.parked_cars[license_plate] = car

        # add the car to the parked_cars_stored list
        self.parked_cars_stored.append(car)

        # update the json file based on the current parked_cars dict
        self.json_save("check-in")

        # log the check-in
        self.logger.add_check_in(self.id, license_plate, "check-in")

        # print that the car is parked
        print(f"License registered - {license_plate} checked in at {check_in}")

        # check-in was successful, return True
        return True

    def check_out(self, license_plate: str):
        """
        Check out a car from the parking machine.

        :param license_plate: The license plate number of the car to check out.
        :return: The parking fee for the checked out car.
        """
        # variable to check if the car is checked in
        is_checked_in = False

        # check if the car is checked in
        if license_plate in self.parked_cars:
            is_checked_in = True

        # if the car is not checked in, print that the car is not checked in and return False
        if not is_checked_in:
            print(f"{license_plate} is not checked in")
            return False

        # if the car is checked in, remove the car from the parked_cars dict and return the parking fee
        if is_checked_in:
            # get the parking fee
            fee = self.get_parking_fee(license_plate)

            # print the fee
            print(fee)
            print(f"Parking fee: {fee:.2f} EUR")

            # log the check-out
            self.logger.add_check_out(self.id, license_plate, "check-out", fee)

            # Update the database with the check-out time and parking fee
            self.parked_cars[license_plate].check_out = datetime.now()
            self.parked_cars[license_plate].parking_fee = float(fee)
            self.update(self.parked_cars[license_plate])

            # update the json file based on the current parked_cars dict
            self.json_save("check-out")

            # remove the car from the parked_cars dict
            del self.parked_cars[license_plate]

            # return the fee - this is calculated in the get_parking_fee method
            return fee

    def get_parking_fee(self, license_plate: str):
        """
        :param license_plate: A string representing the license plate of the car.
        :return: The parking fee for the car, calculated based on the duration of stay and the hourly rate of the parking machine.
        """
        # check if the car is checked in, if not return 0
        if license_plate not in self.parked_cars:
            return 0

        # get the car from the parked_cars dict
        car = self.parked_cars[license_plate]

        # get the check-in time and calculate the duration from the check-in time to now
        check_in_time = car.check_in
        duration = datetime.now() - check_in_time

        # calculate the hours parked and round up to the next hour
        hours_parked = math.ceil(duration.total_seconds() / 3600)
        # hours_parked = math.ceil(duration.total_seconds())
        hours_parked = min(hours_parked, 24)

        # return the fee - this should max out at $60
        return hours_parked * self.hourly_rate

    def json_save(self, action):
        """
        :param action: The action to be saved in the JSON file.
        :return: None
        """
        # variable to store the existing json data
        existing = None

        # check if the json file exists and if it does, check if it has content and then load the data if any
        if os.path.exists(self.json_file):
            if os.path.getsize(self.json_file) > 0:
                with open(self.json_file) as f:
                    existing = json.load(f)

        # create a list to store the new data if existing is None
        if not existing:
            existing = []

        # create a list of the current parked_cars dict
        new_data = [car.to_json() for car in self.parked_cars.values()]

        # combine the existing and new data
        combined = existing + new_data

        print(new_data)
        # write the combined data to the json file
        with open(self.json_file, "w") as f:
            json.dump(combined, f)


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [I] Check-in car by license plate
# [O] Check-out car by license plate
# [Q] Quit program
def main():
    """
    Main function to run the Car Parking Machine program.

    :return: None
    """
    # create a CarParkingMachine object with id: str, capacity: int, hourly_rate: float, parked_cars: dict
    cpm = CarParkingMachine("North", 10, 2.50, None)

    # check if the json file exists and if it does remove it, so we can start fresh
    if os.path.exists(cpm.json_file):
        os.remove(cpm.json_file)

    # set DEBUG_MODE, so we can check in and out cars without entering license plates
    DEBUG_MODE = False

    # set should_quit too False to start the loop
    should_quit = False

    # run the loop until should_quit is True
    while not should_quit:
        # print the menu every iteration of the loop
        print("[I] Check-in car by license plate\n[O] Check-out car by license plate\n[Q] Quit program\n")

        # get the choice from the user
        choice = input("Enter your choice: ").upper() if DEBUG_MODE else input().upper()

        # check if the user wants to check in
        if choice == "I":
            license_plate = input("Enter license plate: ") if not DEBUG_MODE else "AA-123-B"
            print(f"Checking in {license_plate}...")
            cpm.check_in(license_plate)

        # check if the user wants to check out
        elif choice == "O":
            license_plate = input("Enter license plate: ") if not DEBUG_MODE else "AA-123-B"
            print(f"Checking out {license_plate}...")
            cpm.check_out(license_plate)

        # check if the user wants to quit the program
        elif choice == "Q":
            should_quit = True

    # When the user quits the program (exit loop), print a goodbye message
    print("Exiting program...") if DEBUG_MODE else print()


if __name__ == "__main__":
    main()
