# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:55:50 2018

@author: Gebruiker
"""
#------------------------------------------------------------------------------
#                   CHAPTER 7: DEBUGGING
#------------------------------------------------------------------------------


#---------------------TASK 1: USING PRINT TO CHECK FOR ERRORS.-----------
"""
    The code below will not run b/cuserInput is a str type not a int.
    Error message will be displayed. 
    Check for errors by 
    -checking the data type of the users input
    -print out the user input first.
    
"""
userInput = input('please give a number ')
result = userInput - 2

print(type(userInput))
#----------------------TASK 2: USING BREAKPOINTS TO DEBUG----------------------

"""
    break points (e.g. red dot below) can be added to code to check for bugs.
    once break point added use debugging toolbar above. 
    1st  - runs the code up to 1st breakpoint.
    2nd - runs code line by line
    3rd - step into a codeblock selected.
    4th - step out of a selected codeblock.
    5th - ????
    6th - ends debugging mode.
"""
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




