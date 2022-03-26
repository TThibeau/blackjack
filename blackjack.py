from art import logo
from random import choice
import os

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
###############################################################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Starting values
money = 1000
money_input = 100
p_card = [] # player's card(s)
d_card = [] # dealer's card(s   

# Functions
def deal(p=False,d=False):
    if p:
        p_card.append(choice(cards))
    if d:
        d_card.append(choice(cards))

def dealer_min_check():
    if sum(d_card)<17:
        deal(d=True)
        dealer_min_check()

def determine_win():
    if sum(p_card)==21: return "win"
    if sum(p_card)>21 and sum(d_card)>21: return "draw" 
    if sum(p_card)>21: return "lose"
    if sum(p_card)>sum(d_card): return "win"
    if sum(p_card) == sum(d_card): return "draw"
    if sum(d_card)>21:return "win"
    else: return "lose"

def update_bank(result,money):
    if result == "draw": return money
    if result == "lose": 
        money -= money_input
        return money
    if result == "win":
        money += money_input
        return money  

def hit_or_stand(choice):
    dealer_min_check()
    if choice == "hit":
        deal(p=True)
        if sum(p_card)>21: return
        if sum(p_card) == 21: return
        else:
            print(f"Your cards are {p_card}, the dealer's first card is {d_card[0]}")
            choice = input("Hit or Stand?: ").lower()
            hit_or_stand(choice)
    
    if choice == "stand": return

# Main
os.system('cls||clear')
print(logo + "\n")
while(True):
    choice1 = input("What would you like to do? Type 'increase', 'deal' or 'quit': ").lower()

    if choice1 == "deal":
        deal(True,True)
        deal(True,True)

    if choice1 == "increase":
        add_input = int(input("How much would you like to increase with? 10, 50, 100?: "))
        money_input += add_input
        deal(True,True)
        deal(True,True)

    if choice1 == 'quit':
        break

    print(f"Your cards are {p_card}, the dealer's first card is {d_card[0]}")

    if sum(p_card) != 21:
        choice2 = input("What would you like to do? Type 'Double', 'Hit' or 'Stand': ").lower()

        if choice2 == "double":
            money_input *= 2
            dealer_min_check()
            deal(p=True)
            result = determine_win()
            print(f"Your cards are {p_card}, the dealer's cards are {d_card}")
            print(f"------------->: {result}")
            money = update_bank(result,money)


        if choice2 == "hit" or choice2 == "stand":
            hit_or_stand(choice2)
            result = determine_win()
            print(f"Your cards are {p_card}, the dealer's cards are {d_card}")
            print(f"------------->: {result}")
            money = update_bank(result,money)
    else: 
        print("------------->: Blackjack!")
        money = update_bank("win",money)

    money_input = 100
    p_card = [] # player's card(s)
    d_card = [] # dealer's card(s)   
    
    print(f"Your money is now ${money}")