"""
DSC20 WI22 HW05
Name: Jack Kai Lim
PID:  A16919063
"""


# begin helper methods
def ceil(x):
    """
    Simulation to math.ceil
    No doctest needed
    """
    if int(x) != x:
        return int(x) + 1
    return int(x)


def log(x):
    """
    Simulation to math.log with base e
    No doctests needed
    """
    n = 1e10
    return n * ((x ** (1 / n)) - 1)


def cal_no_of_adults(lst):
    """
    Calculate the number of adult per child
    Doctest as part of question 4
    """
    a_per_c = 3
    return ceil(sum(lst) / a_per_c)


# end helper methods

# Question1
def db_calc(dynamic, inst_mult):
    """
    ##############################################################
    # First the function calculates the initial dB level, then return
    another function which takes the dist of the dB we are looking for. Then
     it calculates the dB at that distance and returns it.#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> snare_1 = db_calc('ff',  1.2)
    >>> snare_1(0)
    126
    >>> snare_1(10)
    80
    >>> snare_1(50)
    48
    >>> db_calc('loud', 1)(35)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> db_calc('pp', 1.200001)(50)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> db_calc(100, 0.2)(10)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> db_calc('pp', '1')(10)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> db_calc('pp', 0.9)('10')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> db_calc('ff', 1.2)(100)
    34
    >>> db_calc('ff', 1)(100000)
    0

    """
    assert isinstance(dynamic, str)
    assert isinstance(inst_mult, (int, float))

    dB_dict = {'pp': 30, 'p': 45, 'mp': 60, 'mf': 75, 'f': 90, 'ff': 105}
    dB_min = 0.8
    dB_max = 1.2
    assert True if dynamic in dB_dict.keys() else False
    assert True if dB_min <= inst_mult <= dB_max else False

    dB_init = dB_dict[dynamic] * inst_mult

    def db_distance(dist):
        """
        Calculates what the dB of the music source would be at a distance
        away. And also check to see if the value of distance is 0, which if
        it is returns the initial dB calculated.
        """
        constant = 20
        assert isinstance(dist, int)
        assert dist > 0
        if dist != 0:
            db = ceil(dB_init - constant * log(dist))
            if db < 0:
                return 0
            else:
                return db
        else:
            return ceil(dB_init)

    return db_distance


# Question2
def next_move(file_names, decision):
    """
    ##############################################################
    # I open the file as a rread and read each line of the file. If the
    decision is s I add the first name to the semi list, if it is h i add it
    to the home lst. Then I return a funciton which adds the message to the
    message according to the decision.#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> message_to_students = next_move("files/names.txt", "h")
    >>> mess = message_to_students("Never give up!")
    >>> print(mess)
    Dear I!
    Unfortunately, it is time to go home. Never give up!
    >>> message_to_students = next_move("files/names.txt", "s")
    >>> mess = message_to_students("San Diego, Earth.")
    >>> print(mess)
    Dear A, C, E, G, K!
    We are happy to announce that you can move to the next round.
    It will be held at San Diego, Earth.

    # Add AT LEAST 3 doctests below, DO NOT delete this line

    >>> print(next_move("files/names.txt", "s")('London, Mars.'))
    Dear A, C, E, G, K!
    We are happy to announce that you can move to the next round.
    It will be held at London, Mars.
    >>> print(next_move("files/names2.txt", "h")('Rip'))
    Dear C, I, K!
    Unfortunately, it is time to go home. Rip
    >>> print(next_move("files/names2.txt", "s")('LESSGOOOOO.'))
    Dear A, E, G!
    We are happy to announce that you can move to the next round.
    It will be held at LESSGOOOOO.
    """
    first_name = 0
    decision_pos = 3

    file = open(file_names, 'r')

    semi_lst = []
    home_lst = []
    for line in file:
        line = line.strip('\n').split(',')
        if line[decision_pos] == 'h':
            home_lst.append(line[first_name])
        elif line[decision_pos] == 's':
            semi_lst.append(line[first_name])

    file.close()

    def build_message(message):
        """
        Builds the message returned to the student if they made it to the
        semi finals or if they get sent home.
        """
        if decision == 'h':
            message_final = 'Dear ' + ', '.join(home_lst) + '!' + \
                    '\nUnfortunately, it is time to go home. ' + message
        else:
            message_final = 'Dear ' + ', '.join(semi_lst) +  \
                '!\nWe are happy to ' \
                'announce that you can move to the next round.' \
                '\nIt will be held at ' + message
        return message_final


    return build_message





