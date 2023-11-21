from carparking import *
import os
from datetime import datetime, timedelta

cpm_list_template = ["A", "B", "C", "D"]


def test_check_in_capacity_normal():
    cpm = CarParkingMachine("A", capacity=1, hourly_rate=5.0, parked_cars=None)
    assert cpm.check_in("AAA") is True


def test_check_in_capacity_reached():
    cpm = CarParkingMachine("B", capacity=0)
    assert cpm.check_in("BBB") is False


def test_parking_fees():
    cpm = CarParkingMachine("C", hourly_rate=2.50)

    check_in = datetime.now() - timedelta(hours=2, minutes=10)
    cpm.check_in("X", check_in)

    duration = datetime.now() - check_in
    hours = round(duration.total_seconds() / 3600, 1)
    fee = round(hours * cpm.hourly_rate, 1)

    assert fee == 5.5

    check_in = datetime.now() - timedelta(hours=24)
    cpm.check_in("Y", check_in)

    duration = datetime.now() - check_in
    hours = round(duration.total_seconds() / 3600, 1)
    fee = round(hours * cpm.hourly_rate, 1)

    assert round(fee, 5) == 60.0


def test_check_out():
    cpm = CarParkingMachine("D")

    cpm.check_in("AAA")
    assert "AAA" in cpm.parked_cars

    cpm.check_out("AAA")
    assert "AAA" not in cpm.parked_cars


def teardown_module():
    print("Deleting files for startup/shutdown...")
    print(cpm_list_template)
    for cpm_id in cpm_list_template:
        filename = f"{cpm_id}.json"
        if os.path.exists(filename):
            print(f"Removing {filename}...")
            os.remove(filename)


if __name__ == "__main__":
    teardown_module()
    test_check_in_capacity_normal()
    test_check_in_capacity_reached()
    test_parking_fees()
    test_check_out()
    teardown_module()
