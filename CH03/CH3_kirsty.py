#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:18:12 2018

@author: Gebruiker
"""

"""print("what's your name? ")
name=input().title()
print("Hello {}!".format(name))

age=input("what's your age?")
age=int(age)
if age>30:
    print("Wow your old! Well nice to meet you {0} who is {1}".format(name,age))
else:
    print("You are soo young! Well nice to meet you {0} who is {1}".format(name,age))"""
    
    
    
    
def last2(str):
  last_two_chars=str[-2:] #this should be xx
  
  last_two_chars_part_one=last_two_chars[0] #this should be x
  last_two_chars_part_two=last_two_chars[1] #this should be x
  
  three_times=last_two_chars_part_one*3
  three_in_a_row = (str.count(three_times))
  if last_two_chars_part_one == last_two_chars_part_two and  three_in_a_row==1:
    noOftimesSubstrInStr = (str.count(last_two_chars))
    print(noOftimesSubstrInStr)
  else:
    noOftimesSubstrInStr = (str.count(last_two_chars)-1)
    print(noOftimesSubstrInStr)
last2("axxxaaxx")


def print_hello_world():
    print("hello world!")
    
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

saying_hello();







