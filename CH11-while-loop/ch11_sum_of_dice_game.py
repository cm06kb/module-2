# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:25:20 2018

@author: Gebruiker
"""

#"""game 2 - guess the outcome of a dice role"""

from random import randint

def play_dice_game():  
    user_guess = input("I'm going to role two dices, will the sum of the numbers rolled be odd or even? ")
    user_guess = user_guess.lower()        
    dice_val_1 = (randint(1,6))   
    dice_val_2 = (randint(1,6)) 
    one_plus_two = dice_val_1 + dice_val_2    
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
            
def play_again():
    again = input("would you like to play again? Type Y/N: ")
    again.lower()
    if again == "y" or again == "yes":
        return play_dice_game()
    else:
        print("OK, thanks for playing, goodbye!")
        return "OK, thanks for playing, goodbye!"          

