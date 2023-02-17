#make hit
import random
from simple_colors import *
      
deck = ( "A", "2", "3", "4", "5", "6", '7', '8', '9', 'K', "Q", "J", "A", "2", "3", "4", "5", "6", '7', '8', '9', 'K', "Q", "J", "A", "2", "3", "4", "5", "6", '7', '8', '9', 'K', "Q", "J", "A", "2", "3", "4", "5", "6", '7', '8', '9', 'K', "Q", "J", "A", "2", "3", "4", "5", "6", '7', '8', '9', 'K', "Q", "J", "A", "2", "3", "4", "5", "6", '7', '8', '9', 'K', "Q", "J", "A", "2", "3", "4", "5", "6", '7', '8', '9', 'K', "Q", "J")

def dealer_hand():
    print(f"\nDealer's hand: {bot_hand} = {bot_total}\n")

def black_jack():
    print(yellow("\nBLACK JACK\n"))
    print(green(f"\nYou win! \n\nUser's hand: {user_see_hand}\n")) #put everything in a while loop and reset your hand 
    quit()

def hitting(hit, user_total):
    if hit == "K":
        return 10
    elif hit == "Q":
        return 10
    elif hit == "J":
        return 10
    if hit == "A" and user_total + 11 > 21:
        return 1
    elif hit == "A":
        return 11
    else:
        return int(hit)

def bot_hitting(bot_hit, bot_total):
    if bot_hit == "K":
        return 10
    elif bot_hit == "Q":
        return 10
    elif bot_hit == "J":
        return 10
    if bot_hit == "A" and bot_total + 11 > 21:
        return 1
    elif bot_hit == "A":
        return 11
    else:
        return int(bot_hit)
     
while True:
    first = (random.choice(deck)) #Next steps make 11 and 10 into K, Q, J, A Give everything colour
    second = (random.choice(deck))
    user_see_hand = [first, second]
    bot_first = (random.choice(deck))
    bot_second = (random.choice(deck))
    user_total = 0
    bot_total = 0
    match first:
        case "K":
            first = "10"
        case "Q":
            first = "10"
        case "J":
            first = "10"
        case "A":
            first = "11"
            if first == "11" and user_total + 11 > 21:
                first = "1"
    user_total += int(first)

    match second:
        case "K":
            second = "10"
        case "Q":
            second = "10"
        case "J":
            second = "10"
        case "A":
            second = "11"
            if second == "11" and user_total + 11 > 21:
                second = "1"
    user_total += int(second)
    
    bot_hand = [bot_first, bot_second]
    match bot_first:
        case "K":
            bot_first = "10"
        case "Q":
            bot_first = "10"
        case "J":
            bot_first = "10"
        case "A":
            bot_first = "11"
            if bot_first == "11" and bot_total + 11 > 21:
                bot_first = "1"
    bot_total += int(bot_first)

    match bot_second:
        case "K":
            bot_second = "10"
        case "Q":
            bot_second = "10"
        case "J":
            bot_second = "10"
        case "A":
            bot_second = "11"
            if bot_second == "11" and bot_total + 11 > 21:
                bot_second = "1"
    bot_total += int(bot_second)
    item_amount = 0
    bot_item_amount = 0

    while True: 
        if user_total == 21:
            black_jack()
        print(f"\nUser's hand {user_see_hand} = {user_total}")
        hit_or_stand = input(cyan("\nWould you like to Hit or Stand? \n\n> ")).lower()
        if hit_or_stand == "hit":
            hit = random.choice(deck)
            user_see_hand += hit 
            user_total += hitting(hit, user_total)
            if hit == "A" and user_total > 12:
                item_amount = 1
            if user_total == 21:
                black_jack()
            if item_amount == 0 and "A" in user_see_hand:
                if user_total > 21: #dont work lmfao
                    user_total -= 10
                    item_amount = 1

            if user_total > 21:
                print(red("\nBUST\n", 'bold'))
                print(f'User hand: {user_see_hand} = {user_total}')
                dealer_hand()
                quit()
        while hit_or_stand == "stand":
            if bot_total > 21:
                dealer_hand()
                print(green("User wins!\n", 'bold'))
                quit()
            if bot_total > user_total:
                dealer_hand()
                print(red("Bot wins.\n", 'bold'))
                quit()
            if bot_total >= 17:
                if bot_total < user_total:
                    dealer_hand()
                    print(green("User wins!\n", 'bold'))
                    quit()
                else:
                    dealer_hand()
                    print(red("Bot wins.\n", 'bold'))
                    quit()
            if bot_total < 17:
                bot_hit = random.choice(deck)
                bot_hand += bot_hit
                bot_total += int(bot_hitting(bot_hit, bot_total))
                if bot_item_amount == 0 and "A" in bot_hand: 
                    if bot_total > 21:
                        bot_total -= 10
                        bot_item_amount = 1