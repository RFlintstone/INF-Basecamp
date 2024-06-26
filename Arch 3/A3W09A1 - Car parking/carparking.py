import math
from datetime import datetime


# ParkedCar class to store information of parked cars.
class ParkedCar:
    # Day car parking machine. Max parking fee is 24 hours (hourly_rate * 24).
    def __init__(self, license_place: str, check_in: datetime):
        self.license_place = license_place  # license plate of the car
        self.check_in = check_in  # time the car is parked


# Attributes / Fields:

class CarParkingMachine:
    def __init__(self, capacity: int = 10, hourly_rate: float = 2.50, parked_cars: dict = {}):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

    # receives the license_plate as str, the time as datetime object that the car is parked.
    def check_in(self, license_plate: str, time=None):
        # check if the time is None and set it to datetime.now() if it is
        if time is None:
            time = datetime.now()

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
            return

        # add the car to the parked_cars dict
        car = ParkedCar(license_plate, time)
        self.parked_cars[license_plate] = car

        # print that the car is parked
        print(f"License registered - {license_plate} checked in at {time}")

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

        # remove the car from the parked_cars dict
        del self.parked_cars[license_plate]

        return True

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
    cpm = CarParkingMachine(10, 2.50, {})

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
            cpm.check_in(license_plate=license_plate, time=datetime.now())

        # check if the user wants to check out
        elif choice == "O":
            license_plate = input("Enter license plate: ") if not DEBUG_MODE else "AA-123-B"
            print(f"Checking out {license_plate}...")
            cpm.check_out(license_plate=license_plate)

        # check if the user wants to quit the program
        elif choice == "Q":
            should_quit = True

    # When the user quits the program (exit loop), print a goodbye message
    print("Exiting program...") if DEBUG_MODE else print()


if __name__ == "__main__":
    main()
