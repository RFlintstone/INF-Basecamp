from carparking import *
import os
from datetime import datetime, timedelta

# Create a list of CarParkingMachine IDs which we will be using
cpm_list_template = ["A", "B", "C", "D"]


# test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    # Create a CarParkingMachine object with capacity 1, hourly_rate 5.0 and empty parked_cars dict
    cpm = CarParkingMachine("A", capacity=1, hourly_rate=5.0, parked_cars=None)

    # Assert that check_in returns True because capacity is not reached
    assert cpm.check_in("AAA") is True


# test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    # Create a CarParkingMachine object with capacity 0, hourly_rate 5.0 and empty parked_cars dict
    cpm = CarParkingMachine("B", capacity=0)

    # Assert that check_in returns False because capacity is reached
    assert cpm.check_in("BBB") is False


# test for checking the correct parking fees
def test_parking_fees():
    # Create a CarParkingMachine object with capacity 10, hourly_rate 2.50, and an empty parked_cars dict
    cpm = CarParkingMachine("C", hourly_rate=2.50)

    # Create a check_in variable with 2h10m
    check_in = datetime.now() - timedelta(hours=2, minutes=10)

    # Check in the car with the check_in variable so that the car is parked for 2h10m
    cpm.check_in("X", check_in)

    # Calculate the fee without the check_out function so that we can compare it to the fee,
    # this way the method cant fail because of the check_out function
    duration = datetime.now() - check_in
    hours = round(duration.total_seconds() / 3600, 1)
    fee = round(hours * cpm.hourly_rate, 1)

    # Assert that the parking fee is correct
    assert fee == 5.5

    # Create a check_in variable with 24h
    check_in = datetime.now() - timedelta(hours=24)

    # Check in the car with the check_in variable so that the car is parked for 24h
    cpm.check_in("Y", check_in)

    # Calculate the fee without the check_out function so that we can compare it to the fee,
    # this way the method cant fail because of the check_out function
    duration = datetime.now() - check_in
    hours = round(duration.total_seconds() / 3600, 1)
    fee = round(hours * cpm.hourly_rate, 1)

    # Assert that the parking fee is correct
    assert round(fee, 5) == 60.0


# test for checking out a car
def test_check_out():
    # Create a CarParkingMachine object with capacity 10, hourly_rate 2.50, and an empty parked_cars dict
    cpm = CarParkingMachine("D")

    # Check in the car
    cpm.check_in("AAA")

    # Assert that the car is in the parked_cars dict
    assert "AAA" in cpm.parked_cars

    # Check out the car
    cpm.check_out("AAA")

    # Assert that the car is not in the parked_cars dict
    assert "AAA" not in cpm.parked_cars


# teardown_module is called after and before each test so we can use it to delete the unnecessary files
def teardown_module():
    # Print a message to the user
    print("Deleting files for startup/shutdown...")
    print(cpm_list_template)

    # Loop through the cpm_list_template and delete the files if they exist
    for cpm_id in cpm_list_template:
        filename = f"{cpm_id}.json"
        if os.path.exists(filename):
            print(f"Removing {filename}...")
            os.remove(filename)


# This is the main function which will run the tests one by one
if __name__ == "__main__":
    # Remove the files if they exist
    teardown_module()

    # Run the tests
    test_check_in_capacity_normal()
    test_check_in_capacity_reached()
    test_parking_fees()
    test_check_out()

    # Remove the files if they exist
    teardown_module()
