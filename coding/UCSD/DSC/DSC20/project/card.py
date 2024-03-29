class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        ...
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        assert isinstance(rank, (int, str))
        assert rank in ranks
        self.rank = rank
        assert isinstance(suit, str)
        self.suit = suit
        assert isinstance(visible, bool)
        self.visible = visible

    def __lt__(self, other_card):
        ...
        j_rank = 11
        q_rank = 12
        k_rank = 13
        a_rank = 14
        self_rank = self.rank
        if self_rank == 'J':
            self_rank = j_rank
        elif self_rank == 'Q':
            self_rank = q_rank
        elif self_rank == 'K':
            self_rank = k_rank
        elif self_rank == 'A':
            self_rank = a_rank

        other_rank = other_card.rank
        if other_rank == 'J':
            other_rank = j_rank
        elif other_rank == 'Q':
            other_rank = q_rank
        elif other_rank == 'K':
            other_rank = k_rank
        elif other_rank == 'A':
            other_rank = a_rank

        if self.rank == other_card.rank:
            return self.suit < other_card.suit
        else:
            return self_rank < other_rank

    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        ...
        suit = self.suit
        if suit == 'hearts':
            suit = '♥'
        elif suit == 'spades':
            suit = '♠'
        elif suit == 'clubs':
            suit = '♣'
        elif suit == 'diamonds':
            suit = '♦'
        if self.visible:
            return '____\n|' + str(self.rank) + '  |\n| ' \
                   + suit + ' |\n|__' + str(self.rank) + '|'
        else:
            return '____\n|' + '?' + '  |\n| ' \
                   + '?' + ' |\n|__' + '?' + '|'

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """
        ...
        if self.visible:
            return '(' + str(self.rank) + ', ' + self.suit + ')'
        else:
            return '(?, ?)'

    def get_rank(self):
        ...
        return self.rank

    def get_suit(self):
        ...
        return self.suit

    def set_visible(self, visible):
        ...
        self.visible = visible
