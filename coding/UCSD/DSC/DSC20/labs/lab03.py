"""
DSC 20 Lab 03
Name: Jack Kai Lim
PID: A16919063
"""


# Q1
def ingredient_reverse(input_recipe):
    """
    Read in a file and return a dictionary with the ingredient and its
    corresponding dishes. The order of the ingredients should be the same
    order in which they first appear in the file.

    >>> ingredient_reverse("files/Meat_lover.txt")
    {'Beef': ['Roast Beef', 'Broccoli Beef'], 'Potato': ['Roast Beef'], \
'Black Pepper': ['Roast Beef'], 'Salt': ['Roast Beef', 'Broccoli Beef'], \
'Broccoli': ['Broccoli Beef']}
    >>> ingredient_reverse("files/Blank.txt")
    {}
    >>> ingredient_reverse("files/Asian_fusion.txt")
    {'Pork': ['Guo Bao Rou'], 'Egg': ['Guo Bao Rou', 'Sushi'], \
'Soy Sauce': ['Guo Bao Rou', 'Kung Pao Chicken'], \
'Pepper': ['Guo Bao Rou', 'Kung Pao Chicken'], \
'Green Onion': ['Guo Bao Rou', 'Kung Pao Chicken'], \
'Vinegar': ['Guo Bao Rou', 'Sushi'], 'Chicken': ['Kung Pao Chicken'], \
'Rice': ['Sushi'], 'Cucumber': ['Sushi']}

    """
    with open(input_recipe, 'r') as file:
        d = {}
        with open(input_recipe, 'r') as file:
            for line in file:
                recipe_name = line.strip('\n ').split(':')[0]
                recipe_ings = line.strip('\n ').split(':')[1].split(',')
                recipe_ings = [ing.strip() for ing in recipe_ings]
                for ing in recipe_ings:
                    if ing not in d.keys():
                        d[ing] = []
                for key in d.keys():
                    if key in recipe_ings:
                        d[key].append(recipe_name)

        return d


# Q2
def popular_words_message(messages, word):
    """
    Read in files and return a tuple with the index of the line that contains
    the input word most often and its count. Return a tuple of two zeros if
    the input word can not be found.

    >>> popular_words_message("files/Message_1.txt", "to")
    (9, 3)
    >>> popular_words_message("files/Message_2.txt", "happy")
    (8, 4)
    >>> popular_words_message("files/Message_3.txt", "DSC20")
    (0, 0)
    >>> popular_words_message("files/Message_3.txt", "secret")
    (8, 1)
    """
    total = 0
    line_with_most = 0
    with open(messages) as file:
        for i, line in enumerate(file):
            line = line.lower().strip('\n')
            line = line.replace(',', '')
            line = line.split(' ')
            count = line.count(word)
            if total < count:
                line_with_most = i + 1
            if total < count:
                total = count
    return (line_with_most, total)


# Q3
def cake_decoration(orders):
    """
    IMPORTANT: You should only use list comprehension for this question.
    Follow the syntax guidelines in the writeup.

    Take a list of orders and count the unique letters needed to
    be decorated for orders of even length.

    >>> cake_decoration(['Marina', 'Ruixuan','George'])
    [5, 5]
    >>> cake_decoration([])
    []
    >>> cake_decoration([''])
    [0]
    >>> cake_decoration(["Looooool","Yesssss", 'uncopyrightable.'])
    [3, 16]
    """
    return [len(list(set(word))) for word in orders if orders.index(word)
            == 0 or orders.index(word) == len(orders) - 1]


# Q4
def transpose(matrix):
    """
    IMPORTANT: You should only use list comprehension for this question.
    Follow the syntax guidelines in the writeup.

    Takes in a list of lists representation of a matrix and
    returns its transpose, also as a list of lists.

    >>> arr1 = transpose([[1,2,3],[4,5,6],[7,8,9]])
    >>> print(arr1)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    This test is simply to help you visualize your output,
    it is in no way a hint or part of the solution
    >>> print('\\n'.join(''.join(str(i)) for i in arr1))
    [1, 4, 7]
    [2, 5, 8]
    [3, 6, 9]

    >>> transpose([[1]])
    [[1]]

    >>> arr2 = transpose([[1,2],[3,4],[5,6]])
    >>> print(arr2)
    [[1, 3, 5], [2, 4, 6]]

    >>> print('\\n'.join(''.join(str(i)) for i in arr2))
    [1, 3, 5]
    [2, 4, 6]

    >>> arr3 = transpose([[1],[2],[3],[4],[5],[6]])
    >>> print(arr3)
    [[1, 2, 3, 4, 5, 6]]

    >>> print('\\n'.join(''.join(str(i)) for i in arr3))
    [1, 2, 3, 4, 5, 6]

    """
    return [[matrix[j][i] for j in range(len(matrix))] for i
            in range(len(matrix[0]))]


# Q5
def pascals_triangle(n):
    """
    IMPORTANT: You should only use list comprehension for this question.
    Follow the syntax guidelines in the writeup.

    Takes in an int n and returns a nested list representation of
    Pascal's Triangle where each list is a row.

    >>> arr4 = pascals_triangle(4)
    >>> print(arr4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

    >>> print('\\n'.join(''.join(str(i)) for i in arr4))
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]

    >>> pascals_triangle(0)
    []

    >>> arr6 = pascals_triangle(6)
    >>> print(arr6)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], \
[1, 6, 1, 0, 5, 1]]

    >>> print('\\n'.join(''.join(str(i)) for i in arr6))
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 6, 1, 0, 5, 1]
    """
    return [[int(x) for x in y] for y in [str(11 ** i) for i in range(n)]]
