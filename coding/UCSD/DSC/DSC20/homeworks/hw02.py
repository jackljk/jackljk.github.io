"""
DSC 20 Homework 02
Name: Jack Kai Lim
PID: A16919063
"""


# Question 1
def playlist_password(playlist_name, limit):
    """
    ############################################################## # For
    this question, I iterate through every character in the string, then I
    run through a large if/elif statement, which checks what the character
    in the string is and does the change to the poassword according. And
    through each , iteration, I check to see if the limit has been reached.
    If it has been reached, I return the password at that point else the for
    loop with keep looping until it has gone through all the characters in
    the string.# # method description and add at least 3 more doctests
    below. # ##############################################################

    >>> playlist_password("World's Best Lasagne", 10)
    'eBsd7rwost'
    >>> playlist_password('Baked Casserole', 12)
    'oraCdaBkesse'
    >>> playlist_password('Hash browns', 11)
    'orb4s4awns'

    >>> playlist_password('', 10)
    ''
    >>> playlist_password('Hi this is just a test string', 100)
    'irtstsatsisi4t4isjuteng'
    >>> playlist_password('Helloooo', 4)
    'e477'
    """
    if_l = '7'
    if_h = '4'
    password = ''
    for character in playlist_name:
        if len(password) != limit:
            if character.lower() == 'a' or character.lower() == 'e' \
                    or character.lower() == 'i' \
                    or character.lower() == 'o' or character.lower() == 'u':
                password = password + character
                password = password[::-1]
            elif character.lower() == 'd' or character.lower() == 'w' \
                    or character.lower() == 'k':
                password = password + character.lower()
            elif character.lower() == 'l':
                password = password + if_l
            elif character.lower() == 'h':
                password = password + if_h
            elif not character.isalnum():
                continue
            else:
                password = password + character
        else:
            return password
    return password


# Question 2
def cookable_recipes(ings, recipes):
    """
    ############################################################## # First I
    iterate through all the recipes in the dictionary. Then I check to see
    if the required ingredients for each of the recipes is avaliable in my
    ings(inventory). If it is I add the recipe to the output list, if not I
    pass.# # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> rec = {'Egg Fried Rice': ['egg', 'rice', 'msg'], \
'Spaghetti': ['noodle', 'tomato sauce'], 'Steamed Rice': ['rice']}
    >>> cookable_recipes(['egg', 'msg', 'rice'], rec)
    ['Egg Fried Rice', 'Steamed Rice']
    >>> cookable_recipes(['egg', 'rice', 'msg', 'noodle', 'tomato sauce'], rec)
    ['Egg Fried Rice', 'Spaghetti', 'Steamed Rice']
    >>> cookable_recipes(['egg'], rec)
    []

    >>> cookable_recipes(['egg', 'rice', 'msg', 'noodle', 'tomato-sauce'], rec)
    ['Egg Fried Rice', 'Steamed Rice']
    >>> rec2 = {'Egg Fried Rice': ['egg', 'rice', 'msg'], \
'Boiling Water': ['water'] ,'Spaghetti': ['noodle', 'tomato sauce'], \
'Steamed Rice': ['rice']}
    >>> cookable_recipes(['egg', 'msg','tomato-sauce'], rec2)
    []
    >>> cookable_recipes(['water'], rec2)
    ['Boiling Water']
    """
    lst = []
    for food, req_ings in recipes.items():
        if all(ing in ings for ing in req_ings):
            lst.append(food)
    return lst


# Question 3
# Part 1
def process_purchase(purchase):
    """
    ############################################################## # First I
    iterate through the list to get all the stores stored as keys in a
    dictionary. Then next i iterate through the list and add all itens to
    the list to its related store.# # method description and add at least 3
    more doctests below. #
    ##############################################################

    >>> process_purchase([('rice', 'mitsuwa'), ('msg', '99ranch'), \
('eggs', 'costco')])
    {'mitsuwa': ['rice'], '99ranch': ['msg'], 'costco': ['eggs']}
    >>> process_purchase([('milk', 'ralphs'), ('carrot', 'ralphs'), \
('milk', 'ralphs'), ('carrot', 'costco')])
    {'ralphs': ['milk', 'carrot', 'milk'], 'costco': ['carrot']}

    >>> process_purchase([])
    {}
    >>> process_purchase([('rice', 'mitsuwa'), ('msg', '99ranch'), \
('eggs', 'costco'),('milk', 'ralphs'), ('carrot', 'ralphs'), \
('milk', 'ralphs'), ('carrot', 'costco')])
    {'mitsuwa': ['rice'], '99ranch': ['msg'], 'costco': ['eggs', 'carrot'], \
'ralphs': ['milk', 'carrot', 'milk']}
    >>> process_purchase([('milk', 'ralphs'), ('milk', 'ralphs'), \
    ('milk', 'ralphs'), ('milk', 'ralphs'),\
    ('milk', 'ralphs'), ('milk', 'ralphs')])
    {'ralphs': ['milk', 'milk', 'milk', 'milk', 'milk', 'milk']}
    """
    d = {}
    for p in purchase:
        if p[1] in d:
            pass
        else:
            d[p[1]] = []
    for p in purchase:
        d[p[1]].append(p[0])
    return d


