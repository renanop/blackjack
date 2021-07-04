# importing libraries
import random

# defining deck suits, ranks and values for blackjack game.
suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}

class Card:
    """
    A model of a card from a standard deck.
    """
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values.get(rank)
        
    def __str__(self):
        return f'A {self.rank} of {self.suit}'


class Deck:
    """
    A model for a deck of cards.
    """
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.all_cards.append(card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
    def __str__(self):
        card_list = [card.__str__() for card in self.all_cards]
        return ', '.join(card_list)

        
class Player:
    
    def __init__(self, name, balance):
        self.name = name
        self.hand = []
        self.balance = balance
    
    def remove_card(self):
        return self.hand.pop()
    
    def add_cards(self, cards):
        if type(cards) == type([]):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)
            
    def add_balance(self, ammount):
        self.balance += ammount
        
    def bet(self, ammount):
        if self.balance >= ammount:        
            self.balance -= ammount
            return ammount
        else:
            print("Balance is not enough")
            return False            
    def player_value(self):
        value = 0
        for card in self.hand:
            value += card.value
            
        return int(value)
    
    def print_hand(self):
        list_text_hand = [card.__str__() for card in self.hand]
        return ', '.join(list_text_hand)
    
    def reset_hand(self):
        self.hand = []
    
    def __str__(self):
        return f'{self.name} has the following cards: {self.print_hand()}. The total number of points is: {self.player_value()}'
        
            


    
    

        
        

