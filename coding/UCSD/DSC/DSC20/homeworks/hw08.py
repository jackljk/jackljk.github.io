"""
DSC 20 Homework 08
Name: Jack Kai Lim
PID:  A16919063
"""


# Question 1
def from_list_to_dict(lst):
    """
    >>> lst = [(1,2),(3,4),(5,6)]
    >>> from_list_to_dict(lst)
    {1: 2, 3: 4, 5: 6}

    >>> lst = [("one",1),("two",2)]
    >>> from_list_to_dict(lst)
    {'one': 1, 'two': 2}

    >>> lst = []
    >>> from_list_to_dict(lst)
    {}

    # Add at least 3 doctests below #
    >>> lst = [(True, 12), (False, 'lol')]
    >>> from_list_to_dict(lst)
    {True: 12, False: 'lol'}
    >>> lst = [(1,2),(3,4),(5,6), ("one",1),("two",2)]
    >>> from_list_to_dict(lst)
    {1: 2, 3: 4, 5: 6, 'one': 1, 'two': 2}
    >>> lst = [('f', 'p'), (12, 147216846), (True, False)]
    >>> from_list_to_dict(lst)
    {'f': 'p', 12: 147216846, True: False}
    >>> lst = [(1, 2), (1, 4)]
    >>> from_list_to_dict(lst)
    {1: 4}
    """
    if len(lst) == 0:
        return {}
    elif len(lst) == 1:
        return {lst[0][0]: lst[0][1]}
    else:
        return {lst[0][0]: lst[0][1]} | from_list_to_dict(lst[1:])


# Question 2
def make_two_dicts(str1, str2, key1, key2):
    """
    >>> s1 = "abc"
    >>> s2 = "abd"
    >>> make_two_dicts(s1, s2, "k1", "k2")
    {'k1': ['b', 'a'], 'k2': ['c']}

    >>> s1 = "abcd"
    >>> s2 = "hijkl"
    >>> make_two_dicts(s1, s2, "k1", "k2")
    {'k1': [], 'k2': ['d', 'c', 'b', 'a']}

    >>> s1 = "marina"
    >>> s2 = "langlois"
    >>> make_two_dicts(s1, s2, "key1", "key2")
    {'key1': ['a', 'n', 'i', 'a'], 'key2': ['r', 'm']}

    # Add at least 3 doctests below #
    >>> s1 = "Uncle Roger"
    >>> s2 = "Haiyah"
    >>> make_two_dicts(s1, s2, 'msg', 'no')
    {'msg': [], 'no': ['r', 'e', 'g', 'o', 'R', ' ', 'e', 'l', 'c', 'n', 'U']}

    >>> s1 = "?lo) "
    >>> s2 = ")? "
    >>> make_two_dicts(s1, s2, 'symbols', 'everything else')
    {'symbols': [' ', ')', '?'], 'everything else': ['o', 'l']}
    >>> s1 = 'Jack Kai Lim 20'
    >>> s2 = "I love DSC20"
    >>> make_two_dicts(s1, s2, 'shared', 'Not shared')
    {'shared': ['0', '2', ' ', ' ', ' '], \
'Not shared': ['m', 'i', 'L', 'i', 'a', 'K', 'k', 'c', 'a', 'J']}
    """

    def recursion(str1, str2, lst1, lst2):
        if len(str1) == 1:
            if str1[0] in str2:
                return [str1[0]] + lst1, lst2
            else:
                return lst1, [str1[0]] + lst2
        else:
            if str1[0] in str2:
                return recursion(str1[1:], str2, [str1[0]] + lst1, lst2)
            else:
                return recursion(str1[1:], str2, lst1, [str1[0]] + lst2)



    return {key1: recursion(str1, str2, [], [])[0], \
            key2: recursion(str1, str2, [], [])[1]}


