#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:18:12 2018

@author: Gebruiker
"""

#------------------------------------------------------------------------------

#  CHAPTER 3 - FUNCTIONS AND IMPORTING MODULES

#---------------------------------------------------------------------------------------

#-TASK TWO: CREATE A FUNCTION WHICH PRINTS A STR AND PERFORMS A NUMBER OPERATION-----

#-------------------------------------------------------------------------------------

def saying_hello():
        print("what's your name? ")
        name=input().title()
        age=input("what's your age?")
        age=int(age)
        if age>30:
            print("Wow your old! Well nice to meet you {0} who is {1}, oh and HELLO WORLD!".format(name,age))
        else:
            print("You are soo young! Well nice to meet you {0} who is {1}, oh and HELLO WORLD!".format(name,age))
        
        num1 = input("give me any two numbers and I will mutiply them for you, give me the first number: ")
        num2 = input("OK, now the second number: ")
        num1= int(num1)
        num2 = int(num2)
        num3 = num1 * num2
        print("That's easy, {} multiplied by {} is just {}".format(num1, num2, num3))        
        print_hello_world()

#-------------------------------------------------------------------------------
#    TASK 4  - ADDING TWO NUMBERS FUNCTION
#-------------------------------------------------------------------------------

def add_two_numbers_from_args(number1, number2): 
 answer = number1 + number2
 print ("{} plus {} is {}".format(number1, number2, answer))


#-------------------------------------------------------------------------------
#    TASK 5  - TEMPERATURE CONVERSION FUNCTION
#-------------------------------------------------------------------------------

def convert_centigrade_to_fahrenheit_and_kelvin(centigrade): 
    fahrenheit = centigrade * 9.0 / 5.0 + 32 
    kelvin = centigrade + 273.15
    main_result = "{} Degrees Centigrade is the same as {} Degrees Fahrenheit and {} Kelvin.".format(centigrade, fahrenheit, kelvin)
    print(main_result)
    return main_result





#"""LEARN PYTHON THE HARDWAY"""
#"""exercise 19"""
## the function cheese_and_crackers is defined. It takes three arguments.This will be skipped
##by the interpreter until the function is called.
#def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print("You have %d cheeses!" % cheese_count)
#    print("You have %d boxes of crackers!" % boxes_of_crackers)
#    print("Man that's enough for a party!")        
#    print("Get a blanket.\n")   
## the line below is printed to the console.
#
#
#"""Write at least one more function of your own design, and run it 10 different ways"""
#
#def How_many_at_the_dinner_party(plate_count, number_of_forks):
#    print("You have %d plates!" % plate_count)
#    print("You have %d forks!" % number_of_forks)
#    if plate_count<number_of_forks:
#        number_of_guests=plate_count
#    else:
#        number_of_guests=number_of_forks
#    print("You have {} plates and {} forks, this means you can have {} guests!".format(plate_count, number_of_forks,number_of_guests))        
#
#
#
#
#"""exercise 20"""
##from sys import argv 
#
#
#
##script, input_file = argv
##
##def print_all(f):        
##    print(f.read())
##def rewind(f): 
##    f.seek(0) 
##def print_a_line(line_count, f): 
##    print(line_count, f.readline()) 
##
##current_file = open(input_file)   
##print("First let's print the whole file:\n")
##print_all(current_file) 
##print("Now let's rewind, kind of like a tape.")
##rewind(current_file) 
##print("Let's print three lines:") 
##current_line = 1 
##print_a_line(current_line, current_file) 
##current_line = current_line + 1 
##print_a_line(current_line, current_file) 
##current_line = current_line + 1 
##print_a_line(current_line, current_file)

##-------------------------------------------------------------------------------
##    TASK TWO  - USING RANGE() WITH ARGUMENTS ()
##-------------------------------------------------------------------------------
#print(list(range(10))) 
#print(list(range(1,10))) 
#print(list(range(1,10,2))) #start, end, steps
##you dont have to use the step or end arguements if you dont want to.....







