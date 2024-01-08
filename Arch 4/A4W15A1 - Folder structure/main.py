'''
In a program a function is implemented to traverse the folders and files.
It returns the result as a list. A list indicates a folder and a string item is a file.

For example: ['file_1',[]] is a folder that contains a file and an empty subfolder; ['file_1','file_2',['file_1']] is a folder containing two files and a subfolder with a file.
Your task is to implement a Python function that:

- Given such a list as the root folder prints the contents. Indentation of the folder will be > and for a file will be -.
- Given such a list as the root folder prints the number of files.
'''


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


if __name__ == "__main__":
    test_cases = [
        ['file_1', []],
        ['file_1', 'file_2', ['file_1']],
        ['file_1', 'file_2', ['file_3', 'file_4', 'file_5'], ['file_6', ['file_7', 'file_8'], ['file_9'], 'file_9', ['file_10']], []],
        ['file_1', ['file_3', ['file_2', ['file_10', ['file_9', 'file_8']]]], []],
        [[], [[], [[]]]]
    ]

    for case in test_cases:
        rec_print_folders(0, '', case)
        print('Number of files in case: ', case, ' is ', rec_count_files(case))