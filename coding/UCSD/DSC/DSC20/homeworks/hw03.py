"""
DSC 20 Homework 03
Name: Jack Kai Lim
PID: A16919063
"""


### Question 1
def sort_by_index_with_for_loop(index, array):
    """
    Sort the array with the given index and return a list of
    (<element>, <original index>, <new index>) tuples.

    Parameters:
        index: List of length n that contains interger 0 to n-1.
        array: List of length n.
    Returns:
        A list of length n containing
        (<element>, <original index>, <new index>) tuples or an empty list
        if n is 0.

    >>> sort_by_index_with_for_loop([ 0, 4, 2, 3, 1], ["zero", "four", "two",\
"three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), ('three', 3, 3), \
('four', 1, 4)]
    """
    lst = []
    assert isinstance(index, list), 'Index is not a list'
    assert isinstance(array, list), 'Array is not a list'
    assert len(index) == len(array), 'Index and array length are not equal'
    for i in range(len(index)):
        lst.append((array[index[i]], index[i], i))

    return lst


def sort_by_index(index, array):
    """
    Sort the array with the given index and return a list of
    (<element>, <original index>, <new index>) tuples. Throw an assertion
    error (thrown by failed asserts automatically) if the arguments passed
    are invalid.

    >>> sort_by_index([ 0, 4, 2, 3, 1], \
["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), ('three', 3, 3), \
('four', 1, 4)]

    >>> sort_by_index([ 0.0, 4.0, 2.0, 3.0, 1.0], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> sort_by_index([ 0, 4, 2, 3, 0], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> sort_by_index([ 0, 4, 2, 3], ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> sort_by_index(2, ['three', 'four'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> sort_by_index([2, 1, 3, 0], 'four')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> sort_by_index([0, 2, 3, 1], [2, 'four', True, ['list', 'list']])
    [(2, 0, 0), (True, 2, 1), (['list', 'list'], 3, 2), ('four', 1, 3)]
    """

    assert isinstance(index, list)
    assert all(isinstance(x, int) for x in index)
    assert isinstance(array, list)
    assert len(index) == len(array)
    assert sum(index) == sum([x for x in range(len(index))])

    return [(array[index[i]], index[i], i) for i in range(len(index))]


### Question 2
def intersection(str1, str2):
    """
    Finds the intersection of str1 and str2 where an intersection is
    determined by str1[i] == str[i].

    >>> intersection("bbbaabbb", "dddaaddd")
    'aa'
    >>> intersection("bbbaabbb", "dddaa")
    'aa'
    >>> intersection("bbbaabbb", "ddd")
    ''
    >>> intersection("bbbbbbbbb", "ababababa")
    'bbbb'
    >>> intersection("bbbaabbb", 1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> intersection('', '')
    ''
    >>> intersection('bbaabb', 'ddAAdd')
    ''
    >>> intersection(',,,:::...', ',kk:jk.ll')
    ',:.'
    """
    assert isinstance(str1, str)
    assert isinstance(str2, str)

    return ''.join([str1[i] for i in range(len(str1 if len(str1) < len(str2)\
                                else str2)) if str1[i] == str2[i]])


