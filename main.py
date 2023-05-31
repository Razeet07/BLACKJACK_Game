import random
import os
from art import logo
def deal_card():
    '''Returns a Random card form the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


    ''' Take a list of cards and return score calaculated frm card'''

'''Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
 If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), 
 then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
 If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.'''

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Black Jack"
    elif user_score == 0:
        return "win with blackjack"
    elif user_score > 21:
        return "you went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over. You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "YOU lOSE"
    
    

# Deal the user and computer 2 cards each using deal_card() and append().

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 11: The score will need to be rechecked with every new card drawn and
    #  the checks in Hint 9 need to be repeated until the game ends.

    while not is_game_over:

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or 
    # if the user's score is over 21, 
    # then the game ends.

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)



        print(f" your card :{user_cards}, Current Score: {user_score}")
        print(f" Comp's First card :{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        # Hint 10: If the game has not ended, 
        # ask the user if they want to draw another card. 
        # If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

        else:
            user_deal = input("Type 'y' to get another card , type 'n' to pass :" )
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    #Hint 12: Once the user is done, it's time to let the computer play.
    # The computer should keep drawing cards as long as it has a score less than 17.

    ''' Now computer Play'''

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"your Final hand:{user_cards}, final score : {user_score}")
    print(f"Computer's Final hand:{computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))


''' Asking user to play another game /quit the game '''


while input("Wanna play BLACKJACK? Type 'y'  or 'n': ") == "y":
    os.system('clear')
    play_game()


