from deck import Deck
from hand import DealerHand, PlayerHand
from card import Card

# don't change these imports
from numpy.random import randint, seed

seed(20)


class Blackjack:
    """
    Game of blackjack!

    # Removes the game summaries from the previous doctest run
    >>> from os import remove, listdir
    >>> for f in listdir("game_summaries"):
    ...    remove("game_summaries/" + f)

    #######################################
    ### Doctests for calculate_score() ####
    #######################################
    >>> card_1 = Card("A", "diamonds")
    >>> card_2 = Card("J", "spades")
    >>> hand_1 = PlayerHand()
    >>> Blackjack.calculate_score(hand_1)
    0
    >>> hand_1.add_card(card_1)
    >>> Blackjack.calculate_score(hand_1) # (Ace)
    11
    >>> hand_1.add_card(card_2)
    >>> Blackjack.calculate_score(hand_1) # (Ace, Jack)
    21

    >>> card_3 = Card("A", "spades")
    >>> hand_2 = PlayerHand()
    >>> hand_2.add_card(card_1, card_3)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace)
    12
    >>> hand_2.add_card(card_2)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace, Jack)
    12

    >>> hand_3 = PlayerHand()
    >>> card_4 = Card(2, "spades")
    >>> card_5 = Card(4, "spades")
    >>> hand_3.add_card(card_4, card_5)
    >>> Blackjack.calculate_score(hand_3)
    6

    #######################################
    ### Doctests for determine_winner() ####
    #######################################
    >>> blackjack = Blackjack(10)
    >>> blackjack.determine_winner(10, 12)
    -1
    >>> blackjack.determine_winner(21, 21)
    0
    >>> blackjack.determine_winner(22, 23)
    0
    >>> blackjack.determine_winner(12, 2)
    1
    >>> blackjack.determine_winner(22, 2)
    -1
    >>> blackjack.determine_winner(2, 22)
    1
    >>> print(blackjack.get_log())
    Player lost with a score of 10. Dealer won with a score of 12.
    Player and Dealer tie.
    Player and Dealer tie.
    Player won with a score of 12. Dealer lost with a score of 2.
    Player lost with a score of 22. Dealer won with a score of 2.
    Player won with a score of 2. Dealer lost with a score of 22.
    <BLANKLINE>  
    >>> blackjack.reset_log()

    #######################################
    ### Doctests for play_round() #########
    #######################################
    >>> blackjack_2 = Blackjack(10)
    >>> blackjack_2.play_round(1, 15)
    >>> print(blackjack_2.get_log())
    Round 1 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (10, clubs) (A, clubs)
    Dealer Cards: (Q, clubs) (?, ?)
    Dealer Cards Revealed: (7, diamonds) (Q, clubs)
    Player won with a score of 21. Dealer lost with a score of 17.
    <BLANKLINE>
    >>> blackjack_2.reset_log()
   
    >>> blackjack_2.play_round(3, 21)
    >>> print(blackjack_2.get_log())
    Round 2 of Blackjack!
    wallet: 15
    bet: 5
    Player Cards: (4, clubs) (7, clubs)
    Dealer Cards: (A, hearts) (?, ?)
    Player pulled a (J, hearts)
    Dealer Cards Revealed: (5, clubs) (A, hearts)
    Dealer pulled a (6, clubs)
    Dealer pulled a (2, clubs)
    Dealer pulled a (8, clubs)
    Player won with a score of 21. Dealer lost with a score of 22.
    Round 3 of Blackjack!
    wallet: 20
    bet: 10
    Player Cards: (6, hearts) (9, diamonds)
    Dealer Cards: (K, hearts) (?, ?)
    Player pulled a (Q, hearts)
    Dealer Cards Revealed: (J, diamonds) (K, hearts)
    Player lost with a score of 25. Dealer won with a score of 20.
    Round 4 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (5, diamonds) (10, diamonds)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, diamonds)
    Player pulled a (7, spades)
    Dealer Cards Revealed: (2, diamonds) (2, hearts)
    Dealer pulled a (K, spades)
    Dealer pulled a (3, spades)
    Player lost with a score of 25. Dealer won with a score of 17.
    <BLANKLINE>
    
    >>> with open("game_summaries/game_summary2.txt", encoding = 'utf-8') as f:
    ...     lines = f.readlines()
    ...     print("".join(lines[10:26]))
    Dealer Hand:
    ____
    |7  |
    | ♦ |
    |__7|
    ____
    |Q  |
    | ♣ |
    |__Q|
    Winner of ROUND 1: Player
    <BLANKLINE>
    ROUND 2:
    Player Hand:
    ____
    |4  |
    | ♣ |
    <BLANKLINE>

    >>> blackjack_3 = Blackjack(5)
    >>> blackjack_3.play_round(5, 21)
    >>> print(blackjack_3.get_log())
    Round 1 of Blackjack!
    wallet: 5
    bet: 5
    Player Cards: (2, clubs) (2, hearts)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, clubs)
    Player pulled a (3, diamonds)
    Player pulled a (3, hearts)
    Player pulled a (3, spades)
    Player pulled a (4, clubs)
    Player pulled a (4, diamonds)
    Dealer Cards Revealed: (2, diamonds) (2, spades)
    Dealer pulled a (4, hearts)
    Dealer pulled a (4, spades)
    Dealer pulled a (5, clubs)
    Player lost with a score of 24. Dealer won with a score of 17.
    Wallet amount $0 is less than bet amount $5.

    >>> blackjack_4 = Blackjack(500)
    >>> blackjack_4.play_round(13, 21) # At least 52 cards will be dealt
    >>> blackjack_4.reset_log()
    >>> blackjack_4.play_round(1, 17)
    >>> print(blackjack_4.get_log())
    Not enough cards for a game.
    """

    # Class Attribute(s)
    game = 0
    starting_bet = 5
    def __init__(self, wallet):
        # Initialize instance attributes
        # auto-increment as needed
        ...
        self.deck = Deck()
        assert isinstance(wallet, (int, float))
        self.wallet = wallet
        self.game_increment = 0
        self.log = ''
        Blackjack.game += 1
        self.bet = Blackjack.starting_bet

    def play_round(self, num_rounds, stand_threshold):
        """
        Plays `num_rounds` Blackjack rounds.

        Parameters:
            num_rounds (int): Number of rounds to play.
            stand_threshold (int): Score threshold for when the player
            will stand (ie player stands if they have a score >=
            this threshold)
        """
        # This could get pretty long!
        assert isinstance(num_rounds, int)
        assert isinstance(stand_threshold, int)
        bet = 5
        min_no_cards = 4
        ran_max = 6
        dealer_st = 17
        bet_increment = 5
        for i in range(num_rounds):
            if len(self.deck.cards) < min_no_cards:
                self.log = self.log + "Not enough cards for a game."
                break
            if self.wallet >= bet:
                self.log = self.log + 'Round ' + str(self.game_increment + 1) + \
                       ' of ' \
                                                              'Blackjack!\n'
            if self.wallet < bet:
                self.log = self.log + "Wallet amount $" + str(self.wallet) + \
                " is less than bet amount $" + str(Blackjack.starting_bet) + "."
                break
            else:
                self.log = self.log + 'wallet: ' + str(self.wallet) + \
                           '\nbet: ' + str(bet) + '\n'

            self.deck.shuffle(mongean= randint(0,ran_max),
                              modified_overhand = randint(0,ran_max))

            player = PlayerHand()
            dealer = DealerHand()
            self.deck.deal_hand(player)
            self.deck.deal_hand(dealer)
            self.deck.deal_hand(player)
            self.deck.deal_hand(dealer)
            self.log = self.log + 'Player Cards: ' + player.__repr__() + '\n'
            self.log = self.log + 'Dealer Cards: ' + dealer.__repr__() + '\n'
            self.hit_or_stand(player, stand_threshold)
            dealer.reveal_hand()
            self.log = self.log + 'Dealer Cards Revealed: ' + \
                       dealer.__repr__() + '\n'
            self.hit_or_stand(dealer, dealer_st)
            p_score = Blackjack.calculate_score(player)
            d_score = Blackjack.calculate_score(dealer)
            winner = self.determine_winner(p_score, d_score)
            if winner == 1:
                self.wallet += bet
                bet += bet_increment
            elif winner == -1:
                self.wallet -= bet
                if bet > Blackjack.starting_bet:
                    bet -= bet_increment
            self.game_increment += 1
            self.add_to_file(player, dealer, winner)

    def calculate_score(hand):
        """
        Calculates the score of a given hand. 

        Sums up the ranks of each card in a hand. Jacks, Queens, and Kings
        have a value of 10 and Aces have a value of 1 or 11. The value of each
        Ace card is dependent on which value would bring the score closer
        (but not over) 21. 

        Should be solved using list comprehension and map/filter. No explicit
        for loops.

        Parameters:
            hand: The hand to calculate the score of.
        Returns:
            The best score as an integer value.
        """
        ...
        pic_val = 10
        aces = 11
        assert isinstance(hand, (PlayerHand, DealerHand))
        cards = hand.get_cards()
        cards = [c.get_rank() for c in cards]
        cards1 = [v if isinstance(v, int) else pic_val if v in ['J', 'Q',
                                                'K'] else 1 for v in cards]
        total = sum(cards1)
        if 'A' in cards:
            if total <= aces:
                total += pic_val

        return total

    def determine_winner(self, player_score, dealer_score):
        """
        Determine whether the Blackjack round ended with a tie, dealer winning, 
        or player winning. Update the log to include the winner and
        their scores before returning.

        Returns:
            1 if the player won, 0 if it is a tie, and -1 if the dealer won
        """
        ...
        bj_max = 21
        if player_score == dealer_score or\
            (dealer_score > bj_max and player_score > bj_max):
            self.log = self.log + 'Player and Dealer tie.\n'
            return 0
        elif (player_score > bj_max and dealer_score < bj_max) or (
                dealer_score > \
                player_score and dealer_score < bj_max):
            self.log = self.log + 'Player lost with a score of ' + str(
                player_score) + '. Dealer won with a score of ' + str(
                dealer_score) + '.\n'
            return -1
        elif (player_score <= bj_max and dealer_score > bj_max) or (
                player_score > dealer_score):
            self.log = self.log + 'Player won with a score of ' + str(
                player_score) + '. Dealer lost with a score of ' + str(
                dealer_score) + '.\n'
            return 1




    def hit_or_stand(self, hand, stand_threshold):
        """
        Deals cards to hand until the hand score has reached or surpassed
        the `stand_threshold`. Updates the log everytime a card is pulled.

        Parameters:
            hand: The hand the deal the cards to depending on its score.
            stand_threshold: Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold).
        """
        ...
        if not isinstance(hand, DealerHand):
            while Blackjack.calculate_score(hand) < stand_threshold:
                if len(self.deck.cards) == 0:
                    break
                self.log = self.log + 'Player pulled a ' + \
                           self.deck.get_cards()[0].__repr__() + '\n'
                self.deck.deal_hand(hand)

        else:
            while Blackjack.calculate_score(hand) < stand_threshold:
                if len(self.deck.cards) == 0:
                    break
                self.log = self.log + 'Dealer pulled a ' + \
                           self.deck.get_cards()[0].__repr__() + '\n'
                self.deck.deal_hand(hand)

    def get_log(self):
        ...
        return self.log

    def reset_log(self):
        ...
        self.log = ''

    def add_to_file(self, player_hand, dealer_hand, result):
        """
        Writes the summary and outcome of a round of Blackjack to the 
        corresponding .txt file. This file should be named game_summaryX.txt
        where X is the game number and it should be in `game_summaries` 
        directory.
        """

        # Remember to use encoding = "utf-8" 
        ...
        with open('game_summaries/game_summary{}.txt'.format(Blackjack.game),
                  'a',
                  encoding= "utf-8") as file:
                file.write('ROUND ' + str(self.game_increment) + ':\nPlayer '
                                                             'Hand:\n')
                x = [str(c) for c in player_hand.get_cards()]
                for card in x:
                    file.write(card + '\n')
                file.write('Dealer Hand:\n')
                y = [str(c) for c in dealer_hand.get_cards()]
                for card in y:
                    file.write(card + '\n')
                if result == 1:
                    file.write('Winner of ROUND ' + str(self.game_increment) +
                               ': Player\n\n')
                elif result == 0:
                    file.write('Winner of ROUND ' + str(self.game_increment) +
                               ': tie\n\n')
                elif result == -1:
                    file.write('Winner of ROUND ' + str(self.game_increment) +
                               ': Dealer\n\n')
