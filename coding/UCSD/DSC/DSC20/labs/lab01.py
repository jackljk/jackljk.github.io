"""
DSC 20 Lab 01
Name: Jack Kai Lim
PID: A16919063
"""

# Question 1
def channel_title(first, second, limit):
    """
    >>> channel_title('favorite', 'recipes', 70)
    'Favorite 15 Recipes.'
    >>> channel_title('favorite', 'recipes', 17)
    'Favorite 15 Rec.'
    >>> channel_title('yum', 'recipes', 10)
    'yumyumyum'
    >>> channel_title('yummy', 'rice', 10)
    'Super Chef'
    >>> channel_title('good', 'food', 15)
    'Good 8 Food.'
    >>> channel_title('', '', 3)
    ''
    >>> channel_title(' ', '', 2)
    'Super Chef'
    """
    x = str(len(first) + len(second))
    First = first.capitalize()
    Second = second.capitalize()
    string = First + ' ' + x + ' ' + Second + '.'
    if len(string) <= limit:
        return string
    if len(second) > 3:
        string = First + ' ' + x + ' ' + Second[0:3] + '.'
        if len(string) <= limit:
            return string
    if len(first) <= 3:
        string = first + first + first
        if len(string) <= limit:
            return string
    return 'Super Chef'


# Question 2
def recipe_type(lst):
    """
    >>> recipe_type([])
    'No preference'
    >>> recipe_type(['vegetarian', 'meatarian','vegetarian', 'meatarian', 'meatarian'])
    'meatarian'
    >>> recipe_type(['vegetarian', 'meatarian','vegetarian'])
    'vegetarian'
    """
    if lst.count('vegetarian') > lst.count('meatarian'):
        return 'vegetarian'
    if lst.count('vegetarian') < lst.count('meatarian'):
        return 'meatarian'
    else:
        return 'No preference'



# Question 3
def recipe_name(input, index):
    """
    >>> recipe_name("maytuwmbmdyu ismafldaxd", 2)
    'yummy salad'
    >>> recipe_name("marina", 6)
    'NoName'
    >>> recipe_name("marina", -4)
    'NoName'
    >>> recipe_name("fried_r i c e ", 6)
    'rice'
    >>> recipe_name("", 0)
    'NoName'
    >>> recipe_name("jdka c a k e", 4)
    '    '
    """
    if index < 0:
        return 'NoName'
    if index > len(input) - 1:
        return 'NoName'
    else:
        string = input[index]
        for i in range(index + 2, len(input), 2):
            string = string + input[i]
        return string



# Question 4
def total_calories(portions, calories):
    """
    >>> total_calories(3, 300)
    'For 3 portions your meal has 900 calories.'
    >>> total_calories(2, 100.75)
    'For 2 portions your meal has 201.5 calories.'
    >>> total_calories(7, 250.35)
    'For 7 portions your meal has 1752.45 calories.'
    >>> total_calories(0, 100)
    'For 0 portions your meal has 0 calories.'
    >>> total_calories(100, 0)
    'For 100 portions your meal has 0 calories.'
    """
    calories = str(calories*portions)
    portions = str(portions)
    return 'For ' + portions + ' portions your meal has ' + calories + ' calories.'


# Question 5
def calories_per_portion(input):
    """
    >>> calories_per_portion("For 7 portions your meal has 1752 calories.")
    '250.29'
    >>> calories_per_portion("For 4 portions your meal has 1000 calories.")
    '250.0'
    >>> calories_per_portion("For 1 portions your meal has 1 calories.")
    '1.0'
    >>> calories_per_portion("For 10 portions your meal has 0 calories.")
    '0.0'
    """
    input = input.split()
    portion = int(input[1])
    calories = int(input[6])
    return str(round(calories/portion, 2))


# Question 6
def calories_per_item(hundr, weight, number_cookies, output_type):
    """
    >>> calories_per_item(430, 0.3, 20, 0)
    'One item has 64.5 kcal.'
    >>> calories_per_item(430, 0.3, 20, 1)
    'One item has 64.5 Calories.'
    >>> calories_per_item(1, 1000, 10, 1)
    'One item has 1000.0 Calories.'
    >>> calories_per_item(1, 1000, 10, 0)
    'One item has 1000.0 kcal.'
    >>> calories_per_item(0, 1000, 10, 0)
    'One item has 0.0 kcal.'
    """
    if output_type == 0:
        type = ' kcal'
    if output_type == 1:
        type = ' Calories'
    weight_per_item = weight/number_cookies*1000
    cal = str(weight_per_item/100 * hundr)
    return 'One item has ' + cal + type  +'.'

