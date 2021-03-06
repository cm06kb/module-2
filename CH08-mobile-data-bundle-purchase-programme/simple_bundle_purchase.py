

def dataBundlePurchase(password, balance):
    """ 
        starts the purchase of a data bundle.
        Sets a counter, to check how many times user has entered password to 0. 
        Then calls check password function
    """
    user_attempts_at_password = 0
    return passwordCheck(password, balance, user_attempts_at_password )
      

def passwordCheck(password, balance, user_attempts_at_password):
    """
       takes a user input of password and compares password passed 
       from databundlePurchase function. If password correct calls transaction type
       function. If incorrect increments the user_attempts_at_password counter 
    """
    userPassword_attempt = input("  Please input your password: ")
    if userPassword_attempt == password:
        return transactionType(balance)
    else:
        user_attempts_at_password += 1
        if user_attempts_at_password<3:
            print("incorrect password, please try again.")
            return passwordCheck(password, balance, user_attempts_at_password)
        else:
            print("You have entered an incorrect password three times, you are now locked out of your account. Please contact us for assistance")

def transactionType(balance):  
    """
        Takes in user input, checks if user wants to check credit or check balance,
        calls the the next function based on user input.
    """
    user_transaction_type = input("type 1 to check credit or type 2 to purchase data or 3 to exit: ")
    if user_transaction_type == "1":
        return checkBalance(balance)
    elif user_transaction_type == "2":
        return phoneNumberCheck(balance)
    elif user_transaction_type == "3":
        print("Thank you for using our services, goodbye.")
        return "Thank you for using our services, goodbye."
    else:
        print("option not possible, please try again")
        return transactionType(balance)
#---------------------------------------------------------------------------
# TRANSACTION TYPE 1 CALLED - CHECK BALANCE
#-----------------------------------------------------------------------------        
def checkBalance(balance):
    """
        This func is called if user asked to check balance in transactiontype func.
        This returns users balance, if in the negative, the user is given the option to
        top up
    """
    if balance>0:
        print("Your balance is £{}".format(balance))
        return do_you_want_to_top_up(balance)
    else:
        print("Insufficient credit, your balance is £{}".format(balance))
        return do_you_want_to_top_up(balance)
    
def do_you_want_to_top_up(balance):
    """ 
        checks if user wants to top.
        If yes returns a function to top up balance.
        If no returns the transaction type function.
        
    """
    does_user_want_to_top_up = input("would you like to top up? please type Y or N : ")
    does_user_want_to_top_up.lower()
    if does_user_want_to_top_up == "y" or does_user_want_to_top_up == "yes":
        return top_up(balance)
    else:
        return transactionType(balance) 

def top_up(balance):  
      """
          Asks user how much they want to top up.And updates the balance
          
      """
      request_top_up = int(input("How much money would you like to add to your account?"))  
      balance = balance + request_top_up
      print("your new balance is £{:.2f}. You can now purchase credit.".format(balance))
      return transactionType(balance)
    
#------------------------------------------------------------------------------
# if user wants to top up they must first enter their phone number 
# correctly twice.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# OPTION 2 : USER WANTS TO ADD CREDIT.      
#------------------------------------------------------------------------------

def phoneNumberCheck(balance):
    """
        Before user tops up they must enter their phone number correctly twice.
        Checks the number entered twice is the same.
        Calls is_a_uk_num function to check num is a valid telephone number. 
        If number is valid credit_requested_less_than_balance function called 
        to check they have enough credit already to top up.
    """
    userNumber_attempt1 = input("please enter a valid mobile number, starting with a 0 and of the format xxx-xxxx-xxxx: ")
    valid = is_a_uk_num(userNumber_attempt1)
    if valid:
        userNumber_attempt2 = input("please re-enter your phone number: ")
        if userNumber_attempt1 == userNumber_attempt2:
            return credit_requested_less_than_balance(balance)
        else:
            print("Incorrect phone number")
            return phoneNumberCheck(balance)
    else:
        print("Incorrect phone number")
        return phoneNumberCheck(balance)



def is_a_uk_num(userNumber_attempt1):
    """
        Checks the number provided by user is a valid UK number.
    """
    if len(userNumber_attempt1) == 13 and (userNumber_attempt1[0]=="0") and (userNumber_attempt1[3] =="-") and (userNumber_attempt1[8] =="-"):
        return True
    else:
        return False

       
def credit_requested_less_than_balance(balance):
    """
        Checks if the user has enough funds to purchase credits.
        
    """
    credit_requested = int(input("please enter the amount of credit  you would like to purchase, this must be a mutiple of 5: "))     
    if balance>=credit_requested:
        return credit_mutiple_of_5(balance, credit_requested)
    else:
        print("You do not have enough sufficient funds to purchase £{} of credit.".format(credit_requested))
        return do_you_want_to_top_up(balance)
         
def credit_mutiple_of_5(balance, credit_requested):
    """
        User must pruchase credits as multiples of 5.
        Checks if credits requested is divisible by 5 (with no remainder).
    """
    balance = balance - credit_requested
    if  credit_requested % 5==0:
         return "You have now purchased £{} of credit, your balance is now £{:.2f}, please proceed to checkout".format(credit_requested, balance)
    else:
        print("you may only purchase credit in bundles of 5")
        return credit_requested_less_than_balance(balance)


    




        