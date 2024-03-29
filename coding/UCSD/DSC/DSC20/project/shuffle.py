class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    """

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
        mid = 2
        assert isinstance(cards, list)
        assert isinstance(num, int)
        if num == 0:
            return cards
        def create_middle(c_list, num):
            assert isinstance(c_list, list)
            if num == 0:
                return c_list
            if len(c_list) % 2 == 0:
                start = (len(c_list) // 2) - 1
                if num % 2 == 0:
                    start_i = start - (num // mid) + 1
                    end_i = start + (num // mid) + 1
                else:
                    start_i = start - (num // mid)
                    end_i = start + (num // mid) + 1
            else:
                start = len(c_list) // mid
                if num % 2 == 0:
                    start_i = start - (num // mid)
                    end_i = start + (num // mid)
                else:
                    start_i = start - (num // mid)
                    end_i = start + (num // mid) + 1
            return c_list[start_i: end_i] + \
                   c_list[:start_i] + c_list[end_i:]

        new_lst = create_middle(cards, num)
        return Shuffle.modified_overhand(new_lst, num - 1)


    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores
        the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        ...
        index = 2
        s_to_l = -2
        if len(cards) % 2 == 0:
            if len(cards) == index:
                return [cards[-1]] + [cards[s_to_l]]
            else:
                return [cards[-1]] + Shuffle.mongean(cards[:s_to_l]) +\
                       [cards[-2]]
        else:
            if len(cards) == 1:
                return [cards[-1]]
            else:
                return [cards[s_to_l]] + Shuffle.mongean(cards[:s_to_l]) + \
                       [cards[-1]]