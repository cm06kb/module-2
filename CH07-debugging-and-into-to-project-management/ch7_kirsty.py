# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:55:50 2018

@author: Gebruiker
"""
#----------------------TASK 1--------------------------------------------------
userInput = int(input('please give a number '))
result = userInput - 2
print(type(userInput))
#----------------------TASK 2--------------------------------------------------
def simpleOperation(userInput):
    result = userInput - 2
    return result

def nestedOperation(result):
    result = simpleOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation(result)
print(result2)
simpleOperation(userInput)