# Question3
def forge(filepath):
    """
    ##############################################################
    # Open the file as a read to check the total number of votes the and the
     number for and against the idea. Then find the value that would be the
     majority. Then I gather the information again in the new defined
     function and overwrite the file with the new data#
    # method description and add at least 3 more doctests below. #
    ##############################################################
	>>> forge('files/vote1.txt')(0)
    >>> with open('files/vote1.txt', 'r') as outfile1:
    ...     print(outfile1.read().strip())
    Jerry,0
    Larry,0
    Colin,0
    Scott,0
    Jianming,0
    Huaning,1
    Amy,1
    Elvy,1
    >>> forge('files/vote2.txt')(0)
    >>> with open('files/vote2.txt', 'r') as outfile2:
    ...     print(outfile2.read().strip())
    Jerry,0
    Larry,0
    Colin,0
    Scott,1
    Jianming,0
    Huaning,1
    Amy,1
    Elvy,0
    >>> forge('files/vote3.txt')(1)
    >>> with open('files/vote3.txt', 'r') as outfile3:
    ...     print(outfile3.read().strip())
    Jerry,1
    Larry,1
    Colin,1
    Scott,0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> forge('files/vote4.txt')(1)
    >>> with open('files/vote4.txt', 'r') as outfile4:
    ...     print(outfile4.read().strip())
    Jack Lim,1
    Matt oh yeaa ,1
    Noob,0
    >>> forge('files/vote5.txt')(1)
    >>> with open('files/vote5.txt', 'r') as outfile5:
    ...     print(outfile5.read().strip())
    Jack,1
    Jack,1
    Jack,0
    Jack,0
    Jack,1
    Jack,1
    Jack,1
    Jack,0
    >>> forge('files/vote6.txt')(1)
    >>> with open('files/vote6.txt', 'r') as outfile6:
    ...     print(outfile6.read().strip())
    Jack,0
    Jack,1
    Jack,1
    Jack,1
    Jack,1
    Jack,1
    Jack,0
    Jack,0
    Jack,1
    """
    half = 2
    decision_pos = 1
    count = 0
    yes = 0
    no = 0
    with open(filepath, 'r') as file:
        for line in file:
            count += 1
            if line.strip('\n').split(',')[decision_pos] == '0':
                no += 1
            elif line.strip('\n').split(',')[decision_pos] == '1':
                yes += 1
        if count % 2 == 0:
            majority = ceil(count / half) + 1
        else:
            majority = ceil(count / half)
        file.close()

    def update(decision):
        """
        This function updates the text file that has been forge to make the
        selected majority be the majority. Which does soby first reading the
        file and storing the data in a variable which is then overwritten
        on the file.
        """
        data = ''
        no2 = 0
        yes2 = 0
        with open(filepath, 'r') as file2:
            for line2 in file2:
                line2_cleaned = line2.strip('\n').split(',')
                if decision == 0:
                    if line2_cleaned[decision_pos] != decision and no + no2 \
                            <= \
                            majority:
                        data = data + line2_cleaned[0] + ',' + str(decision) \
                               + '\n'
                        no2 += 1
                    else:
                        data = data + line2
                elif decision == 1:
                    if line2_cleaned[decision_pos] != decision and yes + yes2 \
                            <= \
                            majority:
                        data = data + line2_cleaned[0] + ',' + str(decision) \
                               + '\n'
                        yes2 += 1
                    else:
                        data = data + line2
        with open(filepath, 'w') as overwrite:
            overwrite.write(data)

    return update