### Question 3
def decode(to_decode):
    """
    Moves all the uppercase character to the beginning of the
    string and case the lowercase characters to uppercase.

    Parameters:
       to_decode: A string that is not all lowercase
    Returns:
       A decoded string.

    >>> decode(" neHAw yePParY")
    'HAPPY NEW YEAR'
    >>> decode(" Gof ERriALTvia")
    'GERALT OF RIVIA'
    >>> decode("ALL UPPERCASE")
    'ALLUPPERCASE '
    >>> decode("all lowercase")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> decode('here is symBols, :"}{|')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> decode(123)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> decode('What ' + 'H appens')
    'WHHAT  APPENS'
    >>> decode('   ')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(to_decode, str)
    assert any([x.isupper() for x in to_decode])
    assert all(x.isalpha() or x.isspace() for x in to_decode)

    return ''.join([x for x in to_decode if x.isupper()] + [x for x in \
                to_decode if x.islower() or x == ' ']).upper()


# Question 4
def find_closest_stores(friends, stores):
    """
    ##############################################################
    # First I iterate through the friends dictionary, then for each
    iteration in the friends dictionary. I iterate iterate through the
    stores dictionary, which I sorted into ascending order of the store
    name. Then I find the absolute distance between the 2 places, and find
    the min. Which I then put into a new dictionary.  #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> friends1 = {'rob': 10, 'bob': 12}
    >>> stores1 = {'walmart': 11, 'costco': 12}
    >>> find_closest_stores(friends1, stores1)
    {'rob': 'walmart', 'bob': 'costco'}

    >>> friends2 = {'bob': 12}
    >>> stores2 = {'target': 12, 'costco': 12}
    >>> find_closest_stores(friends2, stores2)
    {'bob': 'costco'}
    >>> friends3 = {'bob': 12, 'rob': 10, 'bobby': 3}
    >>> stores3 = {'target': 12, 'costco': 12, 'ralphs': 2}
    >>> find_closest_stores(friends3, stores3)
    {'bob': 'costco', 'rob': 'costco', 'bobby': 'ralphs'}
    >>> friends4 = {'bob': 12, 'bob': 12}
    >>> stores4 = {'target': 13, 'target': 13}
    >>> find_closest_stores(friends4, stores4)
    {'bob': 'target'}
    >>> friends5 = {'Jack': 1, 'kai': 2, 'mei': 3, 'jason': 6}
    >>> stores5 = {'target': 12, 'costco': 12, 'ralphs': 2, 'whole foods':10}
    >>> find_closest_stores(friends5, stores5)
    {'Jack': 'ralphs', 'kai': 'ralphs', 'mei': 'ralphs', 'jason': 'ralphs'}
    """
    return {friend: min([(abs(dist1 - dist2), store) for store, dist2 \
            in sorted(stores.items())])[1] for friend, dist1 in \
            friends.items()}


# Question 5
def average_housing(house_prices):
    """
    Calculate the lowest average price of houses in given areas while also
    ignoring the null value (-9999).

    Parameters:
        house_prices: A dictionary containing locations and their list
        of house prices.
    Returns:
        The house location with the lowest average price when ignoring null
        values.

    >>> average_housing({'LA': [782900, 1368800, -9999, -9999], \
                        'SD': [746600, 697100, 989900, 785000], \
                        'BNY': 675000})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> average_housing({92122: [746600, 697100, 989900, 785000]})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> average_housing({'LA': [782900, 1368800, 599000, 750000], \
                        'SD': [746600, 697100, 989900, 785000], \
                        'BNY': [675000, 239000, 789000, 1049000]})
    'BNY'
    >>> average_housing({'LA': [782900, 1368800, -9999, -9999], \
                        'SD': [746600, 697100, 989900, 785000], \
                        'BNY': [675000, -9999, 789000, 1049000]})
    'SD'
    >>> average_housing({'Acorn Blvd': [0, 1, 2], \
                        'Pine Ave': [4, 3, -9999], \
                        'Maple Lane': [3, -9999, 3, 3]})
    'Acorn Blvd'
    >>> average_housing({'LA': ['a', 12222, 3333]})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> average_housing({'LA': [0, -999, 100], \
                        'SD': [746600, 697100, 989900, 785000], \
                        'BNY': [675000, -9999, 789000, 1049000]})
    'LA'
    >>> average_housing({'UCSD': 2345})
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(house_prices, dict)
    assert all(isinstance(x, str) for x in house_prices.keys())
    assert all(isinstance(x, list) for x in house_prices.values())
    assert all(all([isinstance(x, int) or isinstance(x, float) for x in a]) \
               for a in house_prices.values())
    return min([(sum([price for price in prices if price >= 0]) / \
                 len([price for price in prices if price >= 0]), \
                 location) for location, prices in \
                house_prices.items()])[1]


# Question 6
def create_id(names, commands):
    """
    ##############################################################
    # Create a lambda function for each of the functions. Then I iterate
    through the commands needed to be applied in the order listed. Then excute
    the function on all the names in the list of names and return the list of
    names after running through all the #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> create_id(["TomNook", "Isabelle"], [('upper', 2)])
    ['TOmNoOk', 'ISaBeLlE']
    >>> create_id(["TomNook", "Isabelle"], [('last', 5), ('remove', 0)])
    ['belle']
    >>> create_id(["TomNook", "Isabelle"], [('first', 4), \
('insert', 2, 'Mabel'), ('length', 4)])
    ['TomN', 'Isab', 'Ma5bel']
    >>> create_id(["TomNook", "Isabelle"], [('insert', 2, 'bob'),\
    ('remove', 1), ('upper', 3), ('first', 6), ('last', 3), ('length', 1)])
    ['N3Oo', 'b3Ob']
    >>> create_id(['Charles'], [('first', 10)])
    ['Charles']
    >>> create_id(['Charles313'], [('length', 2)])
    ['Charl10es313']
    >>> create_id(['a b c d e f g h i j k l m n o p'], [('upper', 3)])
    jb
    >>> create_id(['we da best', 'Tommy'], [('upper', 3), ('remove', 0)])
    """
    string_pos = 2
    c
    first_func = lambda s, n: s[0:n]
    last_func = lambda s, n: s[len(s) - n: len(s)]
    insert_func = lambda l, index, name: l.insert(index, name)
    remove_func = lambda l, index: [x for x in l if x != l[index]]
    length_func = lambda s: s[0:len(s)//2] + str(len(s)) + s[len(s)//2:len(s)]
    func_dict = {'upper': upper_func, 'first': first_func, 'last': last_func,
                 'insert': insert_func, 'remove': remove_func,\
                 'length':length_func}

    for command in commands:
        if command[0] == 'upper':
            for i, name in enumerate(names):
                names[i] = func_dict[command[0]](name, command[1])
        elif command[0] == 'first':
            for i, name in enumerate(names):
                names[i] = func_dict[command[0]](name, command[1])
        elif command[0] == 'last':
            for i, name in enumerate(names):
                names[i] = func_dict[command[0]](name, command[1])
        elif command[0] == 'insert':
            func_dict[command[0]](names, command[1], command[string_pos])
        elif command[0] == 'remove':
            names = func_dict[command[0]](names, command[1])
        elif command[0] == 'length':
            for i, name in enumerate(names):
                if command[1] < len(name):
                    names[i] = func_dict[command[0]](name)

    return names
