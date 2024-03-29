"""
DSC 20 Lab 04
Name: Jack Kai Lim
PID: A16919063
"""


# Q1
def smiley(message):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this
    question. Instead, use lambda functions, any, map, and/or filter.

    Make a function that converts specific characters to smiley faces.
    
    >>> smiley("DSC20:(")
    'DSC20:)(:'
    >>> smiley(":e)k3o(")
    ':)e:)k3o(:'
    >>> smiley(":(((((")
    ':)(:(:(:(:(:'
    """

    return ''.join(list(map(lambda s: s + ')' if s == ':' else s + ':'
    if s == '(' else ':' + s if s == ')' else s, message)))


# Q2
def math_message(message):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this
    question. Instead, use lambda functions, map, and/or filter.

    Make a function that converts the specified characters to numbers and
    removes non-alphanumeric characters.

    >>> math_message("Math!!")
    'M4th'
    >>> math_message("DSC20 is Great! :))")
    'D5C20i5Gr34t'
    >>> math_message("!@!@!@")
    ''
    """
    return ''.join(list(filter(lambda s: s.isalnum(), list(map(lambda s: '3'
    if s.lower() == 'e' else '4' if s.lower() == 'a' else 0 \
        if s.lower() == 'o' else '5' if s.lower() == 's' else s, message)))))


# Q3
def chocolate_cakes(recipes):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this
    question. Instead, use lambda functions, map, and/or filter.

    Take a dictionary of dishes and ingredients
    and return cakes that contain chocolate in them.

    >>> chocolate_cakes({'rum cake': ["chocolate", "cheese"], 'fried rice'\
    : ["egg", "rice"]})
    ['rum cake']
    >>> chocolate_cakes({'cheesecake': ["sugar", "cheese"], 'fried rice': \
    ["egg", "rice"]})
    []
    >>> chocolate_cakes({})
    []
    """
    return list(filter(lambda s: isinstance(s, str), list(map(lambda key,\
    values: key if any(filter(lambda ing: (ing == 'chocolate'), values)) \
    else None, recipes, recipes.values()))))


# Q4
def contains_ingredients(ing, check_ing):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this
    question. Instead, use lambda functions, map, and/or filter.

    Take a 2D list of ingredients you have and a list of pancake ingredients.
    Return a 2D list where each list only contains ingredients present in
    the list of pancake ingredients.

    >>> contains_ingredients([["peanut butter","sugar"], ["maple syrup", \
    "brown sugar", "salt"], ["flour", "eggs", "tomatoes"]], ["sugar", \
    "maple syrup", "eggs", "flour"])
    [['sugar'], ['maple syrup'], ['flour', 'eggs']]

    >>> contains_ingredients([["honey", "cinnamon"], ["water", "cucumber"], \
    ["flour", "eggs", "eggplants"], ["vanilla"]], ["vanilla", "honey", \
    "cinnamon", "eggs",])
    [['honey', 'cinnamon'], [], ['eggs'], ['vanilla']]
    """

    return list(map(lambda ings_list: list(filter(lambda x: isinstance(\
        x, str), list(map(lambda ing: ing if ing in check_ing else None,\
                          ings_list)))), ing))


# Q5
def christmas_gifts(gifts, maximum_price):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this
    question. Instead, use lambda functions, map, and/or filter.

    Given a list of tuples (Gift, Price), return the list of presents you
    bought. You should buy any present the price of which is below or equal to
    the maximum price.

    >>> gifts = [('Laptop', 100), ('PS5', 150), ('car', 500), \
    ('Plane ticket', 150)]
    >>> christmas_gifts(gifts, 200)
    ['Laptop', 'PS5', 'Plane ticket']

    >>> gifts = [('Phone', 10), ('PS5', 150), ('car', 500), \
    ('Laptop', 50), ('Clothes', 21)]
    >>> christmas_gifts(gifts, 10)
    ['Phone']
    """
    return list(filter(lambda x: isinstance(x, str), map(lambda t: t[0] if t[1]
    <= maximum_price else None, gifts)))


# Q6
def notifications(notifications_list, max_chars):
    """
    IMPORTANT: You should NOT use loops or list comprehensions for this
    question. Instead, use lambda functions, map, and/or filter.

    Given a list of notifications and the number of max characters,
    determine the number of notifications that you received the alert for.

    >>> notif = ['John, Call us', 'Please review our Subscription Policy', \
    'Congrats, you are enrolled in DSC20', 'Pay you rent tomorrow']
    >>> notifications(notif, 35)
    3
    >>> notifications(notif, 1)
    0
    >>> notifications(notif, 100)
    4
    """
    return sum(filter(lambda x: isinstance(x, int), map(lambda s: 1 if len(s) \
    <= max_chars else None, notifications_list)))
