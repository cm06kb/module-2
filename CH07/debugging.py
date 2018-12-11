# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:55:50 2018

@author: Gebruiker
"""

userInput = int(input('please give a number '))
result = userInput - 2

userInput = int(input('please give a number '))

def simpleOperation(userInput):
    result = userInput - 2
    return result

def nestedOperation():
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation()

print(result2)