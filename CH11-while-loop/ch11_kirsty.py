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



x = 33
while x>=1:
    print(x,":", end="    ")
    x = x/2
print(x)

#compute triangular numbers, return n +(n-1). The update n=n-1, keeps looping until n=1

def triangular_num(n):
    while n>=1:
        print(n+(n-1))
        n = n-1
triangular_num(5)



#student mark pass or fail.
results = {'bob': 65, 'bill': 85, 'james': 13}
result_list =list(results.items())

n=0
while n <= (len(result_list)-1):
    if result_list[n][1] >= 70:
        print("student {} achieved first class".format(result_list[n][0]))
    elif result_list[n][1] >= 40:
        print("student {} achieved a passing grade".format(result_list[n][0]))
    else:
      print("student {} failed".format(result_list[n][0]))
    n = n + 1
print(result_list)

#alternative method using user input.
def did_they_pass():
    passing = "yes"
    while passing == "yes":
        name = input("please enter a name:  ")
        student_mark = int(input("please enter a mark:  "))
        if student_mark>= 70:
            print("student {} achieved first class".format(name))
            passing ="yes"
        elif student_mark>=40:
            print("student {} achieved a passing mark".format(name))
            passing ="yes"
        else:
            print("student {} failed".format(name))
            passing = "no"
    
did_they_pass()

#using break in while loops

i = 55
while i>10:
    print(i)
    i = i*0.8
    if i == 35.2:
        break
print(i)

"""greeting loop"""

def greetings():
    name = "placeholder"
    while name != "done":
        name = input("Please enter your name: ")
        print("Greetings and salutations {}".format(name))

greetings()

"""phonebook_dict with while loop"""

phoneBook = {}
x = (len(phoneBook)-1)
while x<3:
    name = input("Please enter your name: " )
    lucky = input("Please enter your lucky number: " )
    postcode = input("Please enter your postcode: " )
    town = input("Please enter your town/city: " )
    phoneBook[name] = [lucky, postcode, town]
    x = (len(phoneBook)-1)

print(phoneBook)


       
            





    
    
    
    