# Question 3
def dict_decompose(d):
    """
    >>> d={"M,L":["DSC20", "DSC30"], "A,B":["DSC20", "DSC30"], \
    "C,D":["DSC20", "DSC10"]}
    >>> l1, l2 = dict_decompose(d)
    >>> l1.sort()
    >>> l1
    ['A,B', 'C,D', 'M,L']
    >>> l2.sort()
    >>> l2
    ['DSC10', 'DSC20', 'DSC30']

    >>> d = {1:[1,2,3], 2:[3,4,5], 3:[]}
    >>> l1, l2 = dict_decompose(d)
    >>> l1.sort()
    >>> l1
    [1, 2, 3]
    >>> l2.sort()
    >>> l2
    [1, 2, 3, 4, 5]

    # Add at least 3 doctests below #
    >>> d = {True: [1, 2, 3], False: [4, 5, 6]}
    >>> test1, test2 = dict_decompose(d)
    >>> test1.sort()
    >>> test1
    [False, True]
    >>> test2.sort()
    >>> test2
    [1, 2, 3, 4, 5, 6]

    >>> d2 = {'Uncle Roger': ['Rice', 'egg'], 'Haiyah': ['egg']}
    >>> b1, b2 = dict_decompose(d2)
    >>> b1.sort()
    >>> b1
    ['Haiyah', 'Uncle Roger']
    >>> b2.sort()
    >>> b2
    ['Rice', 'egg']

    >>> d3 = {False: [], 1: []}
    >>> a1, a2 = dict_decompose(d3)
    >>> a1.sort()
    >>> a1
    [False, 1]
    >>> a2.sort()
    >>> a2
    []
    """



    values = list(d.values())

    def rec1(v):
        if len(v) == 0:
            return []
        elif len(v) == 1:
             return v[0]
        else:
            return list(set(v[0] + rec1(v[1:])))




    def rec2(d):
        keys = list(d.keys())
        if len(keys) == 1:
            return [keys[0]]
        else:
            d.pop(keys[0])
            return [keys[0]] + rec2(d)

    l1 = rec1(values)
    l2 = rec2(d)
    return l2, l1


# Question 4
def q4_doctests():
    """
    >>> Smurfette = Smurf(15, 500, 20, 100)
    >>> Jokey = Common_Smurf(20, 300, 15, 150)
    >>> papa_smurf = PaPa_Smurf(99, 1000, 150, 1000)
    >>> Smurfette.grow_plant(15)
    True
    >>> Smurfette.coin
    485
    >>> Smurfette.harvest(15, 35, 40)
    True
    >>> Smurfette.coin
    505
    >>> Smurfette.experience
    140
    >>> Jokey.count_level()
    'Your smurf is at level 31'
    >>> Smurfette.make_deal(Jokey, 10)
    True
    >>> Smurfette.coin
    495
    >>> Jokey.coin
    310
    >>> Jokey.make_deal(Smurfette, 200)
    True
    >>> Jokey.smurf_berry
    15
    >>> Jokey.make_deal(papa_smurf, 10)
    'Papa Smurf caught you!'
    >>> Jokey.coin
    0
    >>> papa_smurf.count_level()
    'Your smurf is at level 220'
    """
    return


