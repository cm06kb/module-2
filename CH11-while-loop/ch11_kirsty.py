#------------------------------------------------------------------------------
#----------------------------CHAPTER 11: WHILE LOOPs----------------------------
#------------------------------------------------------------------------------

"""
    There are types: conditional loops and counting loops
    
"""

#-------------------------TASK ONE: REPEAT DIVISION---------------------------

#while var x is greater or equal to 33, print the value of x followed by semi colon
#followed by blank space. Then half x. The last value returned is outside the for loop.

x = 33
while x>=1:
    print(x,":", end="    ")
    x = x/2
print(x)

#-------------------------TASK TWO: TRIANGULAR NUMBERS---------------------------

#compute triangular numbers, return n +(n-1). The update n=n-1, keeps looping until n=1

def triangular_num(n):
    while n>=1:
        print(n+(n-1))
        n = n-1
triangular_num(5)


#-------------------------TASK THREE: STUDENT NUMBERS---------------------------

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

#-------------------------TASK 4: BREAK ---------------------------

#using break in while loops -  immediately terminates the current iteration and terminates the loop.

while True:
    name = input("Enter name: ")
    if name == "done":
        break
    print("Hello", name)

"""
    can also use continue command to terminate current iteration and start the next iteration.But use of else is more clear.
    
"""


#-------------------------TASK 5 AND 6: GUESS THE OUTCOME OF A DICE ROLE ---------------------------


from random import randint

def play_dice_game():  
    user_guess = input("I'm going to role two dices, will the sum of the numbers rolled be odd or even? ")
    user_guess = user_guess.lower()        
    dice_val_1 = (randint(1,6))   
    dice_val_2 = (randint(1,6)) 
    one_plus_two = dice_val_1 + dice_val_2    
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

       
            




#"""greeting loop"""
#
#def greetings():
#    name = "placeholder"
#    while name != "done":
#        name = input("Please enter your name: ")
#        print("Greetings and salutations {}".format(name))
#
#greetings()
#
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
    
    
    
    