# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 08:26:29 2018

@author: Gebruiker
"""

"""game 1 - guess my randomly generated number"""
from random import randint

def guess_the_number(attempt, random_number_range):
    random_number = (randint(random_number_range[0],random_number_range[1]))
    user_num = get_user_num(random_number_range)    
    count = 1
    diff = get_the_diff(user_num, random_number)
    return compare_the_numbers(user_num, random_number, count, diff, attempt)

def get_user_num(random_number_range):
    user_num = int(input("welcome, try to guess my number. Enter a number between {} and {}:".format(random_number_range[0],random_number_range[1])))
    if user_num not in range(random_number_range[0],random_number_range[1]):
        print("hmm, somethings not rigth there, try again.")
        return get_user_num(random_number_range)
    else:
        return user_num

def get_the_diff(user_num, random_number):          
    if user_num<random_number:
        above_below = "below"
        diff = random_number - user_num
        return diff, above_below
    else:
        above_below = "above"
        diff = user_num - random_number   
        return diff, above_below
            
            
def compare_the_numbers(user_num, random_number, count, diff, attempt):  
    if (user_num == random_number) and (count == 1):
        print("Wow you must be psychic, you got it in one guess!")
        return play_again()    
    elif (user_num == random_number) and (attempt>=count>0):
        print("Well done, that took {} guesses ".format(count))
        return play_again()
    elif (user_num == random_number) and (attempt>=count>0):
        print("Well done, that took {} guess ".format(count))
        return play_again()
    elif (user_num != random_number) and (count<attempt):
        return how_far_from_the_number(user_num, random_number, count, diff, attempt)
    else:
        print("Nope, wrong again, GAME OVER!!!!!!")
        return play_again()
            
def how_far_from_the_number(user_num, random_number, count, diff, attempt):            
    while user_num != random_number:
        if  diff[0]<2:
            if diff[1] == "above":
                user_num = int(input("Ohhhh so close! Though slightly too high. Try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)
            else:
                user_num = int(input("Ohhhh so close! Though slightly too low. Try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)
        elif diff[0]<4:
            if diff[1] == "above":
                user_num = int(input("hmm not a bad guess but too high. Try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)
            else:
                user_num = int(input("hmm not a bad guess but too low. Try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)
        elif diff[0]<6:
            if diff[1] == "above":
                user_num = int(input("Way too high, try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)
            else:
                user_num = int(input("Way to low, try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)
        elif diff[0]<9:
            if diff[1] == "above":
                user_num = int(input("Terrible, far too high. Try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)            
            else:
                user_num = int(input("Terrible, far too low. Try again :"))
                count = count+1
                diff = get_the_diff(user_num, random_number)
                return compare_the_numbers(user_num, random_number, count, diff, attempt)   
                
def play_again():
    again = input("would you like to play again? Type Y/N: ")
    again.lower()
    if again == "y" or again == "yes":
         return guess_the_number(2, [1,10])
    else:
        print("OK, thanks for playing, goodbye!")
        return "OK, thanks for playing, goodbye!"
            
  