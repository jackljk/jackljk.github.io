
# Name Jack Kai Lim
# PID A16919063

# Question 1

def question_1():
    """

    1 if a method mutates an object 
    0 otherwise

    >>> answer = question_1()
    >>> len(answer)==10
    True
    >>> any([True if (i!=0 and i!=1) else False for i in answer ])
    False
    """
    
    return [0, 0, 0, 1, 1, 0, 0, 1, 0, 1]



# Question 2


def question_2():
    """

    1 if a method is in place
    0 otherwise

    >>> answer = question_2()
    >>> len(answer)==5
    True
    >>> any([True if (i!=0 and i!=1) else False for i in answer ])
    False
    """
    
    return [0, 0, 0, 1, 1]


# Question 3

def reverse_list(lst):
    """ Reverses lst in place. Make sure to NOT create
    a new array. That is, switch all the elements
    within the same array. Only switch the elements 
    in the passed list and RETURN NOTHING.
    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1]
    >>> reverse_list(x)
    >>> x
    [1]
    """

    for i in range(int(len(lst)/2)):
        n = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = n



# Question 4

def swap_lists(alist1, alist2):
    """Swaps content of two lists in place. 
    Does not return anything. 
    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]
    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]
    """

    for i in range(len(alist1)):
        alist1[i], alist2[i] = alist2[i], alist1[i]


# Question 5

def daily_inventory(store, purchases):
    """
    Updates inventory at the end of the day by removing items if nobody
    purchased or if out of stock. Otherwise updates quantity. 
    Should mutate the store dictionary. 

    >>> store = {"Roses": 5, "Tulips": 4}
    >>> purchases = {"Roses": 3} 
    >>> daily_inventory(store, purchases)
    >>> print(store)
    {'Roses': 2}

    >>> store = {"Roses": 5, "Tulips": 4}
    >>> purchases = {"Roses": 3, "Tulips": 4} 
    >>> daily_inventory(store, purchases)
    >>> print(store)
    {'Roses': 2}

    >>> store = {"Roses": 5, "Tulips": 4, "Dandelions": 10}
    >>> purchases = {"Roses": 3, "Tulips": 2, "Dandelions":7} 
    >>> daily_inventory(store, purchases)
    >>> print(store)
    {'Roses': 2, 'Tulips': 2, 'Dandelions': 3}
    """
    l = []
    for item, amount in store.items():
        if item not in purchases.keys():
            l.append(item)
        elif amount - purchases[item] == 0:
            l.append(item)

    for item in l:
        store.pop(item)


    for item, amount in store.items():
        store[item] = amount - purchases[item]


 # Question 6

def reverse_chunks(seq):
    """
    >>> lst1 = [1, 2, 3, 4, 5, 6, 7]
    >>> reverse_chunks(lst1)
    >>> lst1
    [1, 3, 2, 6, 5, 4, 7]

    >>> lst2 = [5, 6, 7, 8, 9, 10, 11]
    >>> reverse_chunks(lst2)
    >>> lst2
    [5, 7, 6, 10, 9, 8, 11]

    >>> lst3 = list(range(1, 12))
    >>> reverse_chunks(lst3)
    >>> lst3
    [1, 3, 2, 6, 5, 4, 10, 9, 8, 7, 11]

    >>> lst4 = []
    >>> reverse_chunks(lst4)
    >>> lst4
    []
    """
    chunk_size = 1
    start_value = 0
    while start_value < len(seq):
        seq[start_value:start_value + chunk_size] =\
        reversed(seq[start_value:start_value + chunk_size])
        start_value += chunk_size
        chunk_size += 1


