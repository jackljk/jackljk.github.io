"""
DSC20 WI22 LAB06
Name: Jack Kai Lim
PID:  A16919063
"""


# Question1
def complexity_tf():
    """
    Write your answers to time complexity True/False questions in this
        function.

    >>> answers = complexity_tf()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, bool) for ans in answers])
    True
    """
    # Your code here
    return [True, False, False, False, True, False, True, True, False, False]


# Question2
def files_target_count(target, *args):
    """
    Write a function that takes in a target character and files.
        Count the # of times the target character appears in all of the files.
        ** Not case sensitive.

    >>> files_target_count('e', 'files/file1.txt', 'files/file2.txt')
    5
    >>> files_target_count('\\n', 'files/file1.txt', 'files/file2.txt')
    10
    >>> files_target_count('E', 'files/file1.txt', 'files/file2.txt')
    5
    >>> files_target_count('', 'files/file1.txt', 'files/file2.txt')
    0
    >>> files_target_count('e', 'files/file1.txt', 'files/file2.txt',\
     'files/file3.txt', 'files/file4.txt')
    99
    >>> files_target_count('\\n', 'files/file2.txt', 'files/file4.txt',\
     'files/file3.txt')
    26
    """
    count = 0
    for filepath in args:
        with open(filepath, 'r') as file:
            for line in file.readlines():
                for cha in line:
                    if target.lower() == cha or target.upper() == cha:
                        count += 1
    return count


# Question3
def randomize(*args):
    """
    Write a function where, for each argument, if the type is a:
        - string:
            if the string is all uppercase, take the first half,
            if all lowercase, take the first and last letters,
            otherwise, do nothing
        - int:
            if even, add 2,
            if odd, square and add 3
        - float:
            if negative, convert to equivalent positive value,
            if non-negative, make int (cut off everything after the decimal)
        - bool:
            convert to corresponding int values
        The converted values should be put into a string,
        with the first argument's corresponding value at the end,
        and the last at the beginning.
        If an argument is not any of these types,
        then do not add it to the string.

    >>> randomize(1, 2.3, False, 'DSC20')
    'DS024'
    >>> randomize(True, 4, 'A', -9.8, [1,2,3], 'a', False)
    '0aa9.861'
    >>> randomize(False, True, 'DS', True, 'abc', -3.2, 5, {'a': 1}, -2, ' .')
    ' .0283.2ac1D10'
    >>> randomize()
    ''
    """
    string = ''
    for ele in args:
        if isinstance(ele, bool):
            if ele:
                string = '1' + string
            else:
                string = '0' + string
        elif isinstance(ele, str):
            if not ele.isalnum():
                string = ele + string
            elif ele.upper() == ele:
                if len(ele) != 1:
                    ele = ele[0:int(len(ele) / 2)]
                    string = ele + string
            elif ele.lower() == ele:
                ele = ele[0] + ele[-1]
                if len(ele) == 1:
                    string = ele + ele + string
                else:
                    string = ele + string
        elif isinstance(ele, int):
            if ele % 2 == 0:
                ele = ele + 2
                string = str(ele) + string
            else:
                ele = (ele ** 2) + 3
                string = str(ele) + string
        elif isinstance(ele, float):
            if ele <= 0:
                ele = ele * (-1)
                string = str(ele) + string
            else:
                ele = int(ele)
                string = str(ele) + string
    return string


# Question4
def most_improved_jump(*args, **kwargs):
    """
    Takes in equations and names of normal hill ski jumpers with their
    corresponding jump distances. Just for fun, you want to see how much an
    athlete can improve when their scores are just slightly tweaked. This
    function will apply each equation to each score for each athlete and
    returns the number of points improved for the highest average score
    for each athlete in a dictionary. Round to one decimal place.

    >>> most_improved_jump(lambda s: s * 1.25, lambda s: s + 15, \
lambda s: s**1.05, Bob=[30, 60, 40, 90, 80], Joe=[90, 80, 90], \
Billy=[54, 34, 29, 91, 98, 82])
    {'Bob': 15.0, 'Joe': 21.7, 'Billy': 16.2}

    >>> most_improved_jump(lambda s: s * 2, lambda s: s -2, \
Bob=[30, 60], Joe=[10])
    {'Bob': 45.0, 'Joe': 10.0}
    """
    d = {}
    for key, lst in kwargs.items():
        avg = 0
        ori_avg = sum(lst) / len(lst)
        for func in args:
            diff = sum(list(map(func, lst))) / len(lst) - ori_avg
            if avg < diff:
                avg = round(diff, 1)
        d[key] = avg

    return d


