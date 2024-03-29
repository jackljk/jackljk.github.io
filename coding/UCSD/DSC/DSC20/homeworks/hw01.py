"""
DSC 20 Homework 01
Name: Jack Kai Lim
PID: A116919063
"""

#Helper Functions
def count_digit(n):
    """
    # Helper function for question 1 in order to know how many times to // by 10 #
    # Works by dividing the number x amount of times until it reaches 0, and the count gives us the number of digits#

    >>> count_digit(82759)
    5
    >>> count_digit(2)
    1
    >>> count_digit(0)
    0
    """

    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


# Question 1
def unlucky_number(numbers):
    """
    ##############################################################
    # First I set the value as False as there are only 2 possible answers, therefore if all the if statements fail then
    then 4 is not among the numbers. Next I summed all the numbers in the list, and created a for loop based on the
    number of digit of the numbers to ensure the function can handle large numbers. Each iteration, the function checks
    for whether when the number is modded by 10 whether the remainder is 4 or not, if false we // the summed number and
    repeat the process until all iterations are done, the function either spilts True if its gets a 4 or False if all
    the iterations fail to yield a 4#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    
    >>> unlucky_number([1,2,3,4])
    False
    >>> unlucky_number([1,2,3,4,4])
    True

    # Add at least 3 doctests below here #
    >>> unlucky_number([140, 1000000000])
    True
    >>> unlucky_number([400000, 10])
    True
    >>> unlucky_number([4, 4, 4, 4, 4])
    False
    """
    x = 10
    y = 4
    unlucky = False
    summed_number = sum(numbers)
    for i in range(count_digit(summed_number)):
        if summed_number%x == y:
            unlucky = True
            break
        else:
            summed_number //= x
    return unlucky



# Question 2
def pick_name(names):
    """
    ##############################################################
    # First the function checks to see if the list is empty, if it is, the function returns an empty string. Next the
    function iterates through each name in the list names and checks the number of words by the len of the list given
    from the split function. Then compares to see whether the len if less than the previous one. Length is given a
    large number as a placeholder. Then the function check through each of the names updating the title whenever it
    gets a title shorter than the previous one. If it get a title of the same length it skips over it and continues the
    loop until it has gone through all iterations and the function then returns the title.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> pick_name(["Hi, welcome to DSC20!", "Goodbye to DSC10!", \
"Get Ready To Work Hard!"])
    'Goodbye to DSC10!'
    >>> pick_name(["Start Early!", "Start Often!", "LET'S GO!"])
    'Start Early!'
    >>> pick_name(["Weiyue likes the Fire Spot"])
    'Weiyue likes the Fire Spot'

    # Add at least 3 doctests below here #
    >>> pick_name([])
    ''
    >>> pick_name(["Hello World I'm Here", "Hey World", "Hello World"])
    'Hey World'
    >>> pick_name(["Hello World I'm Here", "Hey World", "Hello World", "BANG!"])
    'BANG!'

    """
    title = 0
    length = 9999
    if len(names) == 0:
        return ''
    for name in names:
        name_as_list = name.split()
        if 0 < len(name_as_list) < length:
            length = len(name_as_list)
            title = name
            if len(names) == 1:
                return title
        elif len(name_as_list) == length:
            continue
        else:
            return title
    return title

# Question 3
def replace_text(text, target_word, desired_word):
    """
    ##############################################################
    # First I check to see whether the target word can be found in the string, if it can be found meaning the find
     finction returns a value, then I use the replace function to replace only the first instance of the word. If the
     find function returns -1, then the target word does not appear therefore I return the Upper of the Text.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> replace_text("Dumplings is a very famous dish for the new year", \
"Dumplings", "🥟")
    '🥟 is a very famous dish for the new year'
    >>> replace_text("dumplings dumplings dumplings", "dumplings", "🥟")
    '🥟 dumplings dumplings'
    >>> replace_text("We all love DSC20", "Lie", "Truth")
    'WE ALL LOVE DSC20'
    >>> replace_text("Happy! new! Year!", "!", "🧧")
    'Happy🧧 new! Year!'

    # Add at least 3 doctests below here #
    >>> replace_text("Checking the spaces", " ", "GAP")
    'CheckingGAPthe spaces'
    >>> replace_text("LOL", "LOL", "Testing to see if it works with one word")
    'Testing to see if it works with one word'
    >>> replace_text("", "What if", "There is no text")
    ''
    """
    target_position = text.find(target_word)
    if target_position != -1:
        return text.replace(target_word, desired_word, 1)
    else:
        return text.upper()




