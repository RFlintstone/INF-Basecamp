import os
import carparking as cp

if os.path.exists("North.json"):
    os.remove("North.json")

if os.path.exists("carparklog.txt"):
    os.remove("carparklog.txt")

cpm = cp.CarParkingMachine(id="North", capacity=2, hourly_rate=4.0)
print(cpm.parked_cars)

cpm.check_in("BB-494-H")
cpm.check_in("HH-494-B")

print(cpm.parked_cars)

# Local:
# Logged with JSON: Check-ins: 3, Duplicate check-ins: 1, Check-outs: 0
# Logged in .txt: 2 Logged Check-ins, 0 duplicate check-in, 0 Check-outs
# 2 Car objects are stored in the list

'''
[]
21-11-2023 16:22:24;cpm_name=North;license_plate=BB-494-H;action=check-in

License registered - BB-494-H checked in at 2023-11-21 16:22:24.981192
21-11-2023 16:22:24;cpm_name=North;license_plate=BB-494-H;action=check-in
21-11-2023 16:22:24;cpm_name=North;license_plate=HH-494-B;action=check-in

License registered - HH-494-B checked in at 2023-11-21 16:22:24.987192
[<carparking.ParkedCar object at 0x000002246B9855D0>, <carparking.ParkedCar object at 0x000002246BDF5090>]
'''

# Codegrade:
# Logged with JSON: Check-ins: 3, Duplicate check-ins: 1, Check-outs: 0
# Logged in .txt: 2 Logged Check-ins, 0 duplicate check-in, 0 Check-outs
# 2 Car objects are stored in the list

'''
21-11-2023 15:24:19;cpm_name=North;license_plate=BB-494-H;action=check-in

License registered - BB-494-H checked in at 2023-11-21 15:24:19.362613
21-11-2023 15:24:19;cpm_name=North;license_plate=BB-494-H;action=check-in
21-11-2023 15:24:19;cpm_name=North;license_plate=HH-494-B;action=check-in

License registered - HH-494-B checked in at 2023-11-21 15:24:19.362885
[<carparking.ParkedCar object at 0x7f6db626a3d0>, <carparking.ParkedCar object at 0x7f6db6333110>]
'''

# Codegrade's expected pattern is:
'''
\{'BB-494-H': \<carparking.ParkedCar object .*?\>, 'HH-494-B': \<carparking.ParkedCar object .*?\>\}
'''

# So why is it not working?
