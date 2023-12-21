# Arch 3

## Assignment: A3W09A1 - Car parking

### Creation Date: 07-11-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
With the car parking assessment I created a 'quick-test.py' file so I could easily check if the code what was being run by codegrade was passing in the IDE. If it was then I pretty much knew Codegrade would accept it as well. (Although there were instances where the behaviour was different)

## Code Snippet
```python
# This is an example of 'quick-test.py' which would verify is Codegrade would mark it as a success
import carparking as cp
from datetime import datetime, timedelta

cpm = cp.CarParkingMachine(capacity=2, hourly_rate=4.0)
cpm.check_in("BB-494-H")
cpm.check_in("HH-494-B", datetime.now() - timedelta(hours=2))
print(cpm.get_parking_fee("HH-494-B"))
```
