# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:24:19 2018

@author: Gebruiker
"""

"""game 2 - with weighted dice"""

from random import choice

def play_weighted_dice_game():       
    user_guess = get_user_guess()  
    return weight_the_dice(user_guess)

def get_user_guess():
    user_guess = input("I'm going to role two dices, will the sum of the numbers rolled be odd or even? ")
    user_guess = user_guess.lower()
    if user_guess =="odd" or user_guess =="even":
        return user_guess
    else:
        print("Hmm, somethings not quite right, let's try again.")
        return get_user_guess()


def weight_the_dice(user_guess):
    if user_guess == "odd":
        my_list_even = [1] * 5 + [2] * 10 + [3] * 5 + [4] * 10 + [5] * 5 + [6] * 10
        dice_val_1 = int(choice(my_list_even))
        print(dice_val_1)
        dice_val_2 = int(choice(my_list_even))
        print(dice_val_2)
        one_plus_two = dice_val_1 + dice_val_2 
        print(one_plus_two)
        odd_or_even = one_plus_two%2 
        return compare_dice_and_user_guess(odd_or_even, user_guess, dice_val_1, dice_val_2, one_plus_two)
    elif user_guess == "even":
        my_list_odd = [1] * 10 + [2] * 5 + [3] * 10 + [4] * 5 + [5] * 10 + [6] * 5
        dice_val_1 = choice(my_list_odd)
        print(dice_val_1)
        dice_val_2 = choice(my_list_odd)
        print(dice_val_2)
        one_plus_two = int(dice_val_1) + int(dice_val_2)     
        print(one_plus_two)
        odd_or_even = one_plus_two%2 
        return compare_dice_and_user_guess(odd_or_even, user_guess, dice_val_1, dice_val_2, one_plus_two)

def compare_dice_and_user_guess(odd_or_even, user_guess, dice_val_1, dice_val_2, one_plus_two):
    if (odd_or_even == 0) and (user_guess == "even"):
        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is even. YOU WIN!".format(dice_val_1, dice_val_2, one_plus_two))
        return play_again()
    elif (odd_or_even == 0) and (user_guess == "odd"):
        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is even. YOU LOSE!".format(dice_val_1, dice_val_2, one_plus_two))
        return play_again()
    elif (odd_or_even != 0) and (user_guess == "odd"):
        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is odd. YOU WIN!".format(dice_val_1, dice_val_2, one_plus_two))
        return play_again() 
    else:      
        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is odd.Sorry, YOU LOSE!".format(dice_val_1, dice_val_2, one_plus_two))
        return play_again()
            
def play_weighted_dice_game():
    again = input("would you like to play again? Type Y/N: ")
    again = again.lower()
    if again == "y" or again == "yes":
        return play_dice_game()
    elif again == "n" or again == "no":
        print("OK, thanks for playing, goodbye!")
        return "OK, thanks for playing, goodbye!"  
    else:
        print("Hmmm, somethings not quite right. Let's try that again.") 
        return  play_again()