# Question4.1
def number_of_adults_1(lst, age=18):
    """
    ##############################################################
    # First I defined a helper function to calculate the no of adults per
    child needed. Then I used a list comprehension in order to count the
    number of children under the age stated. #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> number_of_adults_1([1,2,3,4,5,6,7])
    3
    >>> number_of_adults_1([1,2,3,4,5,6,7], 5)
    2
    >>> number_of_adults_1([1,2,3,4,5,6,7], age = 2)
    1
    
    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> number_of_adults_1([10, 1, 2, 3, 4], age = 3)
    1
    >>> number_of_adults_1([18])
    1
    >>> number_of_adults_1([0], age = 1)
    1
    """
    assert all([True for x in lst if x > 0])

    return cal_no_of_adults([1 for i in lst if i <= age])


# Question4.2
def number_of_adults_2(*args):
    """
    ##############################################################
    # Iterate through the list and return a 1 if the age is less than 18.
    Then I use the helper function to calculate the number of adults needed. #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> number_of_adults_2(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_2(10,20,13,4)
    1
    >>> number_of_adults_2(19, 20)
    0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> number_of_adults_2(18)
    1
    >>> number_of_adults_2()
    0
    >>> number_of_adults_2(1, 2, 3, 4, 5, 6, 7, 8, 9)
    3
    """

    return cal_no_of_adults([1 for i in args if i <= 18])


# Question4.3
def number_of_adults_3(*args, age=18):
    """
    ##############################################################
    # Use list comprehensiont o create a listof student below the age limit,
     then using the helper function to calculate the number of adults needed.#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> number_of_adults_3(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 5)
    2
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 2)
    1

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> number_of_adults_3(18)
    1
    >>> number_of_adults_3(1, 2, 3, 4, age = 4)
    2
    >>> number_of_adults_3()
    0
    """

    return cal_no_of_adults([1 for i in args if i <= age])


# Question5
def school_trip(age_limit, **kwargs):
    """
    ##############################################################
    # Iterating through the kwargs lst of values and appending a new
    dictionary with the values of the number of adults required according to
     the class using the function from 4.3 to so.#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> school_trip(14, class1=[1,2,3], class2 =[4,5,6,7], class3=[15,16])
    {'class1': 1, 'class2': 2, 'class3': 0}
    >>> school_trip(14, class1=[21,3], class2 =[41,1,2,24,6], \
    class3=[30,3,1,7,88])
    {'class1': 1, 'class2': 1, 'class3': 1}
    >>> school_trip(100, class1=[21,3], class2 =[41,1000,2,24,6], \
    class3=[3,1,7,88])
    {'class1': 1, 'class2': 2, 'class3': 2}

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> school_trip(18, class1=[])
    {'class1': 0}
    >>> school_trip(18, class1=[1, 2, 3, 4, 5, 6, 7, 8])
    {'class1': 3}
    >>> school_trip(2, class1=[1, 2, 3, 4, 5, 6], class2=[11, 12, 13, 14, \
    15, 16])
    {'class1': 1, 'class2': 0}
    """
    d = {}
    for cls, s_lst in kwargs.items():
        d[cls] = number_of_adults_3(*s_lst, age = age_limit)

    return d


# Question6
def rearrange_args(*args, **kwargs):
    """
    ##############################################################
    # First I create a list from the args enumerating through them to get
    their index position and the arg, and do the same thing for the kwargs
     in a separate list comprehension and finally adding them together to
     get the final list.#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> rearrange_args(1, 2, 3, 4, 5, 6, 7, 8, 9)
    [('positional_0', 1), ('positional_1', 2), ('positional_2', 3), \
('positional_3', 4), ('positional_4', 5), ('positional_5', 6), \
('positional_6', 7), ('positional_7', 8), ('positional_8', 9)]
    >>> rearrange_args(a=1, d=2)
    [('keyword_0_a', 1), ('keyword_1_d', 2)]
    >>> rearrange_args()
    []
    """

    return [('positional_' + str(i), arg) for i, arg in enumerate(args)] + \
    [('keyword_' + str(i) + '_' + key, value) for i, (key, value) in
     enumerate(kwargs.items())]