# Question5
def ingredient_checker(ing, **kwargs):
    """
    Takes in a popular grocery ingredient as a string and names of people
        who have recently been shopping with the items they bought stored in
        a list and returns a list of tuples revealing the name of the shopper
        and a boolean revealing whether or not this shopper bought the item -
        True if they bought it, False if not.

    >>> ingredient_checker('Eggs', John = ['Pepper', 'Onion', \
    'Flour', 'Salsa'], Rose = ['Chicken', 'Meat', 'Eggs'], \
    Hannah = ['Parmesan', 'Swiss Cheese', 'Bacon'])
    [('John', False), ('Rose', True), ('Hannah', False)]

    >>> ingredient_checker('Kiwi', Jerry = ['Pepper', 'Onion', \
    'Flour', 'Salsa'], Tommy = ['Chicken', 'Meat', 'Eggs'], \
    Mother = ['Parmesan', 'Swiss Cheese', 'Bacon'])
    [('Jerry', False), ('Tommy', False), ('Mother', False)]

    >>> ingredient_checker('Kiwi', Jerry = [], \
    Tommy = ['Chicken', 'Meat', 'Eggs'], \
    Mother = ['Parmesan', 'Swiss Cheese', 'Bacon'], \
    Brother = ['Swiss Cheese', 'Tomatoes'])
    [('Jerry', False), ('Tommy', False), ('Mother', False), ('Brother', False)]

    >>> ingredient_checker('Kiwi')
    []
    """
    return [(key, True) if ing in lst else (key, False) for key, lst in
            kwargs.items()]


# Question6
def check_consideration(*args, **kwargs):
    """

    Create a function which takes in:
        an arbitrary number of tuples in the form of
        (target average, allowed error),
        where the target average is the average number of yards a
        receiver needs to meet criteria
        and the allowed error specifies how many yards under that
        average the receiver can be

        The corresponding receiver names and a
        list of their receiving yard statistics
        their average over the games needs to be at least the target average

        Return a list of players who meet the criteria
        for pro-bowl consideration.


    >>> check_consideration((120, 17), (111, 8), (125, 25), Diggs =\
        [70, 130, 100], Hill = [141, 88, 98, 91], Juju = [132, 100, 99,\
        114])
    ['Hill', 'Juju']

    >>> check_consideration((145, 7), (170, 35), (165, 20), \
    Jefferson = [182, 100, 161], Adams = [117, 122, 98, 71], \
    Kupp = [111, 88, 64, 221])
    ['Jefferson']

    >>> check_consideration((90, 10), (80, 5), (99, 20), \
    Ohtani = [1], Kelce = [117, 122, 98, 71, 110, 77], \
    Miller = [90, 95, 99, 91], Johnson = [43, 100, 88, 101])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> check_consideration((10, 11),(90, 10), (80, 5), (99, 20), \
    Ohtani = [], Kelce = [117, 122, 98, 71, 110, 77], \
    Miller = [90, 95, 99, 91], Johnson = [43, 100, 88, 101])
    Traceback (most recent call last):
    ...
    AssertionError

    """
    assert len([t for t in args]) == len([v for v in kwargs.values()])
    assert all([True if len(lst) != 0 else False for lst in kwargs.values()])
    assert all([True if len(t) == 2 else False for t in args])
    l = []
    for i, tp in enumerate(args):
        range = (tp[0] - tp[1], tp[0] + tp[1])
        for j, (name, lst) in enumerate(kwargs.items()):
            if i == j:
                if range[0] <= sum(lst) / len(lst) <= range[1]:
                    l.append(name)

    return l
