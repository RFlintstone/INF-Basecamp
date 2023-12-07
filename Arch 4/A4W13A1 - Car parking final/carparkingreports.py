import os
import csv
import json
from datetime import datetime, timedelta


def str_to_datetime(date_string, fmt):
    """
    Converts a string to a datetime object based on the specified format.

    :param date_string: A string representing a datetime value.
    :param fmt: The format string specifying the format of the datetime value.
    :return: The datetime object representing the converted string.

    """
    try:
        if isinstance(date_string, str):
            return datetime.strptime(date_string, fmt)
        return date_string
    except ValueError as error:
        print(f"Failed to convert string to datetime object: {error}")
        return None


def datetime_to_string(dt, format_string="%Y-%m-%d %H:%M:%S"):
    """Converts a datetime object or a datetime string to a formatted string.

    :param dt: A datetime object or a datetime string.
    :param format_string: The format string to use for conversion. Defaults to "%Y-%m-%d %H:%M:%S".
    :return: A formatted string representation of the datetime object or string.

    """
    if isinstance(dt, datetime):
        return dt.strftime(format_string)
    elif isinstance(dt, str):
        try:
            datetime_object = datetime.strptime(dt, format_string)
            return datetime_object.strftime(format_string)
        except ValueError:
            return "Invalid Datetime String"
    else:
        return "Invalid Datetime"


class CarParkingReports:
    def __init__(self, cpm_name=None, start_date=None, end_date=None):
        """
        Initializes a new instance of the CarParkingReports class.

        :param cpm_name: a string representing the name of the car parking meter (default is None)
        :param start_date: a datetime object representing the start date for the report (default is None)
        :param end_date: a datetime object representing the end date for the report (default is None)
        """
        self.cpm_name = cpm_name
        self.start_date = start_date
        self.end_date = end_date

    # North, 11-24-2023, 11-24-2023
    def get_license_plates(self):
        """
        This method retrieves license plates based on a given start date and end date. It reads data from a JSON file and checks if the check-in and check-out dates for each entry fall within the specified date range.

        :param self: An instance of the CarParkingReports class.
        :return: A list of license plates with corresponding check-in and check-out dates.
        """
        # Get the start and end dates
        start_date = self.start_date
        end_date = self.end_date

        # Initialize an empty list to store the license plates
        license_plates = []

        # Construct file name from cpm_name
        file = f"{self.cpm_name}_state.json"

        # Check if the file exists and is not empty
        if os.path.exists(file) and os.path.getsize(file) > 0:
            with open(file) as f:
                try:
                    # load json data from the file
                    data = json.load(f)

                    print("DATA:", data)

                    # Loop through the data
                    for entry in data:
                        # Extract check-in and check-out from each entry
                        for key, item in entry.items():
                            print(item)

                            # Convert the dates to datetime objects
                            if isinstance(start_date, str):
                                if start_date is not None:
                                    start_date = str_to_datetime(start_date, "%m-%d-%Y")
                            if isinstance(end_date, str):
                                if end_date is not None:
                                    end_date = str_to_datetime(end_date, "%m-%d-%Y") + timedelta(
                                        hours=23, minutes=59, seconds=59)

                            # Fetch check-in and check-out
                            check_in = item.get("check-in")
                            check_out = item.get("check-out")

                            # Convert these dates properly
                            if check_in:
                                check_in_date = str_to_datetime(check_in, "%m-%d-%Y %H:%M:%S")
                            else:
                                check_in_date = None
                            if check_out:
                                check_out_date = str_to_datetime(check_out, "%m-%d-%Y %H:%M:%S")
                            else:
                                check_out_date = None

                            print(check_in_date, "&", check_out_date)
                            print(start_date, "&", end_date)

                            print(check_in_date, "is", type(check_in_date))
                            print(check_out_date, "is", type(check_out_date))
                            print(start_date, "is", type(start_date))
                            print(end_date, "is", type(end_date))

                            # Validation of the dates and appending to the list
                            if check_in_date is not None:
                                time = check_in_date.timestamp()
                            else:
                                time = check_out_date.timestamp()

                            if int(start_date.timestamp()) <= int(time) <= int(
                                    end_date.timestamp()
                            ):
                                license_plates.append({
                                    "license_plate": item.get("license_plate"),
                                    "check-in": check_in_date,
                                    "check-out": check_out_date,
                                })

                except json.decoder.JSONDecodeError as ex:
                    # Print error message if json decode fails
                    print("Failed to decode JSON: ", ex)
        else:
            # Print message if the file does not exist or is empty
            print("File does not exist or is empty")

        # Return the list of license plates
        return license_plates

    # Do the same as with get_license_plates, but instead make it output:
    # car_parking_machine;total_parking_fee
    # cpm_north;2,050
    # cpm_south;180
    # The date must be read from carparklog.txt
    # 11-22-2023, 11-22-2023
    def get_parking_machine(self):
        """
        Returns a dictionary of parking machine fees calculated from the carparklog.txt file.

        :return: A dictionary where the keys are the names of the parking machines and the values are the total
        parking fees for each machine.
        """
        parking_machine_fees = {}

        # Open and read the carparklog.txt file
        with open('carparklog.txt', 'r') as f:
            lines = f.readlines()

        for line in lines:
            data = line.strip().split(';')

            date_time, machine_entry, license_plate, action = data
            machine_name = machine_entry.split('=')[1]

            # Initialize dict key, if it does not exist
            if machine_name not in parking_machine_fees:
                parking_machine_fees[machine_name] = 0

            # Just for illustration, an arbitrary parking fee
            if action == 'check-in':
                parking_fee = 10  # Arbitrary parking fee
                parking_machine_fees[machine_name] += parking_fee

        # Write the output to a CSV file
        with open(f'parkedcars_{self.cpm_name}_from_{self.start_date}_to_{self.end_date}.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["car_parking_machine", "total_parking_fee"])
            for machine, total_fee in parking_machine_fees.items():
                writer.writerow([machine, "{0:,.0f}".format(total_fee)])

    def generate_parked_cars_report(self):
        """
        This method generates a report of parked cars within a specified time range and saves it to a CSV file.

        :return: None
        """
        # Get the list of license plates
        lp = self.get_license_plates()
        print(lp)

        # datetime to string
        start_date = datetime_to_string(self.start_date, "%m-%d-%Y")
        end_date = datetime_to_string(self.end_date, "%m-%d-%Y")

        # Save the report to a csv file
        self.save_to_csv(lp, f"parkedcars_{self.cpm_name}_from_{start_date}_to_{end_date}.csv")

    def generate_cpm_report(self):
        """
        Generates a car parking machine report.

        :return: None
        """
        self.get_parking_machine()

    def save_to_csv(self, data, file_name):
        """
        Save data to a CSV file.

        :param data: A list of dictionaries representing the data to be saved.
        :param file_name: The name of the CSV file.
        :return: A string indicating the success or failure of the operation.

        Raises:
            ValueError: If 'data' is not a list of dictionaries or if 'file_name' is an empty string.
            FileNotFoundError: If the file specified by 'file_name' does not exist.
            PermissionError: If there is no write permission for the file specified by 'file_name'.
            Exception: If any other error occurs during the operation.
        """
        if not isinstance(data, list):
            raise ValueError("'data' must be a list of dictionaries")

        if not all(isinstance(i, dict) for i in data):
            raise ValueError("all items in 'data' must be dictionaries")

        if isinstance(file_name, str) and file_name.strip() == '':
            raise ValueError("'file_name' must be a non-empty string")

        try:
            with open(file_name, "w") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=";")
                writer.writeheader()
                writer.writerows(data)
            return "Data successfully written to csv file."
        except FileNotFoundError:
            return f"Unable to open file: {file_name}"
        except PermissionError:
            return f"No write permission for file: {file_name}"
        except Exception as e:
            return str(e)


