"""
DSC 20 Homework 09
Name: Jack  Kai Lim
PID:  A16919063
"""


# Question 1

def maze(coord, map):
    """
    Given `coord` as a tuple and `map` as list of strings, 
    return 'treasure!' if treasure can be reached by following the signs
    return 'sad' otherwise
​
    There is no cycle
​
    >>> map = [
    ... "..............",
    ... ".RRRD..RRRRD..",
    ... "...DL..U...D..",
    ... "...D...U.D.D..",
    ... "...RRRRU.D.*..",
    ... ".............."]
    >>> maze((1,1), map)
    'treasure!'
    >>> maze((0,0), map)
    'sad'
    >>> maze((3,9), map)
    'sad'
    >>> maze((4,11), map)
    'treasure!'

    # Add more tests
    >>> map2 = [
    ... "................",
    ... ".RRRRRRRRRD.....",
    ... ".LDL.DULRR*.....",
    ... "................"]
    >>> maze((1, 1), map2)
    'treasure!'
    >>> maze((2, 1), map2)
    'sad'
    >>> maze((2, 10), map2)
    'treasure!'
    """

    if map[coord[0]][coord[1]] == '.':
        return 'sad'
    elif map[coord[0]][coord[1]] == '*':
        return 'treasure!'
    elif map[coord[0]][coord[1]] == 'R':
        return maze((coord[0], coord[1] + 1), map)
    elif map[coord[0]][coord[1]] == 'L':
        return maze((coord[0], coord[1] - 1), map)
    elif map[coord[0]][coord[1]] == 'U':
        return maze((coord[0] - 1, coord[1]), map)
    elif map[coord[0]][coord[1]] == 'D':
        return maze((coord[0] + 1, coord[1]), map)


# Question 2
def binary_search(target, arr, left, right):
    """
    
    >>> arr = [2, 3, 4, 10, 40]
    >>> target = 3
    >>> binary_search(target, arr, 0, 5)
    [[2, 3, 4, 10, 40], [2, 3]]

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
    >>> target = 20
    >>> binary_search(target, arr, 0, 12)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30], [8, 9, 10, 20, 30], [20, 30], [20]]

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
    >>> target = 20
    >>> binary_search(target, arr, 0, 10)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [7, 8, 9, 10], [10], []]

    >>> arr = [2, 3, 4, 10, 40]
    >>> target = 30
    >>> binary_search(target, arr, 0, 5)
    [[2, 3, 4, 10, 40], [10, 40], [10], []]

    # Add more tests
    >>> arr = [1, 2, 3, 4, 5, 7, 8, 9, 9]
    >>> target = 9
    >>> binary_search(target, arr, 0, 9)
    [[1, 2, 3, 4, 5, 7, 8, 9, 9], [7, 8, 9, 9]]
    >>> binary_search(1, [0], 0, 1)
    [[0], []]
    >>> binary_search(2, [2, 22, 22, 222], 0, 1)
    [[2]]

    """

    # Your code is here
    mid = (left + right) // 2
    if len(arr[left:right]) == 0:
        return [[]]
    elif arr[mid] == target:
        return [arr[left:right]]
    elif arr[mid] < target:
        return [arr[left:right]] + binary_search(target, arr, mid + 1, right)
    else:
        return [arr[left:right]] + binary_search(target, arr, left, mid)


# 3 No tests are needed. Fix the code.

# Question 3.1
def fix_1(lst1, lst2):
    """
    Divide all of the elements in `lst1` by each element in `lst2`
    and return the values in a list.

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div)  # add try-except block
            except:
                None
    return out


# Question 3.2
def fix_2(*filepaths):
    """
    Open all of the files in `filepaths` and PRINT a string for each file
    that indicates if this file can be opened or not.

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found

    >>> fix_2('docs.txt')
    docs.txt not found
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r")  # add try-except block
            print(filepath + ' opened')
            cur_file.close()
        except:
            print(filepath + ' not found')



# Question 3.3
def fix_3(lst):
    """
    For each element in `lst`, add it with its following element
    in the list. Returns all of the summed values in a list.

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []

    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]

    >>> fix_3([])
    []
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1])  # add try-except block
        except TypeError:
            print(TypeError)
        except IndexError:
            print(IndexError)
    return sum_of_pairs


# Question 4
def check_inputs(input1, input2):
    """
    # Using and if/else statement to verify each input based on the
    reqwuirements. Then if it does not meet them, then I raise a typeeror. #

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'

    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1

    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type

    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric

    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    >>> check_inputs([1, 2, 3], 2.0)
    'Input validated'
    >>> check_inputs([True, 1, 3], 2)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 0 is not numeric
    >>> check_inputs([], [])
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    """

    # Your code is here
    if not isinstance(input1, list):
        raise TypeError('input1 is not the correct type')
    elif not all(isinstance(x, (int, float)) for x in input1) or \
        any(isinstance(x, bool) for x in input1):
        for i, x in enumerate(input1):
            if not isinstance(x, (int, float)) or isinstance(x, bool):
                raise TypeError('The element at index {} is not '
                                'numeric'.format(i))
            else:
                continue
    elif not isinstance(input2, (int, float)):
        raise TypeError('input2 is not the correct type')
    elif input2 not in input1:
        raise TypeError('input2 not in input1')
    else:
        return 'Input validated'


# Question 5
def load_file(filename):
    """
    # First I check if the filename given is a string or not, then next I
    check to see if the file exist.Then next I check to see whether there
    are any elements/words in the list. If there are then I return the
    number of words in the list. #

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string

    >>> load_file('files/ten_words.txt')
    10

    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty

    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    >>> load_file(True)
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string
    >>> load_file('files/1 word.txt')
    1
    >>> load_file([1, 2, 3, 4])
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string
    """

    # Your code is here
    if not isinstance(filename, str):
        raise TypeError('filename is not a string')
    else:
        try:
            open(filename, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(filename + ' does not exist')
        else:
            with open(filename, 'r') as file:
                total = 0
                if file.read(1):
                    for line in file:
                        line_lst = line.strip('\n').split(' ')
                        total += len(line_lst)
                else:
                    raise ValueError('File is empty')

    return total