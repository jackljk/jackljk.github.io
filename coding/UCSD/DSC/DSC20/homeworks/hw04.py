"""
DSC 20 Homework 04
Name: Jack Kai LIm
PID: A16919063
"""
from math import log


# Question 1.1
def contract_list(filepath):
    """
    ##############################################################
    # Open the filepath and read from the filepath, then I split the text
    whenever there is a newline. #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> contract_list('files/contracts1.txt')
    ['Theo Hui, 19', 'Ben Ly, 20', 'Nathan Buenviaje, 23']
    >>> contract_list('files/contracts2.txt')
    ['Luke Pacetti, 17', 'Jonah Garcia, 16', 'Brandon Olander, 20', \
'Ed Cloyd, 400']
    >>> contract_list('files/contracts3.txt')
    ['Stewie Lewis, 22', 'Sarah Culbertson, 19', 'Kim Lam, 21']
    >>> contract_list('files/contracts4.txt')
    ['Jack, 20', 'Ryan, 100', 'Bob, 2020', '']
    >>> contract_list('files/contracts5.txt')
    ['Theo Hui, 19', 'Ben Ly, 20', 'Nathan Buenviaje, 23', 'Luke Pacetti, \
17', 'Jonah Garcia, 16', 'Brandon Olander, 20', 'Ed Cloyd, 400', 'Stewie \
Lewis, 22', 'Sarah Culbertson, 19', 'Kim Lam, 21', 'Jack, 20', \
'Ryan, 100', 'Bob, 2020', '']
    >>> contract_list('files/contracts6.txt')
    ['Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr., \
108754931659231654978631298546']
    """
    return open(filepath).read().split('\n')


# Question 1.2
def registration(names, veterans):
    """
    ##############################################################
    # I map through all the names in the name list to get the age as a
    number,then I map through each name returning the name in the list of
    the name can't be found in the veteran list and has a age less than or
    equal to 21 #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> registration(['Theo, 19', 'Ben, 20', 'Nathan, 23'], \
['Ben, 20', 'Colby, 18'])
    ['Theo, 19']
    >>> registration(['Michelle, 17', 'Jonah, 16', \
'Brandon, 20', 'Ed, 40'], [])
    ['Michelle, 17', 'Jonah, 16', 'Brandon, 20']
    >>> registration([], ['Stewie, 22', 'Sarah, 19', 'Kim, 21'])
    []

    >>> registration([12], ['Ben, 20'])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> registration(['Ben, 20'], [12])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> registration(('Ben, 20'), [])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> registration(['Ben, 20'], ('Bob, 21'))
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(names, list)
    assert isinstance(veterans, list)
    assert all(isinstance(x, str) for x in names)
    assert all(isinstance(x, str) for x in veterans)

    return list(filter(lambda x: isinstance(x, str), map(lambda lst: ' '.join(
            lst) if int(lst[1]) <= 21 and ' '.join(lst) not in veterans
            else None, map(lambda name: name.split(' '), names))))


# Question 2.1

def generate_labels_review(band_info):
    """
    ##############################################################
    # First if I check if the persons age is before 2022, if it is then I
    form the label. And return it. #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> generate_labels_review([('Ben Chen', 2016, 18, 'Flute'), \
('Theo Hui', 2021, 32, 'Mallet')])
    {'Ben Chen': 'ben18chen16flute', 'Theo Hui': 'theo32hui21mallet'}
    >>> generate_labels_review([])
    {}
    >>> generate_labels_review([('Linh Truong', 2077, 42, 'trombone'), \
('Gwen Am', 2006, 69, 'Trombone'), ('Brandon brandon', 1996, 0, 'Bass')])
    {'Gwen Am': 'gwen69am06trombone', 'Brandon brandon': 'bran0brandon96bass'}

    >>> generate_labels_review([(12629, 2016, 18, 'Flute')])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review([('Ben Chen', 2016, 18, 4123)])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review([('Ben Chen', 2016, '18', 'Flute')])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review([('Ben Chen', '2016', 18, 'Flute')])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review((['Ben Chen', 2016, 18, 'Flute'], ('Theo Hui',\
    2021, 32, 'Mallet')))
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review((('Ben Chen', 2016, 18, 'Flute'), ('Theo Hui',\
    2021, 32, 'Mallet')))
    Traceback (most recent call last):
    ...
    AssertionError
    """
    name = 0
    year = 1
    dot_num = 2
    instr = 3
    assert isinstance(band_info, list)
    assert all(isinstance(x, tuple) for x in band_info)
    assert all(isinstance(x[name], str) for x in band_info)
    assert all(isinstance(x[year], int) for x in band_info)
    assert all(isinstance(x[dot_num], int) for x in band_info)
    assert all(isinstance(x[instr], str) for x in band_info)

    d = {}
    for person in band_info:
        if person[year] < 2022:
            d[person[name]] = person[name].split(' ')[0].lower()[:4] + str(
                person[dot_num]) + person[name].split(' ')[1].lower() + str(
                person[year])[-2:] + person[instr].lower()
    return d


# Question 2.2

def generate_labels(band_info):
    """
    ##############################################################
    # Created a lambda function to create the label, and to iterate through
    the band_info list to create a list of tghe keys and values for the
    dictionary. then I use .update to add the values to the list #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> generate_labels([('Ben Chen', 2016, 18, 'Flute'), \
