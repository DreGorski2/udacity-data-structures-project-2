# For this problem, the goal is to write code for finding all files under a directory
#  (and all directories beneath it) that end with ".c"

import os
from pprint import pprint

path = os.getcwd() + '/testdir 2'
suffix = ".c"


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if not isinstance(path, str):
        print(f"{path} is an invalid path ")
        return None

    elif not isinstance(suffix, str):
        print(f"{suffix} is an invalid suffix")
        return None


    path_list = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            if file_path.endswith(suffix):
                path_list.append(file_path)
        if os.path.isdir(file_path):
            # find_files(suffix, file_path)
            new_file = find_files(suffix, file_path)
            path_list.extend(new_file)
    return path_list


if __name__ == '__main__':
    path = os.getcwd() + '/testdir 2'
    suffix = ".c"
    lists = find_files(suffix, path)
    pprint(find_files(".c", path))  # solution to problem 2


# Test 1
pprint(find_files(".txt", path))  # blank list no .txt files
# Test 2
pprint(find_files(".h", path))  # list with 4 .h file paths
# Test 3
pprint(find_files(None, path))  # None invalid suffix
# Test 4
pprint(find_files(".c", None))  # None invalid path
# Test 5
pprint(find_files(None, None))  # none invalid path
# Test 6
pprint(find_files(12, path))  # none invalid suffix




















