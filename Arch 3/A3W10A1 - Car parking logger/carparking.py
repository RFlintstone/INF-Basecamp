import os
import math
from datetime import datetime


# ParkedCar class to store information of parked cars.
class ParkedCar:
    # Day car parking machine. Max parking fee is 24 hours (hourly_rate * 24).
    def __init__(self, license_place: str, check_in: datetime):
        self.license_place = license_place  # license plate of the car
        self.check_in = check_in  # time the car is parked


# log a car check-in and a method to log a car check-out. The class should use an id to identify for which parking
# machine this logger is. Every check-in and check-out should write a line to a logfile named 'carparklog.txt' which
# is shared by all car parking machines.
class CarParkingLogger:
    def __init__(self, id: str, log_file: str = "carparklog.txt"):
        self.id = id
        self.log_file = log_file

    def get_total_car_fee(self, license_plate: str):
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

        # close the file and return the total fee
        log_file.close()
        rounded_total_car_fee = round(total_fee, 2)
        return rounded_total_car_fee

    def get_machine_fee_by_day(self, cpm_name: str, date: str):
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

        # close the file and return the total fee
        log_file.close()
        rounded_total_car_fee = round(total_fee, 2)
        return rounded_total_car_fee

    def add_check_in(self, cpm_name: str, license_plate: str, action: str):
        # get the current date and time
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        # replace spaces with underscores
        cpm_name = cpm_name.replace(" ", "_")
        license_plate = license_plate.replace(" ", "_")
        action = action.replace(" ", "_")

        # write the line to the log file
        write = self.write_to_log_file(f"{date} {time};cpm_name={cpm_name};license_plate={license_plate};"
                                       f"action={action}\n")
        if write:
            self.read_log_file()
        return cpm_name

    def add_check_out(self, cpm_name: str, license_plate: str, action: str, parking_fee: float):
        # get the current date and time
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        # replace spaces with underscores
        cpm_name = cpm_name.replace(" ", "_")
        license_plate = license_plate.replace(" ", "_")
        action = action.replace(" ", "_")

        # write the line to the log file
        write = self.write_to_log_file(f"{date} {time};cpm_name={cpm_name};license_plate={license_plate};"
                                       f"action={action};parking_fee={parking_fee:.2f}\n")
        if write:
            self.read_log_file()
        return cpm_name

    def open_log_file(self):
        # check if the log file exists, if not create it
        if not os.path.exists(self.log_file):
            open(self.log_file, "w").close()

        # open the log file
        log_file = open(self.log_file, "a")

        # return the file
        return log_file

    def read_log_file(self):
        # Open file to read
        with open(self.log_file) as f:
            file_content = f.read()

        # Print the content
        print(file_content)

        # Return the content
        return file_content

    def write_to_log_file(self, new_line: str):
        # open the log file
        log_file = self.open_log_file()

        # use seek to start writing at the beginning of the file and write the new line
        log_file.seek(0)
        log_file.write(new_line)

        # truncate the file to the current position and close the file
        log_file.truncate()
        log_file.close()

        return True


# CarParkingMachine class to store information of the car parking machine.
class CarParkingMachine:
    def __init__(self, id: chr, capacity: int = 10, hourly_rate: float = 2.50, parked_cars: dict = {}):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.logger = CarParkingLogger(id)

    # receives the license_plate as str, the check_in/time as datetime object that the car is parked.
    def check_in(self, license_plate: str, check_in=None):
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
            # print that the car is already parked
            print(f"{license_plate} is already checked in")
            return False

        # add the car to the parked_cars dict
        car = ParkedCar(license_plate, check_in.replace(microsecond=0))
        self.parked_cars[license_plate] = car
        self.logger.add_check_in(self.id, license_plate, "check-in")

        # print that the car is parked
        print(f"License registered - {license_plate} checked in at {check_in}")

        return True

    # receives the license_plate as str and returns the owed parking fee total
    def check_out(self, license_plate: str):
        # check if the car is parked
        if license_plate not in self.parked_cars:
            # print that the car is not parked
            print(f"{license_plate} is not checked in")
            return False

        # get the parking fee
        fee = self.get_parking_fee(license_plate)

        # print the fee
        # print(f"{license_plate} parking fee: {fee} EUR")
        print(fee)
        print(f"Parking fee: {fee:.2f} EUR")
        self.logger.add_check_out(self.id, license_plate, "check-out", fee)

        # remove the car from the parked_cars dict
        del self.parked_cars[license_plate]

        return fee

    # receives the license_plate as str and calculates/returns the parking fee
    def get_parking_fee(self, license_plate: str):
        # hourly_rate * whole parking hours rounded up, with max of 24 hours
        if license_plate not in self.parked_cars:
            return 0

        # get the check in time
        car = self.parked_cars[license_plate]
        check_in_time = car.check_in
        duration = datetime.now() - check_in_time

        # get the hours parked
        hours_parked = math.ceil(duration.total_seconds() / 3600)
        # hours_parked = math.ceil(duration.total_seconds())
        hours_parked = min(hours_parked, 24)

        # return the fee - this should max out at $60
        return hours_parked * self.hourly_rate


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [I] Check-in car by license plate
# [O] Check-out car by license plate
# [Q] Quit program
def main():
    # capacity: int, hourly_rate: float, parked_cars: dict
    cpm = CarParkingMachine("North", 10, 2.50, {})

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
