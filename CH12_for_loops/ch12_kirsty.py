

##------------------------------------------------------------------------------
##----------------------------CHAPTER 12: WHILE LOOPs---------------------------
##------------------------------------------------------------------------------
#
#
#
##-------------------------TASK ONE: LOOP THROUGH A LIST-------------------------
#
#my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
#
#for item in my_shopping_cart:
#    print(item)
#
#
##-------------------------TASK TWO: UPDATE LIST VALUES-------------------------
#
#values = [875, 23, 451]
#"""
#    for each element in values, print the value as a str with ---> before it
#"""
#for val in values:
#    print('---> '+str(val))
#
#
##-------------------------TASK THREE: CREATE OWN LIST AND PRINT-------------------------
#
#values = ["THIS", 55, "that"]
#
#for items in values:
#    print('****', item)
#    
#
##-------------------------TASK FOUR: LOOP THROUGH A STRING DATA TYPE -------------------------
#
#for char in "yes":
#    print(char)
#
##-------------------------TASK FIVE: LOOP THROUGH A TUPLE DATA TYPE -------------------------
#

#my_tup = (1,2,3)
#for n in my_tup:
#    print(n)

#-------------------------TASK SIX AND SEVEN: LOOP THROUGH A DICTIONARY TYPE -------------------------

salary_dic = {"al":20000.1234, "bo":50000.2134, "ced":1500.5678}
"""
    sort the dict above by values from highest to lowest (bo, al, ced).
    
"""
#first convert keys to a list.
labels = list(salary_dic.keys())
print(labels)

#now sort keys by dic value.
labels.sort(reverse = True, key = lambda k:salary_dic[k])
print("keys sorted by values from highest to lowest: " + str(labels))

# use a for loop to loop over each label to print key:value pairs.

"""
string formatting: below we have included {field_name:conversion}.
field_name: index of the arguement to str format.
conversion: s, d or f (convert to str, decimal or float)
below we add 4 spaces of padding to label and right align >.
we show the float values to only 1 decimal point using .1f and give padding value of 8.

"""
for label in labels:
    print('{0:>4} = {1:8.1f}'.format(label, salary_dic[label]))

#--------TASK EIGHT: COMBINE COUNTING LOOP AND CONDITIONALS TO FILTER OUT VALUES --------


"""
Scan a list using if , else and for loops to print particular values
e.g. only print metals in a metal dict with a density value > 8.

"""

densities = {"iron": 7.8, "gold": 19.2, "zinc": 7.13, "lead": 11.4}

sorted_density_dict = sorted(densities.items(), key = lambda kv:kv[1])
print(sorted_density_dict)

only_greater_than_eight = []
for metal in  sorted_density_dict:
        if metal[1]>8:
            only_greater_than_eight.append(metal)
        else:
            pass

print("This is a list containing metals with density greater than 8: " + str(only_greater_than_eight)) 





#-------------------------TASK NINE: DESIGN A SUM FUNCTION --------

"""
use a for loop to sum the values in a list.

"""
def add_up_values(num_to_add):
    total = 0
    for val in num_to_add:
        total += val
        return "TOTAL:" + str(total)

print(add_up_values([3,12,10]))


#-------------------------TASK TEN: USE A LOOP WITH INDEX VALUES --------
def times_by_two(values):
    for i in range(len(values)):
        values[i] = values[i] * 2
        return values

print(times_by_two([1550, 46, 902]))

#-------------------------TASK ELEVEN: USE A LOOP WITH RANGE FUNCTION --------


def generate_a_list(value):
    new_list = list(range(value))
    for i in new_list:
        print(i)
    

generate_a_list(10)
    

#-------------------------TASK TWELVE: USING BREAK IN LOOPS-------------------

nums = [2,3,65,23,123,432,3]
for n in nums:
    if n>100:
        print("found:", n)
        break

#-------------------------TASK THIRTEEN: USING NESTED LOOPS-------------------
"""
code below prints items from the inner loop and the inner loop runs to completion
for each iteration of the outer loop. 

"""
outer_vals = [1,2,3]
inner_vals = ["a", "b", "c"]
for oval in outer_vals:
    for ival in inner_vals: 
        print(oval, ival)
        
#-------------TASK FOURTENN: MULTIPLICATION TABLE WITH A FOR LOOP-------------------

"""
code below:
    inner loop runs until each j item * first item in i is printed,  
    outer loop runs until each item in j has been multiplied by each item in j. 

"""

for i in range(1,11):
    for j in range(1, 11):
        print("{0:>3}".format(i*j), end="")
    """
     back slash n creates a empty line between each iteration of outer loop.
     
    """
    print("\n")    



















    