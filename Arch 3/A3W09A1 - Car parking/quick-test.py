import carparking as cp
from datetime import datetime, timedelta

cpm = cp.CarParkingMachine(capacity=2, hourly_rate=4.0)
cpm.check_in("BB-494-H")
cpm.check_in("HH-494-B", datetime.now() - timedelta(hours=2))
print(cpm.get_parking_fee("HH-494-B"))

# import carparking as cp
# from datetime import datetime, timedelta
#
# cpm = cp.CarParkingMachine(capacity=2, hourly_rate=4.0)
# cpm.check_in("BB-494-H")
# cpm.check_in("HH-494-B", datetime.now() - timedelta(hours=2))
#
# print(cpm.capacity)
# print(cpm.check_in("TM-123-F"))

# import carparking as cp
# from datetime import datetime, timedelta
#
# cpm = cp.CarParkingMachine(capacity=2, hourly_rate=4.0)
# cpm.check_in("BB-494-H")
# cpm.check_in("HH-494-B", datetime.now() - timedelta(hours=2))
#
# print(cpm.hourly_rate)
# print(cpm.check_out("BB-494-H"))

# import carparking as cp
#
# cpm = cp.CarParkingMachine(capacity=2, hourly_rate=4.0)
# cpm.check_in("BB-494-H")
# cpm.check_in("HH-494-B")
#
# print(cpm.parked_cars)