# Part 2
def grocery_summary(grocery_purchases):
    """
    ############################################################## # First I
    iterate through the list of dictionaries. in each iteration, I iterate
    through the store(key) and item(list of items bought from the store) in
    the dictionary. Then I add the stores as the keys to a new dictionary
    and then I iterate through the list of bought items and check if the
    item already exist in the list or not. If it is new I add it if it is
    not I don't add it.# # method description and add at least 3 more
    doctests below. #
    ##############################################################

    >>> p1 = [{'mitsuwa': ['rice'], '99ranch': ['msg']}, \
{'99ranch': ['sambal', 'banana leaf'], 'costco': ['eggs']}]
    >>> grocery_summary(p1)
    {'mitsuwa': ['rice'], '99ranch': ['msg', 'sambal', 'banana leaf'], \
'costco': ['eggs']}
    >>> p2 = [{'ralphs': ['milk', 'carrot', 'milk'], 'costco': ['carrot']}, \
{'ralphs': ['carrot', 'carrot', 'milk'], 'costco': ['carrot']}]
    >>> grocery_summary(p2)
    {'ralphs': ['milk', 'carrot'], 'costco': ['carrot']}

    # Add at least 3 doctests below here #

    """
    d = {}
    for purchases in grocery_purchases:
        for store, items in purchases.items():
            if store not in d.keys():
                d[store] = []
            for item in items:
                if item not in d[store]:
                    d[store].append(item)

    return d


# Question 4
def channel_stats(videos_stats):
    """
    ############################################################## # First I
    iterate through the list of lists. Then add the according statistic to a
    variable each. Then return everything as a list of tuples.# # method
    description and add at least 3 more doctests below. #
    ##############################################################

    >>> channel_stats ([[123, 231, 82, 430], [340, 158, 225, 647]])
    [('likes', 463), ('dislikes', 389), ('comments', 307), ('views', 1077)]
    >>> channel_stats([[865, 342, 205, 230]])
    [('likes', 865), ('dislikes', 342), ('comments', 205), ('views', 230)]
    >>> channel_stats([[954, 234, 235, 2035], [1040, 350, 394, 2500], \
[70, 43, 23, 230]])
    [('likes', 2064), ('dislikes', 627), ('comments', 652), ('views', 4765)]

    # Add at least 3 doctests below here #
    """
    likes, likes_pos = 0, 0
    dislikes, dislikes_pos = 0, 1
    comments, comments_pos = 0, 2
    views, views_pos = 0, 3
    for stats in videos_stats:
        likes += stats[likes_pos]
        dislikes += stats[dislikes_pos]
        comments += stats[comments_pos]
        views += stats[views_pos]
    lst = [('likes', likes), ('dislikes', dislikes), ('comments', comments),
           ('views', views)]
    return lst


# Question 5
# Part 1
def parse_file(filepath):
    """
    ############################################################## # I open
    the file 2 times as I am gioing to iterate through the lines twice.
    First time, I add all the unique keys, in the form of a list with the
    username and user id. The other time, I compare the key and if they
    match, I add the total view time to the value for that dictionary key.#
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> parse_file('files/viewer1.txt')
    {('marina', 1): [15, 10], ('elvy', 2): [8]}
    >>> parse_file('files/viewer2.txt')
    {('marina', 10): [65, 20], ('elvy', 4): [10, 60, 30], ('colin', 6): [90]}
    >>> parse_file('files/empty.txt')
    {}

    >>> parse_file('files/viewer3.txt')
    {('marina', 10): [0]}
    >>> parse_file('files/viewer4.txt')
    {('marina', 10): [65, 20, 0], ('elvy', 4): [10, 60, 30], \
('colin', 6): [90], ('marina', 1): [15, 10], ('elvy', 2): [8]}
    >>> parse_file('files/viewer5.txt')
    {('marina', 1): [15, 10, 5, 5, 10, 20]}
    """
    d = {}
    txt_file = open(filepath, 'r')
    txt_file2 = open(filepath, 'r')
    for line in txt_file:
        username, user_id, view_start, view_end = line.split(',')
        d[username, int(user_id)] = []
    for line in txt_file2:
        username, user_id, view_start, view_end = line.split(',')
        d[username, int(user_id)].append(int(view_end) - int(view_start))
    txt_file.close()
    txt_file2.close()
    return d


