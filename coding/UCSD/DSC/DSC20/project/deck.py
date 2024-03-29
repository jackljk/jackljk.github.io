from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

        self.cards = [Card(i, suit) for i in ranks for suit in ['clubs',
        'diamonds', 'hearts', 'spades']]

        self.cards.sort()

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        assert all([(k == 'modified_overhand' or k == 'mongean') \
        for k in shuffle_and_count])
        assert all([isinstance(v, int) \
        for v in list(shuffle_and_count.values())])
        if 'modified_overhand' not in shuffle_and_count.keys():
            shuffle_and_count['modified_overhand'] = 0
        if 'mongean' not in shuffle_and_count.keys():
            shuffle_and_count['mongean'] = 0
        self.cards = Shuffle.modified_overhand(self.cards, \
        shuffle_and_count['modified_overhand'])
        for i in range(shuffle_and_count['mongean']):
            self.cards = \
            Shuffle.mongean(self.cards)




    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        ...
        if isinstance(hand, DealerHand):
            if not hand.visible:
                hand.add_card(self.cards[0])
                self.cards.pop(0)
            else:
                hand.add_card(self.cards[0])
                self.cards.pop(0)
        else:
            hand.add_card(self.cards[0])
            self.cards.pop(0)

    def get_cards(self):
        ...
        return self.cards