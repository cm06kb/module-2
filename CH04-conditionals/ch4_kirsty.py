# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:58:58 2018

@author: Gebruiker
"""

print("this" == 'this')

print(3>=4)
print(3>=2)
print(5!=3)
print(5!=3)
print(5!="some string")

def are_they_a_teen():
    age = int(input("how old are you?"))
    is_a_teen = age >= 13 and age <=19
    print("Are they a teen: " + str(is_a_teen))

are_they_a_teen()
#--------------------------TASK 3 and TASK 4-----------------------------------
def num_between_1_and_10():
    number = int(input("Enter a number between 1 and 10: "))
    if number>10:
        print("Too high!")
    elif number<=0:
        print("Too low!")
    else:
        print("very good, you understood the instructions")

num_between_1_and_10()





#--------------------------------TASK 5----------------------------------------
def what_are_they():
    age = int(input("how old are you?"))
    if age<13:
        print("You are a child")
    elif age<18:
        print("You are a teen")
    elif age < 65:
        print("adult")
    else:
        print("You are a pensioner")

what_are_they()

#----------------LEARN PYTHON HARDWAY--------------------------

"""exercise 11"""
print("How old are you?"),
age = input() 
print("How tall are you?"),
height = input()
print("How much do you weigh?"),
weight = input() 
print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

""" Q: what is raw_input? Ans: returns user input as a string."""

    
"""exercise 30"""
people = 30     
cars = 40 
buses = 15 
if cars > people:        
    print("We should take the cars.")     
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")   

if buses > cars:      
    print("That's too many buses.") 
elif buses < cars: 
    print("Maybe we could take the buses.") 
else: 
    print("We still can't decide.") 
            
if people > buses:     
   print("Alright, let's just take the buses.")   
else: 
   print("Fine, let's stay home then.")

    