# Question 4
def approved_recipe(recipe, day, threshold):
    """
    ##############################################################
    # First I iterated through the list and take only the weights of the ingredients to get the total weight. Then next
     I check the day, if it is a weekday I divide the total by 2 if its a weekend I leave it as it is. Next I check to
     see if the weight is more than equal to the threshold. If it is I go through if statements to check if all the
     ingredients wanted by Uncle Roger is present.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> approved_recipe([['msg', 10], ['rice', 20], ['egg', 30]], 'FRIDAY', 30)
    'Fuiyoh'
    >>> approved_recipe([['msg', 10], ['rice', 20], ['egg', 30]], 'friday', 31)
    'Haiyah'
    >>> approved_recipe([['soy sauce', 10], ['rice', 20], ['egg', 30]], \
'FRIDAY', 30)
    'Haiyah'
    
    # Add at least 3 doctests below here #
    >>> approved_recipe([['msg', 10], ['paella', 20], ['egg', 30]], \
'Saturday', 30)
    'Haiyah'
    >>> approved_recipe([['msg', 10], ['rice', 20], ['egg', 30]], \
'FRIDAY', 100)
    'Haiyah'
    >>> approved_recipe([['msg', 10], ['rice', 20], ['EGG', 30]], 'FRIDAY', 30)
    'Fuiyoh'
    """
    weight = 0
    day = day.lower()
    for item in recipe:
        weight += item[1]
    if day != 'saturday' or 'sunday':
        weight /= 2

    if weight >= threshold:
        for item in recipe:
            if item[0].lower() == 'msg':
                for item in recipe:
                    if item[0].lower() == 'egg':
                        for item in recipe:
                            if item[0].lower() == 'rice':
                                return 'Fuiyoh'
    else:
        return 'Haiyah'
    return 'Haiyah'
# Question 5
def money_got(grades):
    """
    ##############################################################
    # First I check to see if the grade list has any elements to determine if the output should be gapped. Next I
    iterate throught he list of grades and check using if statements to determine what the grade got is and add it to
    the total amount of money.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> money_got([])
    'Gapped'
    >>> money_got(["A+", 'A+', "A+", 'A', 'P'])
    90
    >>> money_got(["A+", "A+", "W"])
    0

    # Add at least 3 doctests below here #
    >>> money_got(['W', 'W'])
    -200
    >>> money_got(['a', 'b', 'a+'])
    100
    >>> money_got(["a", "b", "a+","A+", 'A+', "A+", 'A', 'P'])
    190
    """
    aplus, a, aminus = 50, 40, 30
    bplus, b, bminus = 20, 10, 8
    money = 0
    if len(grades) == 0:
        return 'Gapped'

    for grade in grades:
        grade = grade.upper()
        if grade == 'A+':
            money += aplus
        elif grade == 'A':
            money += a
        elif grade == 'A-':
            money += aminus
        elif grade == 'B+':
            money += bplus
        elif grade == 'B':
            money += b
        elif grade == 'B-':
            money += bminus
        else:
            money -= 100
    return money

# Question 6
def number_bought(name, grades, product, price):
    """
    ##############################################################
    # First we get the total money earned using the function from the previous question. Next, we check if the price
     is a integer. If it is not  I return system error. If it is integer, next I check to see if the money earned, is
     more than the price of the item, is it isn't we return that nothing is purchased and set the money left as the
     total money. If money is more than the price, I get the number total number of the item I can purchased, and the
     remaining amount of money.#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    
    >>> number_bought("Yi", ["A+", 'A+', "A+", 'A', 'P'], "milk tea", 5)
    'Yi has bought 18 milk tea and has $0 left.'
    >>> number_bought("Yi", ["A+", 'A+', "A+", 'A', 'P'], "milk tea", 5.2)
    'System Error!'
    >>> number_bought("Weiyue", ["S"], "Football", 200)
    'Weiyue has bought 0 Football and has $-100 left.'

    # Add at least 3 doctests below here #
    >>> number_bought("Yi", ["A+", 'A+', "A+", 'A', 'b-'], "milk tea", 5)
    'Yi has bought 39 milk tea and has $3 left.'
    >>> number_bought("Bob", ["a+", "a+", "a+", "a+"], "Football", 200)
    'Bob has bought 1 Football and has $0 left.'
    >>> number_bought("Yi", ["A+", 'A+', "A+", 'A', 'P'], "milk tea", 'Hello this is a test')
    'System Error!'
    """
    money = money_got(grades)
    if type(price) == int:
        if money >= price:
            no_purchased = money//price
            money_left = money - (no_purchased * price)
        else:
            no_purchased = 0
            money_left = money
    else:
        return 'System Error!'

    return name + ' has bought ' + str(no_purchased) + ' ' + product + ' and has $' + str(money_left) + ' left.'

