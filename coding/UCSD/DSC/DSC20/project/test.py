def modified_overhand(cards, num):
    """
    Takes `num` cards from the middle of the deck and puts them at the
    top.
    Then decrement `num` by 1 and continue the process till `num` = 0.
    When num is odd, the "extra" card is taken from the bottom of the
    top half of the deck.
    """

    # Use Recursion.
    # Note that the top of the deck is the card at index 0.

    assert isinstance(cards, list)
    assert isinstance(num, int)

    def create_middle(c_list, num):
        assert isinstance(c_list, list)
        if num == 0:
            return c_list
        elif len(c_list) % 2 == 0:
            start = (len(c_list) // 2) - 1
            if num % 2 == 0:
                start_i = start - (num // 2) + 1
                end_i = start + (num // 2) + 1
            else:
                start_i = start - (num // 2)
                end_i = start + (num // 2) + 1
        else:
            start = len(c_list) // 2
            if num % 2 == 0:
                start_i = start - (num // 2)
                end_i = start + (num // 2)
            else:
                start_i = start - (num // 2)
                end_i = start + (num // 2) + 1
        return [c_list[start_i: end_i] + \
               c_list[:start_i] + c_list[end_i:]]

    new_lst = create_middle(cards, num)
    print(new_lst)
    return modified_overhand(new_lst, num - 1)




l = [0, 1, 2, 3, 4, 5, 6, 7]

print(modified_overhand(l, 3))

