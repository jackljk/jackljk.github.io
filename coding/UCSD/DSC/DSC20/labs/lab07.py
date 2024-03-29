# Question 1.

class Mascot:
    """ 
    Creates a simple Mascot class with 1 class attribute (type)
    and 3 instance attributes (color, nickname, event)
    >>> mascot1 = Mascot("black and white", "Bing Dwen Dwen", "Olympic Games")
    >>> Mascot.brings
    'Luck'
    >>> mascot1.color
    'black and white'
    >>> mascot1.sing_song("Together for a shared future")
    "Bing Dwen Dwen sings 'Together for a shared future' at Olympic Games"
    >>> mascot1.change_nickname("Puff Puff")
    >>> mascot1.nickname
    'Puff Puff'
    >>> mascot1.event
    'Olympic Games'

    >>> mascot2 = Mascot("brown", "Mishka", "Olympic Games")
    >>> Mascot.brings
    'Luck'
    >>> mascot2.color
    'brown'
    >>> mascot2.sing_song("Goodbye, Moscow!")
    "Mishka sings 'Goodbye, Moscow!' at Olympic Games"
    >>> mascot2.change_nickname("The Olympic Mishka")
    >>> mascot2.nickname
    'The Olympic Mishka'
    """
    brings = 'Luck'
    
    # Initializer (Constructor) / Instance Attributes
    def __init__(self, color, nickname, event):
        self.color = color
        self.nickname = nickname
        self.event = event

    def sing_song(self, song):
        return self.nickname + " sings '" + song + "' at Olympic Games"

    def change_nickname (self, new_name):
        self.nickname = new_name


# Question 2

class Winter_Olympics:
    """
    Creates a class with 1 class attribute and two class methods

    >>> Winter_Olympics.mascot
    'Bing Dwen Dwen'
    >>> Winter_Olympics.starts()
    'Friday, February 4'
    >>> Winter_Olympics.ends()
    'Sunday, February 20'
    """

    # YOUR CODE GOES HERE #

    mascot = 'Bing Dwen Dwen'

    def starts():
        return 'Friday, February 4'

    def ends():
        return 'Sunday, February 20'
# Question 3

class Phone:
    """
    Creates a Phone class 3 instance attributes (brand, battery,
    storage) passed to the constructor. Then add 5 more attributes
    (charge, drain_rate,charge_rate, num_apps, apps), derived from the
    three given instance attributes and 3 methods (use, recharge, install)

    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Robinhood')
    'App installed'
    >>> my_phone.apps
    {'Robinhood'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    """
    # Initializer
    def __init__(self, brand, battery, storage):
        self.brand = brand
        self.battery = battery
        self.storage = storage
        self.charge = self.battery // 2
        # Drain rate will differ based on brand
        # Create if-else structure
        self.drain_rate =10 if self.brand == 'Apple' else 12 if self.brand \
                        == 'OnePlus' else 8 if self.brand == 'Samsung' else 15
        self.charge_rate = 20
        self.num_apps = 0
        self.apps = set()

    def use(self, minutes):
        # TODO: Update charge
        self.charge = self.charge - (self.drain_rate * minutes)
        if self.charge <= 0: # Handles case when we run out of charge
            return 'Out of charge'

    def recharge(self, minutes):
        # TODO: Update charge
        self.charge = (self.charge + (self.charge_rate * minutes)) if (
                self.charge + (self.charge_rate * minutes)) <= self.battery \
            else self.battery

    def install(self, app_size, app_name):
        # Cannot install apps when we don't have charge
        if self.charge <= 0:
            return 'Out of charge'
        # Cannot install apps when we don't have sufficient storage
        if self.storage <= 0:
            return 'Not enough storage'
        # Cannot install apps that are already installed
        if app_name in self.apps:
            return 'App already installed'

        # Have dealt with all potential issues. Install app now
        # TODO: Update storage
        self.storage -= app_size
        # TODO: Update num_apps
        self.num_apps += 1
        # TODO: Update apps
        self.apps.add(app_name)
        return 'App installed'

# Question 4

def max_recursion(tup):
    """
    Returns the largest element in the tuple.

    >>> max_recursion((1,2,3,4))
    4
    >>> max_recursion((13,2,3,4))
    13
    >>> max_recursion((13,2,33,4))
    33
    """

    # Your code is here
    slicing = 2
    if len(tup) == 1:
        return tup[0]
    elif len(tup) > 1:
        if tup[0] < tup[1]:
            return max_recursion(tup[1:])
        else:
            return max_recursion((tup[0:1]) + tup[slicing:])
# Question 5

def max_or_min_recursion(tup, find_max = True):
    """
    Returns the largest or smallest element in the tuple,
    depending on the optinal parameter.

    >>> max_or_min_recursion((1,2,3,4))
    4
    >>> max_or_min_recursion((13,2,3,4), False)
    2
    >>> max_or_min_recursion((13,2,33,-4), True)
    33
    """

    # Your code is here
    slicing = 2
    if len(tup) == 1:
        return tup[0]
    elif len(tup) > 1:
        if find_max:
            if tup[0] < tup[1]:
                return max_or_min_recursion(tup[1:])
            else:
                return max_or_min_recursion((tup[0:1]) + tup[slicing:])
        else:
            if tup[0] > tup[1]:
                return max_or_min_recursion(tup[1:], False)
            else:
                return max_or_min_recursion((tup[0:1]) + tup[slicing:], False)

# Question 6

def find_winner(record, find_max=True):
    """
    
    Returns the name of the country with either largest or
    smallest score, depending on the optional parameter.

    >>> find_winner([('Germany',23),('USA', 49), ('South Korea', 32)])
    'USA'
    >>> find_winner([('China', 12.88),('Japan', 15)], find_max=False)
    'China'
    >>> find_winner([('France', 10), ('UK', 10), ('Spain', 5)], find_max=True)
    'France'
    """
    # Your code is here
    slicing = 2
    if len(record) == 1:
        return record[0][0]
    elif len(record) > 1:
        if find_max:
            if record[0][1] == record[1][1]:
                return find_winner(record[0:1] + record[slicing:])
            elif record[0][1] > record[1][1]:
                return find_winner(record[0:1] + record[slicing:])
            else:
                return find_winner(record[1:])
        else:
            if record[0][1] == record[1][1]:
                return find_winner(record[0:1] + record[slicing:])
            elif record[0][1] < record[1][1]:
                return find_winner(record[0:1] + record[slicing:], False)
            else:
                return find_winner(record[1:], False)
    # somewhere here you may want to use a call to a helper recursive function:
    # find_winner_helper(record, find_max)



# Recursive function. Think, what does it return?
# def find_winner_helper(record, find_max):
    # add your own doct tests to check correctness.


