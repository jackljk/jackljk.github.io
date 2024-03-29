#1

def cat():
    s =     " /\\_/\\" +"\n"
    s = s + "( o.o )" + "\n"
    s = s + " > ^ < " +"\n" 
    return s

def dog():
    s =     "    / \\__" + "\n"
    s = s + "   (    @\\___" + "\n"
    s = s+  "  /         O" + "\n"
    s = s+  " /   (_____/" + "\n"
    s = s + "/_____/"      + "\n"
    return s

def rabbit():
    s =      " __    __" + "\n"
    s = s +  "/ \\\\..// \\" + "\n"
    s = s +  "  ( oo ) " + "\n"
    s = s +  "   \\__/"+"\n"
    return s

class Pets:
    """
    >>> cat1 = Pets("cat", "Fluffy", 4, "F")
    >>> cat2 = Pets("cat", "Buffy", 5, "M")
    >>> print(cat1)
    Fluffy
    <BLANKLINE>
     /\\_/\\
    ( o.o )
     > ^ < 
    <BLANKLINE>

    >>> cat1 < cat2
    True
    >>> cat1 == cat2
    False
    >>> cat1 > cat2
    False
    >>> cat1
    'Animal's type': cat
    'Animal's name': Fluffy
    'Animal's age': 4
    >>> cat3 = cat1 + cat2
    >>> cat3.pet_type
    'cat'
    >>> cat3.name
    'Fy'
    >>> cat3.age
    0
    >>> cat3.gender
    'F'
    """

    ascii_art = {"cat": cat(), "dog": dog(), "rabbit": rabbit()}

    def __init__(self, pet_type, name, age, gender):

        # YOUR CODE STARTS HERE #
        assert isinstance(pet_type, str)
        assert pet_type in ['cat', 'dog', 'rabbit']
        self.pet_type = pet_type
        assert isinstance(name, str)
        self.name = name
        assert isinstance(age,int)
        assert age >= 0
        self.age = age
        assert isinstance(gender, str)
        assert gender in ['F', 'M']
        self.gender = gender


    def __str__ (self):
        # YOUR CODE STARTS HERE #
        if self.pet_type == 'cat':
            return self.name + '\n\n' + cat()
        elif self.pet_type == 'dog':
            return self.name + '\n\n' + dog()
        else:
            return self.name + '\n\n' + rabbit()


    def __repr__(self):

       # YOUR CODE STARTS HERE #

        return "'Animal's type': " + self.pet_type + '\n' + "'Animal's " \
        "name': " + self.name + "\n'Animal's age': " + str(self.age)


    def __lt__(self, other):
        
        # YOUR CODE STARTS HERE #

        return self.age < other.age

    def __eq__(self, other):
        
        # YOUR CODE STARTS HERE #

        return self.age == other.age

    def __add__(self, other):
        
        # YOUR CODE STARTS HERE #
        if self.pet_type == other.pet_type:
            if self.gender != other.gender:
                name = ''
                if self.gender == 'M':
                    name = other.name[0] + self.name[-1]
                else:
                    name = self.name[0] + other.name[-1]
                return Pets(self.pet_type, name, 0, 'F')
            else:
                return "Can't add animals of different types or genders"
        else:
            return "Can't add animals of different types or genders"



#2

class Shopping_Cart():
    """
    >>> sh1 = Shopping_Cart()
    >>> sh1.add_item_to_cart("milk", 3, 4)
    >>> sh1.add_item_to_cart("eggs", 2, 2)
    >>> print(sh1.cart)
    {'milk': (3, 4), 'eggs': (2, 2)}
    >>> print(sh1)
    ['milk', 'eggs']
    >>> sh1
    ['milk', 'eggs']
    >>> sh2 = Shopping_Cart()
    >>> sh2.add_item_to_cart("milk", 5, 4)
    >>> sh3 = sh1 + sh2
    >>> print(sh3.cart)
    {'milk': (8, 4), 'eggs': (2, 2)}
    """

    def __init__(self):
        
        # YOUR CODE STARTS HERE #
        self.cart = {}


    def add_item_to_cart(self, item, weight, price_per_pound):
        
        # YOUR CODE STARTS HERE #
        assert isinstance(item, str)
        assert isinstance(weight, (int, float))
        assert weight > 0
        assert isinstance(price_per_pound, (int, float))
        assert price_per_pound > 0
        self.cart[item] = (weight, price_per_pound)


    def total(self):
        
        # YOUR CODE STARTS HERE #
        t = 0
        for t in self.cart.values():
            t += (t[0]*t[1])

        return t


    def __repr__(self):
        
        # YOUR CODE STARTS HERE #
        return str(list(self.cart.keys()))


    def __lt__(self, other):
        
        # YOUR CODE STARTS HERE #

        return self.total() < other.total()

    def __eq__(self, other):
        
        # YOUR CODE STARTS HERE #

        return self.total() == other.total()

    def __add__(self, other):

        # YOUR CODE STARTS HERE #
        new = Shopping_Cart()
        for item, t in self.cart.items():
            new.add_item_to_cart(item, t[0], t[1])

        for item, t in other.cart.items():
            if item in list(self.cart.keys()):
                new.add_item_to_cart(item, self.cart[item][0] + t[0], t[1])
        return new