# Defining the main function
def main():
    """
    Runs the main program loop for generating parking reports.

    :return: None
    """
    # Creating a reporter object from CarParkingReports
    # This will be used to generate our reports
    reporter = CarParkingReports()

    # This variable is used for controlling the main program loop
    should_quit = False

    # Main program loop
    while not should_quit:
        # Print a menu of options for the user
        print(
            "[P] Report all parked cars during a parking period for a specific parking machine\n"
            "[F] Report total collected parking fee during a parking period for all parking machines\n"
            "[Q] Quit program"
        )

        # Get an input from the user and convert it to uppercase
        choice = input("Select option: ").upper()

        # User has selected to generate a report on parked cars
        if choice == "P":
            # Request required parameters for this report from user
            cpm, start_date, end_date = input("Enter cpm, start, end: ").replace(" ", "").split(",")

            # Set the parameters for the reporter object
            reporter.cpm_name = cpm
            reporter.start_date = start_date
            reporter.end_date = end_date

            # Generate the parked cars report
            reporter.generate_parked_cars_report()

        # User has selected to generate a report on total fees
        elif choice == "F":
            # Request required parameters for this report from user
            start_date, end_date = input("Enter start, end: ").replace(" ", "").split(",")

            # Set the parameters for the reporter object
            reporter.start_date = start_date
            reporter.end_date = end_date

            # Generate the total fees report
            reporter.generate_cpm_report()

        # User has chosen to quit the program
        elif choice == "Q":
            # Set our controlling variable to True to exit the loop
            should_quit = True

    # Print a message after exiting the main loop
    print("Exiting program...")


if __name__ == "__main__":
    main()