class Smurf:
    """
    A class that abstracts the Smurf character of the game.
    """

    def __init__(self, age, coin, smurf_berry, experience):
        """
        Constructor of Smurf. Input validation not required
        Parameters:
            age (int): the age of a certain smurf
            coin (int): number of coin the smurf holds
            smurf_berry (int): number of smurf_berry the smurf holds
            experience (int): total experience of a certain smurf
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(age, int)
        assert age >= 0
        self.age = age
        assert isinstance(coin, int)
        assert coin >= 0
        self.coin = coin
        assert isinstance(smurf_berry, int)
        assert smurf_berry >= 0
        self.smurf_berry = smurf_berry
        assert isinstance(experience, int)
        assert experience >= 0
        self.experience = experience

    def grow_plant(self, cost):
        """
        Return a boolean based on if we are able to successfully grow
        the plant. If successful, deduct the cost of the plant from coin.
        Otherwise, return False
        """
        # YOUR CODE STARTS HERE #
        assert isinstance(cost, int)
        assert cost >= 0
        if cost > self.coin:
            return False
        else:
            self.coin -= cost
            return True

    def make_deal(self, other_smurf, val_item):
        """
        Makes a deal with another smurf for an item worth val_item amount
        of coins. If you don't have enough coins, attempt to use smurf berries.
        Return True if the deal is successful, and False otherwise.
        """
        # YOUR CODE STARTS HERE #
        if val_item > self.coin:
            if val_item > (self.smurf_berry * 10):
                return False
            else:
                val_item2 = (val_item/10 if val_item % 10 == 0 else (val_item
                                                    + (val_item % 10))/10 )
                self.smurf_berry -= val_item
                other_smurf.smurf_berry += val_item
                return True
        else:
            self.coin -= val_item
            other_smurf.coin += val_item
            return True

    def harvest(self, cost, revenue, experience):
        """
        Try to grow and harvest the plant based on the cost. If we are able
        to, increase coin and experienced based on revenue and experience,
        and return True.
        If not, return False
        """
        # YOUR CODE STARTS HERE #
        if cost > self.coin:
            return False
        else:
            self.coin -= cost
            self.coin += revenue
            self.experience += experience
            return True

    def count_level(self):
        """
        Count the level of the smurf.
        Each level is based on experience in blocks of 5
        Return the string 'Your smurf is at level x', where x is the level
        """
        # YOUR CODE STARTS HERE #
        level = str((self.experience // 5) + 1)
        return 'Your smurf is at level ' + level


class Common_Smurf(Smurf):
    """
    A class that abstracts the Common Smurf character of the game.
    """

    def make_deal(self, other_smurf, val_item):
        """
        Makes a deal with another smurf for an item worth val_item amount
        of coins.

        However, if you meet a Papa Smurf, you lose all your coins and return
        the string 'Papa Smurf caught you!'
        """
        # YOUR CODE STARTS HERE #
        if type(other_smurf) == PaPa_Smurf:
            self.coin = 0
            return 'Papa Smurf caught you!'
        else:
            return super().make_deal(other_smurf, val_item)


class PaPa_Smurf(Smurf):
    """
    A class that abstracts the Papa Smurf character of the game.
    """

    def count_level(self):
        """
        Count the level of the smurf.
        Each level is based on experience + age in blocks of 5
        Return the string 'Your smurf is at level x', where x is the level
        """
        # YOUR CODE STARTS HERE #
        level = str(((self.experience + self.age) // 5) + 1)
        return 'Your smurf is at level ' + level

# Question 5
def q5_doctests():
    """
    >>> kart_1 = Kart()
    >>> kart_2 = NormalKart()
    >>> kart_3 = CheaterKart()
    >>> kart_2.nitro(20)
    True
    >>> kart_1.attack(kart_2)
    False
    >>> kart_2.high_score()
    9100
    >>> kart_2.attack(kart_3)
    False
    >>> kart_2.speed
    30
    >>> kart_3.high_score()
    25750
    >>> kart_4 = CheaterKart()
    >>> kart_3.attack(kart_4)
    True
    >>> kart_4.size
    7
    >>> kart_4.speed
    20
    >>> kart_3.size
    8
    >>> kart_4.nitro(40)
    True
    >>> kart_4.lives
    6
    >>> kart_4.attack(kart_2)
    True
    >>> kart_4.high_score()
    24650
    >>> kart_4.size
    8
    >>> kart_2.speed
    50
    """
    return


class Kart:

    def __init__(self):
        # YOUR CODE STARTS HERE #
        self.speed = 50
        self.size = 5
        self.powerup = 3
        self.lives = 3

    def nitro(self, boost):
        # YOUR CODE STARTS HERE #
        if self.powerup == 0:
            return False
        else:
            score1 = self.high_score()
            self.speed = int(((self.speed + boost)**2 + (self.speed -
                                                         boost)**2)**0.5)
            score2 = self.high_score()
            if score1 * 2 <= score2:
                self.lives += 1
            self.powerup -= 1
            return True

    def set_speed(self, new_speed):
        # YOUR CODE STARTS HERE #
        self.speed = new_speed

    def set_lives(self, gains=True):
        # YOUR CODE STARTS HERE #
        if gains:
            self.lives += 1
        else:
            self.lives -= 1

    def set_size(self, new_size):
        # YOUR CODE STARTS HERE #
        self.size = new_size

    def attack(self, other_kart):
        # YOUR CODE STARTS HERE #

        if self.size == other_kart.size:
            return False
        elif self.size > other_kart.size:
            if other_kart.speed - 50 < 0:
                other_kart.lives -= 1
                other_kart.speed = 50
                self.size += 1
                self.speed += 50
                return True
            else:
                other_kart.speed -= 50
                self.speed += 50
                return True
        else:
            if self.speed - 50 < 0:
                self.lives -= 1
                self.speed = 50
                other_kart.size += 1
                other_kart.speed += 50
                return False
            else:
                self.speed -= 50
                other_kart.speed += 50
                return False


    def high_score(self):
        # YOUR CODE STARTS HERE #
        score = self.speed * 100 + self.lives * 500
        return score


class NormalKart(Kart):

    def attack(self, other_kart):
        # YOUR CODE STARTS HERE #
        if type(other_kart) == CheaterKart:
            if self.size == other_kart.size:
                return False
            elif self.size > other_kart.size:
                if other_kart.speed - 50 < 0:
                    other_kart.lives -= 1
                    other_kart.speed = 50
                    self.size += 1
                    self.speed += 50
                    return True
                else:
                    other_kart.speed -= 50
                    self.speed += 50
                    return True
            else:
                self.speed = 30
                self.lives -= 1
                other_kart.speed += 50
                other_kart.size += 1
                return False
        else:
            super().attack(other_kart)




class CheaterKart(Kart):

    def __init__(self):
        # YOUR CODE STARTS HERE #
        self.speed = 70
        self.size = 7
        self.powerup = 5
        self.lives = 5

    def high_score(self):
        # YOUR CODE STARTS HERE #
        score = self.speed * 200 + self.lives * 300 + 250
        return score
