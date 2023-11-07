from datetime import datetime


# ParkedCar class to store information of parked cars.


class ParkedCar:
    # Day car parking machine. Max parking fee is 24 hours (hourly_rate * 24).
    def __init__(self, license_place: str, check_in: datetime):
        self.license_place = license_place
        self.check_in = check_in


# Attributes / Fields:

class CarParkingMachine:
    def __init__(self, capacity: int, hourly_rate: float, parked_cars: dict):
        self.capacity = capacity or 10
        self.hourly_rate = hourly_rate or 2.50
        self.parked_cars = parked_cars

    # receives the license_plate as str, the time as datetime object that the car is parked.
    def check_in(self, license_plate: str, time: datetime):
        self.parked_cars += 1
        print(self.parked_cars)
        print(self.time)
        return license_plate

    # receives the license_plate as str and returns the owed parking fee total
    def check_out(self, licese_plate: str):
        print("")

    # receives the license_plate as str and calculates/returns the parking fee
    def get_parking_fee(self, license_plate: str):
        # hourly_rate * whole parking hours rounded up, with max of 24 hours
        print("")


def main():
    shouldQuit = None
    # capacity: int, hourly_rate: float, parked_cars: dict
    cpm = CarParkingMachine(10, 2.50, {})
    cpm.check_in(license_plate="AA-123-B", time=datetime.now())

#     while not shouldQuit:
#         print('''
# [I] Check-in car by license plate
# [O] Check-out car by license plate
# [Q] Quit program
#         ''')
#         i = input("Input a command: ").upper()
#         if i == "I":
#             print("[I] Check-in car by license plate")
#         if i == "Q":
#             shouldQuit = True
#     exit(1)


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [I] Check-in car by license plate
# [O] Check-out car by license plate
# [Q] Quit program


if __name__ == "__main__":
    main()
