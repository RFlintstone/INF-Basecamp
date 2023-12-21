## Assignment: A3W10A1 - Car parking logger

### Creation Date: 11-14-2023

### What did I learn?
I learned nothing with this assignment.

### How did I learn it?
Not applicable

### Why/how did I solve it?
With the car parking assessment I created a 'quick-test.py' file so I could easily check if the code what was being run by codegrade was passing in the IDE. If it was then I pretty much knew Codegrade would accept it as well. (Although there were instances where the behaviour was different)

## Code Snippet
```python
def write_to_log_file(self, new_line: str):
    # open the log file
    log_file = self.open_log_file()

    # use seek to start writing at the beginning of the file and write the new line
    log_file.seek(0)
    log_file.write(new_line)

    # truncate the file to the current position and close the file
    log_file.truncate()
    log_file.close()

    return True
```
