# Initializing objects:
from classes import Deck, Player

dealer = Player('dealer', 99999999999)

deck = Deck()
deck.shuffle()


## GAME LOGIC

# Initializing player 

name = input('Hello! What is your name? ')
starting_balance = float(input(f'Hi, {name}. What is going to be your initial balance? '))
print("Great. Let the games begin.")

player = Player(name, starting_balance)

game_on = True


# Turn function

def turn():
    turn_card_player = deck.deal_one()
    turn_card_dealer = deck.deal_one()
    player.add_cards(turn_card_player)
    dealer.add_cards(turn_card_dealer)

# GAME LOGIC

while game_on:
    
    # Generating a new deck
    deck = Deck()
    deck.shuffle()
    
    # Reseting dealer and player's hand
    
    player.reset_hand()
    dealer.reset_hand()
    
    # Setting winner and bet boolean values
    
    winner = False
    current_bet = False
        
    # Phase 1: player bets an ammount of money
    while current_bet == False:
        
        try:
            
            bet = float(input('How much you are going to bet? '))
            current_bet = player.bet(bet)
            
        except:
            print("Please enter a number")
    
    
    # Phase 2: Player draws a card
    play_turn = input("Wanna draw a card? [y/n] ")
    
    while play_turn == 'y':
        
        turn()
        
        print(player)
        
        if player.player_value() > 21:
            print(f'{player.name} loses the game!')
            break
        elif player.player_value() == 21:
            print(f'{player.name} scores 21 points and wins the game!!')
            winner = True
            break
        else:
            play_turn = input("Wanna draw a card? [y/n] ")

    # Phase 3: Player stops drawing cards
            
    if play_turn != 'y':
        print(player)
        print(dealer)
            
        if player.player_value() < dealer.player_value() and dealer.player_value() <= 21:
            print(f'{player.name} scores {player.player_value()} and loses the game!!')
            
        elif player.player_value() == dealer.player_value():
            
            while player.player_value() == dealer.player_value():
                
                turn()
                print(player)
                print(dealer)
                
            if player.player_value() > dealer.player_value():
                winner = True
                print(f'{player.name} scores {player.player_value()} and wins the game!!')
                
            else:
                print(f'{player.name} scores {player.player_value()} and loses the game!!')
                
        else:
            winner = True
            print(f'{player.name} scores {player.player_value()} and wins the game!!')

                
            
    if winner == True:
        wage = 2 * current_bet
        player.add_balance(wage)
        
    if player.balance == 0:
        break
        
    keep_playing = input(f'Player {player.name} current balance is {player.balance}. Keep playing? [y/n] ')
    
    if keep_playing.lower() == 'n':
        game_on == False
        break
    
    
 
print(f'Game over!! {player.name} left the game with {player.balance} coins.')           
    
    
