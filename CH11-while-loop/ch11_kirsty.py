# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:16:34 2018

@author: Gebruiker
"""

#----------------------------WHILE LOOPs---------------------------------------

"""There are types: conditional loops and counting loops"""


#-------------------------conditional loops------------------------------------
#while var x is greater or equal to 33, print the value of x followed by semi colon
#followed by blank space. Then half x. The last value returned is outside the for loop.

import math
from random import randint

#x = 33
#while x>=1:
#    print(x,":", end="    ")
#    x = x/2
#print(x)
#
##compute triangular numbers, return n +(n-1). The update n=n-1, keeps looping until n=1
#
#def triangular_num(n):
#    while n>=1:
#        print(n+(n-1))
#        n = n-1
#triangular_num(5)
#
#
#
##student mark pass or fail.
#results = {'bob': 65, 'bill': 85, 'james': 13}
#result_list =list(results.items())
#
#n=0
#while n <= (len(result_list)-1):
#    if result_list[n][1] >= 70:
#        print("student {} achieved first class".format(result_list[n][0]))
#    elif result_list[n][1] >= 40:
#        print("student {} achieved a passing grade".format(result_list[n][0]))
#    else:
#      print("student {} failed".format(result_list[n][0]))
#    n = n + 1
#print(result_list)
#
##alternative method using user input.
#def did_they_pass():
#    passing = "yes"
#    while passing == "yes":
#        name = input("please enter a name:  ")
#        student_mark = int(input("please enter a mark:  "))
#        if student_mark>= 70:
#            print("student {} achieved first class".format(name))
#            passing ="yes"
#        elif student_mark>=40:
#            print("student {} achieved a passing mark".format(name))
#            passing ="yes"
#        else:
#            print("student {} failed".format(name))
#            passing = "no"
#    
#did_they_pass()
#
##using break in while loops
#
#i = 55
#while i>10:
#    print(i)
#    i = i*0.8
#    if i == 35.2:
#        break
#print(i)
#
#"""greeting loop"""
#
#def greetings():
#    name = "placeholder"
#    while name != "done":
#        name = input("Please enter your name: ")
#        print("Greetings and salutations {}".format(name))
#
#greetings()

#"""phonebook_dict with while loop"""
#
#phoneBook = {}
#x = (len(phoneBook)-1)
#while x<3:
#    name = input("Please enter your name: " )
#    lucky = input("Please enter your lucky number: " )
#    postcode = input("Please enter your postcode: " )
#    town = input("Please enter your town/city: " )
#    phoneBook[name] = [lucky, postcode, town]
#    x = (len(phoneBook)-1)
#
#print(phoneBook)


"""game 1"""

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
            
guess_the_number(3,[1,6])         
            

#"""game 2"""


def play_dice_game():  
    user_guess = input("I'm going to role two dices, will the sum of the numbers rolled be odd or even? ")
    user_guess = user_guess()        
    dice_val_1 = (randint(1,6))   
    dice_val_2 = (randint(1,6)) 
    one_plus_two = dice_val_1 + dice_val_1     
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

play_dice_game()
#
#"""game 2 - with weighted dice"""
#
#
#def play_dice_game():       
#    win = 0    
#    lost = 0
#    user_guess = input("I'm going to role two dices, will the sum of the numbers rolled be odd or even? ")
#    dice_val_1 = (randint(1,6))
#    dice_val_2 = (randint(1,6)) 
#    one_plus_two = dice_val_1 + dice_val_1     
#    odd_or_even = one_plus_two%2 
#    return compare_dice_and_user_guess(odd_or_even, user_guess, dice_val_1, dice_val_2, one_plus_two, win, lost)
#
#def compare_dice_and_user_guess(odd_or_even, user_guess, dice_val_1, dice_val_2, one_plus_two, win, lost):
#    if (odd_or_even == 0) and (user_guess == "even"):
#        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is even. YOU WIN!".format(dice_val_1, dice_val_2, one_plus_two))
#        return play_again()
#    elif (odd_or_even == 0) and (user_guess == "odd"):
#        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is even. YOU LOSE!".format(dice_val_1, dice_val_2, one_plus_two))
#        return play_again()
#    elif (odd_or_even != 0) and (user_guess == "odd"):
#        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is odd. YOU WIN!".format(dice_val_1, dice_val_2, one_plus_two))
#        return play_again() 
#    else:      
#        print("Ok, so dice one is {0} and dice two is {1}, so {0} + {1} is {2}, which is odd.Sorry, YOU LOSE!".format(dice_val_1, dice_val_2, one_plus_two))
#        return play_again()
#            
#def play_again(win, lost):
#    again = input("would you like to play again? Type Y/N: ")
#    again.lower()
#    if again == "y" or again == "yes":
#        return play_dice_game()
#    else:
#        print("OK, thanks for playing, goodbye!")
#        return "OK, thanks for playing, goodbye!"          
#
#play_dice_game()







