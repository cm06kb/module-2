

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

salary_dic = {"al":20000, "bo":50000, "ced":1500}

labels = list(salary_dic.keys())
print(labels)

labels.sort(reverse = True, key = lambda k:salary_dic[k])
print("keys sorted by values from highest to lowest: " + str(labels))

for label in labels:
    print({"{0:>8} = {1:5.1f}".format(label, salary_dic[label]))

#-------------------------TASK EIGHT: COMBINE COUNTING LOOP AND CONDITIONALS TO FILTER OUT VALUES --------






#-------------------------TASK NINE: DESIGN A SUM FUNCTION --------





#-------------------------TASK NINE: DESIGN A SUM FUNCTION --------




















    