# Question 7
def report(people, their_grades, products, prices):
    """
    ##############################################################
    # First I get the total number of of people that I will be reporting on. Then I change the order moving from the
    outside in. Then I iterate through the numbers in the new order and use the function from the previous problem
     to get the wanted string. Then I check to see whether there is another people to report, if there is I add a new
     line if there isn't I return the report.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> print(report(["Theo"], [["A+"]], ["iPad"], [1200]))
    Theo has bought 0 iPad and has $50 left.
    >>> print(report(["Yi", "Yi", "Weiyue", "Jianming"], \
    [["A+", 'A+', "A+", 'A', 'P'], ["A+", 'A+', "A+", 'A', 'P'],\
    ["S"], ["A"]], ["milk tea", "MILK TEA", "Football", "Flowers"], \
    [5,5.2,200,1]))
    Yi has bought 18 milk tea and has $0 left.
    Jianming has bought 40 Flowers and has $0 left.
    System Error!
    Weiyue has bought 0 Football and has $-100 left.
    >>> print(report(["Yi", "Weiyue", "Jianming"], \
    [["A+", 'A+', "A+", 'A', 'P'], \
    ["S"], ["A"]], ["milk tea", "Football", "Flowers"], \
    [5,200,1]))
    Yi has bought 18 milk tea and has $0 left.
    Jianming has bought 40 Flowers and has $0 left.
    Weiyue has bought 0 Football and has $-100 left.

    >>> print(report(["Yi", "Weiyue", "Jianming"], \
    [["A+", 'A+', "A+", 'A', 'P'], \
    ["S"], ["A"]], ["milk tea", "Football", "Flowers"], \
    [5,200,'hi']))
    Yi has bought 18 milk tea and has $0 left.
    System Error!
    Weiyue has bought 0 Football and has $-100 left.

    >>> print(report(["Yi", "Weiyue", "Jianming", "Bob", 'Ryan'], \
    [["A+", 'A+', "A+", 'A', 'P'], \
    ["S"], ["A"], ['A+', 'A+'], ["a+", "b"]], ["milk tea", "Football", "Flowers", "Water", "Tennis Racket"], \
    [5,200,1, 50,30]))
    Yi has bought 18 milk tea and has $0 left.
    Ryan has bought 2 Tennis Racket and has $0 left.
    Weiyue has bought 0 Football and has $-100 left.
    Bob has bought 2 Water and has $0 left.
    Jianming has bought 40 Flowers and has $0 left.

    >>> print(report(["Theo"], [["A+", "A+", "A+", "A+", "A+"]], ["iPad"], [1200.00]))
    System Error!
    """
    text = ''
    order = list(range(len(people)))
    order = [order[-i//2] if i % 2 else order[i//2] for i in range(len(order))]
    for i in order:
        text = text + number_bought(people[i], their_grades[i], products[i], prices[i])
        if i != order[-1]:
            text = text + '\n'
        else:
            return text
    return text


# Question 8
def pick_best_shoes(selections, numbers):
    """
    ##############################################################
    # I iterate through the list of numbers and put them through a long if, elif statements. To check whether the number
     is perfectly divisible to 2, 3, 5, 7 or none of them and in that order and which ever if statement comes back true
     I do the related operation to the divisable number. Then next, I choose the shoe which matches the number and check
     for whether it is negative or if it is larger than the length of the list and fix the number accordingly.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> pick_best_shoes(["AJ1", "AJ2", "AJ3"], [2,3,5,7,9])
    'AJ1'
    >>> pick_best_shoes(["AJ1", "AJ2", "AJ3"], [2,4,6])
    'AJ2'
    >>> pick_best_shoes(["Air Mag"], [2001])
    'Air Mag'

    >>> pick_best_shoes(["AJ1", "AJ2", "AJ3", "Off-White", "Gucci"], [2,3,5,7,9,20,142,33])
    'AJ1'
    >>> pick_best_shoes(["AJ1", "AJ2", "AJ3"], [2,5])
    'AJ1'
    >>> pick_best_shoes(["AJ1", "Ultra-Boost"], [100000, 200000, 31])
    'Ultra-Boost'

    """
    add = 2
    minus = 3
    divide = 5
    exp = 7
    current_number = 1
    for number in numbers:
        if number % add == 0:
            current_number += number
        elif number % minus == 0:
            current_number -= number
        elif number % divide == 0:
            current_number /= number
        elif number % exp == 0:
            current_number **= number
        else:
            current_number //= number

    selection = int(current_number)
    if selection > len(selections):
        selection = selection % len(selections)
        return selections[selection]
    elif selection < -len(selections):
        selection = selection % len(selections)
        return selections[selection]
    else:
        return selections[selection]




# Question 9
def concat_lyrics(lyrics, threshold):
    """
    ##############################################################
    # First I iterate through the lines in the list, and as each line as a list, I add to the count the number of words
    in the list. If the count is less than the threshold number then I iterate through the line list through each word.
    And for each word I add it to the text that I am going to return, and I also check to see if the word I am on is
    the last word or not. As if it is not the last word I add a space and if it is the last word I go to the next
    line. #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> print(concat_lyrics([["We’re", "so", "young,", "boy"],\
    ["We", "ain’t", "got", "nothin'", "to", "lose"]], 10))
    We’re so young, boy
    We ain’t got nothin' to lose
    <BLANKLINE>
    >>> print(concat_lyrics([["We’re", "so", "young,", "boy"],\
    ["We", "ain’t", "got", "nothin'", "to", "lose"]], 9))
    We’re so young, boy
    <BLANKLINE>
    >>> concat_lyrics([["We’re", "so", "young,", "boy"],\
    ["We", "ain’t", "got", "nothin'", "to", "lose"]], 3)
    ''

    >>> print(concat_lyrics([['We'],['are','the','champions'], ['my', 'friend']], 3))
    We
    my friend
    <BLANKLINE>

    >>> print(concat_lyrics([['We'],['are','the','champions'], ['my', 'friend'], ['WEEEEEEEEEE']], 2))
    We
    WEEEEEEEEEE
    <BLANKLINE>
    >>> print(concat_lyrics([['We'],['are','the','champions', 'oh yea'], ['my', 'friend'], ['WEEEEEEEEEE']], 4))
    We
    my friend
    WEEEEEEEEEE
    <BLANKLINE>
    """
    text = ''
    count = 0
    for line in lyrics:
        count += len(line)
        if count <= threshold:
            for word in line:
                text = text + word
                if word != line[len(line) - 1]:
                    text = text + ' '
            text = text + '\n'
        elif line != lyrics[-1]:
            count -= len(line)
    return text


# Question 10
def in_festival(fest_coord, approx_loc, radius):
    """
    ##############################################################
    # First I calculate the distance between the approximate coordinate and the festival coordinates. Then I check
     to see if it is less than or equal to the radius. If it is I return True if it is not I return False#
    # method description and add at least 3 more doctests below. #
    ##############################################################
    
    >>> in_festival([1,2], [2,4], 2)
    False
    >>> in_festival([1,2], [3,2], 1)
    False
    >>> in_festival([1,2], [2,2], 1)
    True

    >>> in_festival([200, 1000], [1, 2], 10000000)
    True
    >>> in_festival([-100, -100], [10, -300], -200)
    False
    >>> in_festival([12.31, 0.00001], [0.111, 12971], 0.5)
    False
    """
    x1, y1 = fest_coord[0], fest_coord[1]
    x2, y2 = approx_loc[0], approx_loc[1]
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if dist <= abs(radius):
        return True
    else:
        return False
