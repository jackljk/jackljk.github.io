"""
DSC 20 Lab 02
Name: Jack Kai Lim
PID: A16919063
"""

# Question 1
def pick_username(names):
    """
    >>> pick_username(["JonaThan TanoTo", "WeiYue Li"])
    'JonaThan TanoTo'
    >>> pick_username(["JonaThan TanoTo", "WeiYue Li", "ShuBham KauShal"])
    'ShuBham KauShal'
    >>> pick_username(["JonaThan TanoTo", "WeiYue Li", \
"ShuBham KauShal", "MARINA"])
    'MARINA'
    """
    count = 0
    final_count = 0
    name_index = 0
    for i, name in enumerate(names):
        for letter in name:
            if letter.isupper() == True:
                count += 1
        if final_count < count:
            final_count = count
            count = 0
            name_index = i
        elif final_count == count:
            count = 0
            name_index = i
        else:
            count = 0


    return names[name_index]


# Question 2
def username_2(names):
    """
    >>> username_2(["", "Marina"])
    "uncle roger's biggest fan"
    >>> username_2(["LaiCaiJDanHenRoLu", "JJ~", "Chilli Jam Haiyah"])
    'hilli Jam Haiya'
    >>> username_2(["TUTU", "QIQI", "CECE"])
    'EC'
    """
    count = 0
    name = "uncle roger's biggest fan"
    while count != len(names):
        if len(names[count]) < 3:
            break
        else:
            name = names[count][1:len(names[count]) - 1]
            count += 1

    return name


# Question 3
def replace_text(text, target, desired):
    """
    >>> replace_text("Fuiyoh, this Lab is short! We love it!", "Lie", "Haiyah")
    'FUIYOH, THIS LAB IS SHORT! WE LOVE IT!'
    >>> replace_text("Chilli Jam is the king of flavor. " + \
"We love Chilli Jam. Chilli Jam makes everything better", "Chilli Jam", "MSG")
    'MSG is the king of flavor. We love Chilli Jam. MSG makes everything better'
    >>> replace_text("I put my leg down from chair,", '', ' Haiyah! ')
    ' Haiyah! I put my leg down from chair, Haiyah! '
    """
    text = text
    if text.find(target) != -1:
        text = text.replace(target, desired, 1)
        last = text.rfind(target)
        text2 = text[last:len(text)]
        text2 = text2.replace(target, desired, 1)
        text = text[0:last] + text2
    else:
        text = text.upper()
    return text


# Question 4
def convert_password(pass_dict):
    """
    >>> convert_password({'Hu': 5, 'aO': -2, '15': 3})
    'HuHuHuHuHu****151515'
    >>> convert_password({'1': 3, 'mar': 0, 'ker': -1})
    '111.***'
    >>> convert_password({'hellO': 4, '2': -7, 'end': 2})
    'hellOhellOhellOhellO*******endend'
    >>> convert_password({})
    ''
    """
    password = ''
    for key, value in pass_dict.items():
        if value < 0:
            password = password + str('*'*abs(value)*len(key))
        elif value == 0:
            password = password + '.'
        else:
            password = password + str(key*value)


    return password


# Question 5
def most_damage_taken(input_dict):
    """
    >>> most_damage_taken({'Larry': ['Jonathan', 'Marina', 'Theo'], \
'Marina': ['Larry', 'Theo'], 'Jonathan': ['Marina', 'Theo'], \
'Theo': []})
    'Theo'
    >>> most_damage_taken({'Marina': ['Shubham', 'Shubham', 'Kent'], \
'Kent': ['Marina', 'Marina', 'Marina', 'Shubham'], \
'Shubham': ['Kent', 'Marina']})
    'Marina'
    >>> most_damage_taken({'Jonathan': [], 'Larry': ['Jonathan']})
    'Jonathan'
    >>> most_damage_taken({})
    """
    if len(input_dict) == 0:
        return None
    dmg_dict = {}
    for key in input_dict:
        dmg_dict[key] = 0
    for players in input_dict.values():
        for player in players:
            dmg_dict[player] += 1

    return max(dmg_dict, key=dmg_dict.get)
