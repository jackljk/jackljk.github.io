"""
DSC20 WI22 HW06
Name: Jack Kai Lim
PID:  A16919063
"""

# Question 1
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function. You don't need to add new doctests for this function.
    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 9 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-9, duplicates allowed) #
    return [3, 4, 1, 3, 5, 2, 6, 3, 9, 7]


#Question2
def find_the_word(lst, word):
    """
    ##############################################################
    # Check if the lst has len of 0, if it does then return 0, if not then
    check to see if the length of the lst is more than 1. If it is return 1
    while adding the value of the next item on the lst using a recussion
    method. And finally when the lst is of length 1, return and add only 1
    or 0 for the very last value without the function.   #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> find_the_word(["tickets"], "tickets")
    1
    >>> find_the_word(["selltickets", "tickets", "gold"], "tickets")
    1
    >>> find_the_word(["ticktok", "toktick"], "tickets")
    0
    >>> find_the_word([], "tickets")
    0
    >>> find_the_word(["ticketticket"], "tickets")
    0
    >>> find_the_word(["tickets", "who", "wants", "cheap", "tickets"],\
     "tickets")
    2
    >>> find_the_word(["tickets tickets", "ticketstickets"], "tickets")
    0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> find_the_word(['Case sensitivity'], 'case sensitivity')
    0
    >>> find_the_word([' '], ' ')
    1
    >>> find_the_word(['', '', ''], '')
    3
    """
    if len(lst) == 0:
        return 0
    elif len(lst) > 1:
        if lst[0] == word:
            return 1 + find_the_word(lst[1:], word)
        else:
            return 0 + find_the_word(lst[1:], word)
    else:
        if lst[0] == word:
            return 1
        else:
            return 0


#Question3.1
def corrupt_string(input, to_insert):
    """
    ##############################################################
    # Check if the input length is 0 if it is return an empty string.If the
    length of the input is more than or equal to 1. Then return the first
    character of the input string and the insert string and the function
    with the first letter sliced.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> corrupt_string('tickets', '#')
    't#i#c#k#e#t#s#'
    >>> corrupt_string('', '@')
    ''
    >>> corrupt_string('buy now', '-')
    'b-u-y- -n-o-w-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_string('Haiyah', '-@')
    'H-@a-@i-@y-@a-@h-@'
    >>> corrupt_string(' ', '[]')
    ' []'
    >>> corrupt_string('WALAOEHHHHHHHH', 'h')
    'WhAhLhAhOhEhHhHhHhHhHhHhHhHh'
    """
    if len(input) == 0:
        return ''
    elif len(input) >= 1:
        return input[0] + to_insert + corrupt_string(input[1:], to_insert)
    else:
        return to_insert




# Question 3.2
def corrupt_list(lst, word, to_insert):
    """

    ##############################################################
    # If the len of the lst is 0, return an empty lst. If the length of the
    list is more than 1, and the word matches the target word, return the
    corrupt string using gthe function defined in question 3.1, and return
    the function again with the list sliced at 1. If the word doesn't match,
    return the word at that position and the function sliced at 1 #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> corrupt_list(['tickets'], 'tickets','#')
    ['t#i#c#k#e#t#s#']
    >>> corrupt_list([], 'tickets','@')
    []
    >>> corrupt_list(['buy now', 'tickets'], 'tickets','-')
    ['buy now', 't-i-c-k-e-t-s-']
    >>> corrupt_list(['buy now', 'fake tickets'], 'tickets','-')
    ['buy now', 'fake tickets']
    >>> corrupt_list(['e-ticket', 'TiCkeTs'], 'tickets','-')
    ['e-ticket', 'TiCkeTs']

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_list(['', '', ' '], ' ', 'LOL')
    ['', '', ' LOL']
    >>> corrupt_list(['Cap', 'cap'], 'cap', '-')
    ['Cap', 'c-a-p-']
    >>> corrupt_list(['Hello', 'HELLLLLLLOOOOOOO'], 'Hello', 'LMAO')
    ['HLMAOeLMAOlLMAOlLMAOoLMAO', 'HELLLLLLLOOOOOOO']
    """
    if len(lst) == 0:
        return []
    elif len(lst) > 1:
        if lst[0] == word:
            return [corrupt_string(word, to_insert)] + corrupt_list(lst[1:],
                    word, to_insert)
        else:
            return [lst[0]] + corrupt_list(lst[1:], word, to_insert)
    else:
        if lst[0] == word:
            return [corrupt_string(word,  to_insert)]
        else:
            return [lst[0]]



            
#Question4
def corrupt_with_vowels(input):
    """

    ##############################################################
    # Check the length of the string, if it is 1 then do the final return,
    else, check to see if the character is a vowel and return an empty
    string if it is and return the character if it is not. #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_with_vowels('')
    ''
    >>> corrupt_with_vowels('Jack')
    'Jck'
    >>> corrupt_with_vowels('This s40uld work')
    'Ths s40ld wrk'
    """
    if len(input) <= 1:
        if len(input) == 0:
            return ''
        elif input[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            return ''
        else:
            return input[0]
    elif input[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return '' + corrupt_with_vowels(input[1:])
    else:
        return input[0] + corrupt_with_vowels(input[1:])




#Question 5
def where_to_go(point1, point2, separator):
    """
    ##############################################################
    # If the bounds are equal then I return the either point. If point 1 is
    less then point2 then I return the point 1 as a string and the separator
     and return the function again with point1 + 1, and the same is done
     when point 2 is smaller however, I return thhe function with point1 - 1
     instead#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> where_to_go(1,  10, 'HAIYAH')
    '1HAIYAH2HAIYAH3HAIYAH4HAIYAH5HAIYAH6HAIYAH7HAIYAH8HAIYAH9HAIYAH10'
    >>> where_to_go(10, 5, 'LOL')
    '10LOL9LOL8LOL7LOL6LOL5'
    >>> where_to_go(7, 10, '')
    '78910'
    """
    if point1 == point2:
        return str(point1)
    elif point1 < point2:
        return str(point1) + separator + where_to_go(point1+1, point2,
                                                     separator)
    elif point1 > point2:
        return str(point1) + separator + where_to_go(point1 - 1,
                                                     point2, separator)


