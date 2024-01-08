## Assignment: A4W15A1 - Folder structure

### Creation Date: 12-22-2023

### What did I learn?
I didn't really learn anything as this assessment was almost a copy and paste from the first name hasher assessment.  

### How did I learn it?
Not applicable

### Why/how did I solve it?
As Cigdem Okuyucu said this to me; I won't specify how I solved it or what my code is if I didn't
learn anything new in the assignment/problem.

## Code Snippet
```python
def rec_print_folders(n: int, pref: str, root: list) -> None:
    '''
    This function prints the contents of a given root folder with indentations.
    '''
    for i in root:
        if type(i) is list:
            rec_print_folders(n + 1, pref + '>', i)
        else:
            print(pref + '-' + i)


def rec_count_files(root: list) -> int:
    '''
    The functions counts number of files in a given folder (and all its sub-folders).
    :param root: A nested list: an element either is a file (name) or a list as a sub-folder.
    :return: The number of files in the given folder
    '''

    if len(root) == 0:
        return 0
    else:
        count = 0
        for i in root:
            if type(i) is list:
                count += rec_count_files(i)
            else:
                count += 1
        return count
```
