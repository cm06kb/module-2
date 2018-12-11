# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:37:59 2018

@author: Gebruiker
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:53:21 2018

@author: Gebruiker
"""

def dataBundlePurchase(truePasscode, balance):
    return passwordCheck(truePasscode, balance)
                

def passwordCheck(truePasscode, balance):
    userPassword_attempt = input("please enter your password: ")
    if userPassword_attempt == truePasscode:
        return transactionType(balance)
    else:
        print("incorrect password")
        return passwordCheck(truePasscode)

def transactionType(balance):  
    user_transaction_type = input("type 1 to check credit or type 2 to purchase data: ")
    if user_transaction_type == "1":
        return checkBalance(balance)
    elif user_transaction_type == "2":
        return phoneNumberCheck(balance)
    else:
        print("option not possible, please try again")
        return transactionType()
    
def checkBalance(balance):
    if balance>0:
        return "Your balance is £{}".format(balance)
    else:
        print("Insufficient credit, your balance is £{}".format(balance))
        return do_you_want_to_to_up(balance)
    
def phoneNumberCheck(balance):
    userNumber_attempt1 = input("please enter your phone number: ")
    userNumber_attempt2 = input("please enter your phone number: ")
    if userNumber_attempt1 == userNumber_attempt2:
        return credit_requested_less_than_balance(balance)
    else:
        print("Incorrect phone number")
        return phoneNumberCheck()
        
def credit_requested_less_than_balance(balance):
    credit_requested = int(input("please enter the amount of credit  you would like to purchase, this must be a mutiple of 5  :"))     
    if balance>=credit_requested:
        return credit_mutiple_of_5(balance, credit_requested)
    else:
        print("You do not have enough sufficient funds to purchase £{} of credit.".format(credit_requested))
        return do_you_want_to_to_up(balance)
         
def credit_mutiple_of_5(balance, credit_requested):
    balance = balance - credit_requested
    if  credit_requested % 5==0:
         return "You ahve now purchased £{} of credit, your balance is now £{}, please proceed to checkout".format(credit_requested, balance)
    else:
        return "you may only purchase credit in bundles of 5"

def do_you_want_to_to_up(balance):
    does_user_want_to_top_up = input("would you like to top up? please type Y or N : ")
    does_user_want_to_top_up.lower()
    if does_user_want_to_top_up == "y" or does_user_want_to_top_up == "yes":
        return top_up(balance)
    else:
        return transactionType(balance) 
    
def top_up(balance):      
      request_top_up = int(input("How much money would you like to add to your account?"))  
      balance = balance + request_top_up
      print("your new balance is £{}. You can now purchase credit.".format(balance))
      return credit_requested_less_than_balance(balance)

        