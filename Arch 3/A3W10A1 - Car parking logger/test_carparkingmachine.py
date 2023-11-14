from carparking import *
from datetime import datetime, timedelta

license_plate = "AA-123-B"


# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    # Create a CarParkingMachine object with capacity 10, hourly_rate 2.50 and empty parked_cars dict
    cpm1 = CarParkingMachine("North", 10, 2.50, {})
    # Assert that check_in returns True because capacity is not reached
    assert cpm1.check_in(license_plate) is True


# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    # Create a CarParkingMachine object with capacity 0, hourly_rate 2.50 and empty parked_cars dict
    cpm2 = CarParkingMachine("North", 0, 2.50, {})
    # Assert that check_in returns False because capacity is reached
    assert cpm2.check_in(license_plate, datetime.now()) is False


# Test for checking the correct parking fees
def test_parking_fee():
    # Create a CarParkingMachine object with capacity 10, hourly_rate 2.50, and an empty parked_cars dict
    cpm3 = CarParkingMachine("North", 10, 2.50, {})

    # Create two check_in_time variables, one with 2h10m and one with 24h
    check_in_time_1 = datetime.now() - timedelta(hours=2, minutes=10)
    check_in_time_2 = datetime.now() - timedelta(hours=24)

    # Check in the cars
    cpm3.check_in("c1", check_in_time_1)
    cpm3.check_in("c2", check_in_time_2)

    # Check out the cars and get the parking fees
    fee1 = cpm3.check_out("c1")
    fee2 = cpm3.check_out("c2")

    # Assert that parking time 2h10m, gives correct parking fee
    assert fee1 is True

    # Assert that parking time 24h, gives correct parking fee
    assert fee2 is True

    # Prepare two subtraction variables, one with 30h and one with 24h
    sub1 = datetime.now() - timedelta(hours=30)
    sub2 = datetime.now() - timedelta(hours=24)

    # Check in two cars with the subtraction variables
    cpm3.check_in("a", sub1)
    cpm3.check_in("b", sub2)

    # Get the parking fee for the two cars
    one = cpm3.get_parking_fee("a")
    two = cpm3.get_parking_fee("b")

    # Assert that parking time 30h == 24h max, gives correct parking fee
    assert one == two

    # now = datetime.now()
    # cpm_south = CarParkingMachine(id='CodeGradeTestSouth')
    # cpm_south.check_in(license_plate='AAA', check_in=now - timedelta(hours=2, minutes=10))


# Test for validating check-out behaviour
def test_check_out():
    cpm4 = CarParkingMachine(id="CodeGradeTestMid", hourly_rate=6)

    # Get current time
    now = datetime.now()

    # Subtract 1 hour
    check_in_time = now - timedelta(hours=1)

    # Check in
    cpm4.check_in(license_plate="DDD", check_in=check_in_time)

    # Assert DDD is in parked_cars
    assert "DDD" in cpm4.parked_cars

    # Check out DDD
    fee = cpm4.check_out("DDD")

    # Assert fee is correct
    assert fee == (cpm4.hourly_rate * 1)

    # Assert DDD is no longer in parked_cars
    assert "DDD" not in cpm4.parked_cars


if __name__ == "__main__":
    test_check_in_capacity_normal()
    test_check_in_capacity_reached()
    test_parking_fee()
    test_check_out()