# Part 2
def long_views(filepath, threshold):
    """
    ############################################################## # First I
    open the filepath, then I create a new file path with '_modified'. Then
    I iterate through each line in the file and calculate the length viewed
    by the viewer. Which I then check if it is more than the threshold. If
    it is I write to the file the user id and Yes. Else, I write out the
    user id and No making sure to add a new line each time as well.# #
    method description and add at least 3 more doctests below. #
    ##############################################################

    >>> long_views('files/viewer1.txt', 10)
    >>> with open('files/viewer1_modified.txt', 'r') as outfile1:
    ...     print(outfile1.read().strip())
    1,Yes
    2,No
    1,Yes

    >>> long_views('files/viewer2.txt', 40)
    >>> with open('files/viewer2_modified.txt', 'r') as outfile2:
    ...     print(outfile2.read().strip())
    10,Yes
    4,No
    4,Yes
    10,No
    6,Yes
    4,No

    >>> long_views('files/empty.txt', 10)
    >>> with open('files/empty_modified.txt', 'r') as outfile3:
    ...     print(outfile3.read().strip())
    <BLANKLINE>
    >>> long_views('files/viewer3.txt', 40)
    >>> with open('files/viewer3_modified.txt', 'r') as outfile4:
    ...     print(outfile4.read().strip())
    10,No
    >>> long_views('files/viewer4.txt', 40)
    >>> with open('files/viewer4_modified.txt', 'r') as outfile5:
    ...     print(outfile5.read().strip())
    10,Yes
    4,No
    4,Yes
    10,No
    6,Yes
    4,No
    10,No
    1,No
    2,No
    1,No
    """
    txt_file = open(filepath, 'r')
    filepath_cut = filepath.strip('.txt')
    mod_file = open(filepath_cut + '_modified.txt', 'w')
    for line in txt_file:
        username, user_id, view_start, view_end = line.split(',')
        view_length = int(view_end) - int(view_start)
        if view_length >= threshold:
            mod_file.write(user_id + ',Yes\n')
        else:
            mod_file.write(user_id + ',No\n')


# Part 3
def compare_subscribe(data, subscriber):
    """
    ############################################################## # First I
    iterate through the items in the dictionary, then I check if the viewer
    name is in the list of subcribers. If it is I iterate through the list
    of view time and add them to a sub_view variable while adding 1 to the
    count for subs. If the name is non sub I do the same thing for the non
    sub variables. Then I check if the count is 0 for sub and non sub. If it
    is 0 I return 0 as the average view time, if it is not 0 I calculate the
    avergae time for a sub/non sub. And return the values as a tuple.# #
    method description and add at least 3 more doctests below. #
    ##############################################################

    >>> data = parse_file('files/viewer1.txt')
    >>> compare_subscribe(data, ['marina'])
    (12, 8)
    >>> compare_subscribe(data, ['marina', 'elvy'])
    (11, 0)
    >>> compare_subscribe(data, [])
    (0, 11)

    >>> data2 = parse_file('files/viewer2.txt')
    >>> compare_subscribe(data2, ['marina', 'colineee'])
    (42, 47)
    >>> compare_subscribe(data2, ['marina', 'colin', 'elvy'])
    (45, 0)
    >>> data3 = parse_file('files/empty.txt')
    >>> compare_subscribe(data3, ['marina'])
    (0, 0)
    """
    sub_view = 0
    count_sub = 0
    nonsub_view = 0
    count_nonsub = 0
    for viewer, view_time in data.items():
        if viewer[0] in subscriber:
            for time in view_time:
                sub_view += int(time)
                count_sub += 1
        else:
            for time in view_time:
                nonsub_view += int(time)
                count_nonsub += 1

    if count_sub == 0:
        avg_sub = 0
    else:
        avg_sub = int(sub_view / count_sub)
    if count_nonsub == 0:
        avg_nonsub = 0
    else:
        avg_nonsub = int(nonsub_view / count_nonsub)
    return (avg_sub, avg_nonsub)
