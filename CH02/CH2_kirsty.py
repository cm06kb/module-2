#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:18:12 2018

@author: Gebruiker
"""
"""task 1"""
print(5 - 6)
print(8 * 9)
print(6 / 2)
print(5 / 2)
print( 5.0 / 2)
print(5 % 2)
print(2 * (10 + 3))
print(2 ** 4)
 
"""Task 2 variable practise."""
age = 5
age = "almost three"
a_longer_name = "hello, CFG!"
print (age)
print (a_longer_name)
age=5
age="almost there"
age=29.5
age="I really don't know!"
print(age)

"""task 3 """

print("hello" + "world")
print("joke" *3)
print("chen"+ str(3))
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())


s1="hello" + "world"
s2="joke"*3
s3=5
print(s1 + " " + s2*10)
print(s1 + " " + s2 + " " +  " " + str(s3))

strExample="a,b,b,s,happy"
print(strExample.split(","))

"""string formatting task 4"""
age=6
like="painting"

age_description="My age is {} and I like {}.".format(age,like)
print(age_description)

age_description2="My age is {0} and I like {1}.".format(age,like)
print(age_description2)
"""here the variables are pivate, if we change the age 
variable below, age_description variables will not change.
the code is read sequentially. Everything is provate, inside a scope.
NOT GLOBAL
Question: is this the case in Javascript? 
ANSWER: Yes this is exactly the same in JS"""

rabbit="""bugs bunny

is a cool rabit"""
print(rabbit)


"""
%s
%d
%r
are all the same as {} in python 2"""

age_description = "My age is {0} and I like {1}.".format(age, like)

"""homework end of chapetr 2"""

print(10/3)
print(10%3)

a=1
a=a+1
a = 1
a = a + 1 
print (a)
b = "hello" 
print (b)
c = b.title() 
print (b)
print (c)
d = "hello"
e = d.title()
print (d)
print (e)
name = "Dave"
f = "Hello {0}! ".format(name) 
print (f)
name = "Sarah"
print (f)
print (f *5)


"""learn python the hardway"""""
"""exercise 1"""
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

""""exercise 2"""
"""I checked the code above"""
"""exercise 3"""

print("I will now count my chickens:")
#30 is divided by 6, and the answer is added to 25.
print("Hens", 25.0 + 30.0 / 6.0)
# 25 is multiplied by the remiander of 3 divided by 4, then the sum is subtracted from 100.
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")
# 1 is divided by  four and then added to 6, this is then subtracted from 
#the remainder of 4/2, then added to 5, then subtracted from 6.

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")
# the program checks if 5 is less than -2, it is not so prints false. 
print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")
# the program checks if 5 is greater than minus 2, it is so prints true.
print("Is it greater?", 5.0 > -2.0)
# the program checks if 5 is greater than or equal to minus 2, it is so prints true.
print("Is it greater or equal?", 5.0 >= -2.0)
# the program checks if 5 is less than or equal to minus 2, it is not so prints false.

print("Is it less or equal?", 5.0 <= -2.0)
# hmmmmm, why is 7/4 not cutting off the decimal?
print(7/4)
print(7.0/4.0)

"""Exercise 4: Variables And Names"""
#  we have assigned some number and a float to variables. We used these variables in  
#  calculations and assigned these too to variables. We have then concatenated  strings 
#  with our variables and printed these to the console.
cars = 100
space_in_a_car = 4.0 #  hmm removing the floating point appears to have no effect....
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#  carpool capacity must be defined by average_passengers_per_car as
# python reads the code top to bottom.The variables are private not global.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

"""exercise 5"""
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % 
    (age, height, weight, age + height + weight))

inches = 5.0
pounds = 20.0
inch_to_centimetre= inches * 2.54
pound_to_kilogram = pounds/0.45

print("%d inches is the same as %d centimetres." % (inches, inch_to_centimetre))
print("%d pounds is the same as %d kilograms." % (pounds, pound_to_kilogram))


"""Exercise 6: Strings and Text"""
# strings ahve been assigned to variables, and string formatting has been used to add 
# in string and decimal values.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)
#  string is printed which includes string formatting using %r, which will print the raw string.
print("I said: %r." % x)
print("I also said: '%s'." % y)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# prints raw string and False
print(joke_evaluation % hilarious)

w = ("This is the left side of...")
e = ("a string with a right side.")
# conctenate variable e with variable W
print(w + e)

"""exercise 7"""
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do? ans= prints fullstop ten times.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens ans=no change...
# prints out concatenated variables, comma should make all the concatenated strings appear on one line
# but they don't?????
print(end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)


"""Exercise 8: Printing, Printing"""
formatter = "%r %r %r %r"
# another method of using string formatting, where keyword formatter staed first
# folloed by pound sign, the brackets containg the object to print out.
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))


"""Exercise 9: Printing, Printing, Printing"""
days= "Mon Tues Wed Thurs Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

"""exercise 10: what was that?"""

while True: 
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i,)
        break
        








