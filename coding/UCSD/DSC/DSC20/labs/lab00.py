"""
DSC 20 Lab 00
Name: Jack Kai Lim
PID:  A16919063
"""

def new_year_wishes(wish, num):
    """
    This method generates new year wishes by adding exclamation
    marks or returning "Happy New Year" if wish is more than 15
    characters long.

    >>> new_year_wishes("Dream Big", 5)
    'Dream Big!!!!!'
    >>> new_year_wishes("Wish you wealth and happiness", 3)
    'Happy New Year!!!'
    >>> new_year_wishes("Never Too Late", 0)
    'Never Too Late'
    """
    if len(wish) > 15:
        return  'Happy New Year' + '!'*num
    else:
        return wish + '!'*num


