# Building a deck of cards as shown in week 4 of class
import random
from threading import Timer
import os

class Card:
    """ class that represents a card """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    """ class that represents a deck """
    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['spades', 'diamonds', 'clubs', 'hearts']
        self._cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self._cards)

    def show_order(self):
        for card in self._cards:
            print(card)

    def show_order_begginer(self):
        """ Only face cards reaveled """
        cards_to_memorize = []
        for card in self._cards:
            if card.rank in ['J', 'Q', 'K', 'A']:
                print(card)
                cards_to_memorize.append(str(card))
        return cards_to_memorize

    def deck_recall(self):
        """ Beginner friendly verson of faces only """
        d = Deck()
        d.shuffle()
        print('Start from only face cards.')
        def timeout():
            """ using threaing for a recall timer """
            print('Time is up!')
        sec = input('How many seconds would you need to review the number? ')
        sec = int(sec)
        # starting the timer
        t = Timer(sec, timeout)
        t.start()
        memorize = d.show_order_begginer()
        print(f'Now recall. You have {sec} seconds to work on it!')  # Add timer and erase the sequence
        # join as time is up
        t.join()

        os.system('clear')

        for card in memorize:
            guess = input('Next card? ')
            if card == guess:
                pass
            else:
                print(f'Wrong, correct card was {card}')
                break