('Theo Hui', 2021, 32, 'Mallet')])
    {'Ben Chen': 'ben18chen16flute', 'Theo Hui': 'theo32hui21mallet'}
    >>> generate_labels([])
    {}
    >>> generate_labels([('Linh Truong', 2077, 42, 'trombone'), \
('Gwen Am', 2006, 69, 'Trombone'), ('Brandon brandon', 1996, 0, 'Bass')])
    {'Gwen Am': 'gwen69am06trombone', 'Brandon brandon': 'bran0brandon96bass'}

    # Add at least 3 doctests below here #
    >>> generate_labels_review([(12629, 2016, 18, 'Flute')])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review([('Ben Chen', 2016, 18, 4123)])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review([('Ben Chen', 2016, '18', 'Flute')])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review([('Ben Chen', '2016', 18, 'Flute')])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review((['Ben Chen', 2016, 18, 'Flute'], ('Theo Hui',\
    2021, 32, 'Mallet')))
    Traceback (most recent call last):
    ...
    AssertionError
    >>> generate_labels_review((('Ben Chen', 2016, 18, 'Flute'), ('Theo Hui',\
    2021, 32, 'Mallet')))
    Traceback (most recent call last):
    ...
    AssertionError
    """
    name = 0
    year = 1
    dot_num = 2
    instr = 3
    assert isinstance(band_info, list)
    assert all(isinstance(x, tuple) for x in band_info)
    assert all(isinstance(x[name], str) for x in band_info)
    assert all(isinstance(x[year], int) for x in band_info)
    assert all(isinstance(x[dot_num], int) for x in band_info)
    assert all(isinstance(x[instr], str) for x in band_info)
    d = {}
    create_label = lambda person: person[name].split(' ')[0].lower()[:4] + str(
        person[dot_num]) + person[name].split(' ')[1].lower() + str(
        person[year])[-2:] + person[instr].lower()
    lst_of_key_values = lambda t: [t[name], create_label(t)] if t[year] < \
                        2022 else None
    d.update(filter(lambda l: isinstance(l, list), map(lst_of_key_values,
                                                       band_info)))
    return d


# Question 3
def find_bands(bands, target_avg, target_range, min_shows):
    """
    ##############################################################
    # First I define a lambda function to get the avg score, only including
    the band if they have perform more times then the minimum. Then I check
    to see if the avg of the band is within the target range, and return it
    if it is. #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> DCI = {'Blue Devils': [98.2, 97.1, 99.1, 97.3, 98.2], \
        'Blue Coats': [98, 96.5, 97.2, 93, 92.1, 92, 97.4], \
        'Carolina Crown': [75.7, 82.8, 86.1, 98.2], \
        'The Cadets': [96.1, 93.4, 81, 78, 57.9, 86, 71.2, 35.5], \
        'Mandarins': [89.3, 88.1, 85.6, 83.8, 79.1, 88.4, 75.7], \
        'Little Rocks':[42], \
        'Logan Colts':[98.2, 84.4, 69.2, 42, 84]}

    >>> find_bands(DCI, (0, 10), 30, 2)
    []
    >>> find_bands(DCI, (90, 5), 5, 7)
    ['Mandarins']
    >>> find_bands(DCI, (70, 8), 10, 5)
    ['The Cadets', 'Logan Colts']
    >>> find_bands(DCI, (95, 3), 5, 4)
    ['Blue Devils', 'Blue Coats', 'The Cadets']
    >>> find_bands(DCI, (50, 2), 100, 1)
    ['Blue Devils', 'Blue Coats', 'Carolina Crown', 'The Cadets', \
'Mandarins', 'Little Rocks', 'Logan Colts']
    >>> find_bands(DCI, (100, 10), 0, 1)
    []
    >>> find_bands(DCI, (0, 5), 20, 1)
    []
    """
    avg = lambda l: sum(l[:target_avg[1]])/len(l[:target_avg[1]])
    bands_avg = lambda d: (d[0], avg(d[1])) if len(d[1]) >= min_shows else None
    avg_check = lambda t: t[0] if target_avg[0] - target_range < t[1] < \
                target_avg[0] + target_range else None

    return list(filter(lambda x: isinstance(x, str), map(avg_check,filter(
        lambda x: isinstance(x, tuple), map(bands_avg, bands.items())))))
