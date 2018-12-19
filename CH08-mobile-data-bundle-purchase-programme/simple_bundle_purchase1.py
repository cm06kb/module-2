def dataBundlePurchase(password, balance):
    """sets counter user_attempts_at_password to 0. Calls check password function"""
    user_attempts_at_password = 0
    check_userpasswordpasswordCheck(password, balance, count)
    

         

def passwordCheck(password, balance, count):
"""takes a user input of password and compares password passed 
   from databundlePurchase function. If password correct calls transaction type
   function. If incorrect increments the user_attempts_at_password counter """"
    userPassword_attempt = input("  Please input your password: ")
    if userPassword_attempt == truePasscode:
        return transactionType(balance)
    else:
        count += 1
        if count<3:
            print("incorrect password, please try again.")
            return passwordCheck(password, balance, count)
        else:
            print("You have entered an incorrect password three times, you are now locked out of your account. Please contact us for assistance")

def transactionType(balance):  
"""Takes in user input, checks if user wants to check credit or check balance,
calls the the next function based on user input."""
    user_transaction_type = input("type 1 to check credit or type 2 to purchase data: ")
    if user_transaction_type == "1":
        return checkBalance(balance)
    elif user_transaction_type == "2":
        return phoneNumberCheck(balance)
    else:
        print("option not possible, please try again")
        return transactionType(balance)
    
def checkBalance(balance):
"""This func is called if user asked to check balance in transactiontype func.
    This returns users balance, if in the negative, the user is given the option to
    top up"""
    if balance>0:
        print("Your balance is £{}".format(balance))
        return "Your balance is £{}".format(balance)
    else:
        print("Insufficient credit, your balance is £{}".format(balance))
        return do_you_want_to_top_up(balance)
#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
def is_a_uk_num(userNumber_attempt1):
    if len(userNumber_attempt1) == 11 and (userNumber_attempt1[0]==0):
        return True
    elif (len(userNumber_attempt1)==13) and (userNumber_attempt1[4]== "-" or userNumber_attempt1[4]== " " ) and (userNumber_attempt1[8]=="-" or userNumber_attempt1[8]=="-"):
        return True
    elif (len(userNumber_attempt1)==13) and (userNumber_attempt1[3]== "-" or userNumber_attempt1[3]== " " ) and (userNumber_attempt1[9]=="-" or userNumber_attempt1[9]=="-"):
        return True
    elif (len(userNumber_attempt1) == 15) and (userNumber_attempt1[0]=="(") and  (userNumber_attempt1[4]==")" or userNumber_attempt1[5]==")" or userNumber_attempt1[6]==")" or userNumber_attempt1[9]==")"):
        return True
    else:
        return False

def phoneNumberCheck(balance):
    userNumber_attempt1 = input("please enter your phone number: ")
    valid = is_a_uk_num(userNumber_attempt1)
    if valid==True:
        userNumber_attempt2 = input("please re-enter your phone number: ")
        if userNumber_attempt1 == userNumber_attempt2:
            return credit_requested_less_than_balance(balance)
        else:
            print("Incorrect phone number")
            return phoneNumberCheck(balance)
    else:
        print("Incorrect phone number")
        return phoneNumberCheck(balance)


    
        
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



        