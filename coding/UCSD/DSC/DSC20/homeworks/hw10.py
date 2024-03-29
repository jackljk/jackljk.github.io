"""
DSC 20 Homework 10
Name: Jack Kai Lim
PID:  A16919063
"""

from util import Stack, Queue


# Question 1
def parentheses_checker(expression):
    """
    ##############################################################
    # By using a stack, only if the top opennign parenthesis of the stack is
     does not match, then we return False. Else we return True in every other
     case.  #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> parentheses_checker("(((]})")
    False
    >>> parentheses_checker("(")
    False
    >>> parentheses_checker("(){}[]]")
    False
    >>> parentheses_checker("(   x   )")
    True
    >>> parentheses_checker("a()b{}c[]d")
    True
    >>> parentheses_checker("")
    True

    # Add at least 3 doctests below #
    
    """
    # YOUR CODE GOES HERE #
    opening_sym = ['[', '{', '(']
    s = Stack()
    for sym in expression:
        if sym in opening_sym:
            s.push(sym)
        else:
            if sym in ['[', '{', '(', ']', '}', ')']:
                if s.is_empty():
                    return False
                top_sym = s.pop()
                if top_sym == '(':
                    if sym != ')':
                        return False
                if top_sym == '[':
                    if sym != ']':
                        return False
                if top_sym == '{':
                    if sym != '}':
                        return False

    if s.is_empty():
        return True
    elif s.num_items == 1:
        return False
    return True


# Question 2
def run_around(n, m):
    """
    n is the number of players in the circle
    m is the number of the player removed from a game
    functions prints the number of removed player, in order
    >>> run_around(6,3)
    3
    6
    4
    2
    5
    1
    >>> run_around(-1,-2)
    Traceback (most recent call last):
    ...
    ValueError: m and n should be positive!
    >>> run_around('5','1')
    Traceback (most recent call last):
    ...
    TypeError: Invalid input data type.

    # Add at least 3 doctests below #
    >>> run_around(3, 0)
    Traceback (most recent call last):
    ...
    ValueError: m and n should be positive!
    >>> run_around(3, 1)
    1
    2
    3
    >>> run_around(True, False)
    Traceback (most recent call last):
    ...
    ValueError: m and n should be positive!
    """
    # YOUR CODE GOES HERE #
    if not all(isinstance(x, int) for x in [n, m]):
        raise TypeError('Invalid input data type.')
    if not all(map(lambda x: True if x > 0 else False, [n, m])):
        raise ValueError('m and n should be positive!')
    q = Queue()
    for i in range(n):
        q.enqueue(i + 1)
    while not q.is_empty():
        for i in range(m):
            if not q.is_empty() and (i + 1) != m:
                x = q.dequeue()
                q.enqueue(x)
            else:
                x = q.dequeue()
                print(x)


# Question 3 (extra credit, you are on your own)

def choices_choices(candidate, pattern, possibility):
    """
    Append all possible words to possibility list

    >>> p = []
    >>> choices_choices(['t','p','h'], "_ower", p)
    >>> p
    ['tower', 'power', 'hower']

    >>> p = []
    >>> choices_choices(['w','c','d'], "_o_er", p)
    >>> p
    ['wocer', 'woder', 'cower', 'coder', 'dower', 'docer']

    >>> p = []
    >>> choices_choices(['w','c','d'], "coder", p)
    >>> p
    ['coder']

    # Add at least 3 doctests below #
    >>> p = []
    >>> choices_choices(['a', 'b', 'c'], '__l', p)
    >>> p
    ['abl', 'acl', 'bal', 'bcl', 'cal', 'cbl']
    >>> p = []
    >>> choices_choices(['p'], '_oo', p)
    >>> p
    ['poo']
    >>> p = []
    >>> choices_choices(['h', 'm'], '_our', p)
    >>> p
    ['hour', 'mour']
    """

    # YOUR CODE GOES HERE #
    l = []

    def inner(letters, pat):
        if len(letters) == 1:
            l.append(pat.replace('_', letters[0], 1))
        else:
            l.append(pat.replace('_', letters[0], 1))
            return inner(letters[1:], pat)

    inner(candidate, pattern)
    for i, word in enumerate(l):
        if word.find('_') == -1:
            if word not in possibility:
                possibility.append(word)
        else:
            x = [x for x in candidate if candidate.index(x) != i]
            inner(x, word)



