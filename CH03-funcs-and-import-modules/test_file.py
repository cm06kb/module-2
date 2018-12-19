# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:45:48 2018

@author: Gebruiker
"""

#------------------------------------------------------------------------------

#  CHAPTER 3 - FUNCTIONS AND IMPORTING MODULES

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#TASK TWO: CREATE A FUNCTION WHICH PRINTS A STR AND PERFORMS A NUMBER OPERATION
#------------------------------------------------------------------------------
import CH3_kirsty as CH3

CH3.saying_hello()

CH3.hello_world_2args(a1, b1)
CH3.hello_world_2args(a2, b2)
CH3.hello_world_4args(a1, b1, a2, b2)

#-------------------------------------------------------------------------------
#    TASK 4  - ADDING TWO NUMBERS FUNCTION
#-------------------------------------------------------------------------------
CH3.add_two_numbers_from_args(2, 5) 


#-------------------------------------------------------------------------------
#    TASK 5  - TEMPERATURE CONVERSION FUNCTION
#-------------------------------------------------------------------------------
CH3.convert_centigrade_to_fahrenheit_and_kelvin(1000)


#"""LEARN PYTHON THE HARDWAY"""
#"""exercise 19"""
#print("We can just give the function numbers directly:")   
##the function cheese_and_crackers is called with numbers added directly as arguments.  
#
#
## the line below is printed to the console.
#print("OR, we can use variables from our script:")
## variables are assigned outside of a function.
#amount_of_cheese = 10 
#amount_of_crackers = 50 
## function called but with variables used as arguments.
#CH3.cheese_and_crackers(amount_of_cheese, amount_of_crackers) 
#print("We can even do math inside too:")    
## function called but with sums used as arguments.
#CH3.cheese_and_crackers(10 + 20, 5 + 6) 
#print("And we can combine the two, variables and math:") 
## function called but with variables used in sums used as arguments.
#CH3.cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#
#"""calling the function - how many people at the dinner party"""
#"""first run"""
#plates = 5
#forks = 8
#CH3.How_many_at_the_dinner_party(plates, forks)
#"""second run """
#CH3.How_many_at_the_dinner_party(5, 8)
#"""third run"""
#CH3.How_many_at_the_dinner_party(5-1, 8+4)
#"""fourth run"""
#CH3.How_many_at_the_dinner_party(plates - 1, forks + 4)
#"""fifth run """
#CH3.How_many_at_the_dinner_party(100 - 19, 10 + 4)
#"""sixth run """
#CH3.How_many_at_the_dinner_party(plates, 10 + 4)
#"""seventh run """
#CH3.How_many_at_the_dinner_party(10 + 4, forks)
#"""eighth run """
#CH3.How_many_at_the_dinner_party(plates* 2, forks%5)
#"""ninth run """
#CH3.How_many_at_the_dinner_party(plates**2, forks/2)
#"""tenth run """
#CH3.How_many_at_the_dinner_party(3**2, 26/2)