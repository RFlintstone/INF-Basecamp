import os
import sys
import sqlite3
from time import sleep

import carparking as cp

cpm = cp.CarParkingMachine(id="North",capacity=2, hourly_rate=4.0)
cpm.check_in("BB-494-H")
cpm.check_out("BB-494-H")

con = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))

print("Connection established")
print(con.execute("SELECT * FROM parkings WHERE license_plate = 'BB-494-H' ORDER BY id DESC LIMIT 1;").fetchone())
