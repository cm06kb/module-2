#------------------------------------------------------------------------------
#                        CHAPTER NINE: COMPOUND DATA TYPES
#                                LISTS AND TUPLES
#------------------------------------------------------------------------------


#--------------------------TASK ONE: CREATE A LIST-----------------------------
my_favourite_fruits = ["apples", "orange", "banana"]

x = ["this", 55, "that",my_favourite_fruits]

print(x[0], x[1], x[2], x[-1][-1])

#----------------------------TASK 2: MODIFY A LIST ------------------------------

#remove items in a list.
x.remove(my_favourite_fruits)
print(x)
#update items in a list.
x[1] = "and"
print(x)
#add items in a list.
x.append("again")
print(x)
#concatenate two lists
x = ["the", "cat", "sat"]
y = ["on", "the", "mat"]
z = x + y
print(z)
print(set(x+y))

#can also use pop and del to remove items from a list.
a = [0,1,2,3,4,5,6,7,8,9]
print(a)
del a[-1]
print(a)
""" removes the last element in the list, the original list has been altered"""
a.pop(-1)
print(a)
"""removes the last item in the list, original list has been altered"""


#---------------------TASK 3: SLICING A LIST-----------------------------------
x = ["this", "and", "that", "once", "again"]
print(x)
#starting at index one and ending at index 4 (not including).
print(x[1:4])
#all elemenst starting from index 2.
print(x[2::])
#we can add a third arg to slicing to increment the slice.
#we can use negative nubers to slice in reverse.

#---------------------TASK 4: SORTING A LIST-----------------------------------

"""
    .sort alters the original array (less memory used)
    sorted returns a new array (more memory used)
    reverse = False sorts descending.
    
"""
x = [7, 11, 3, 9,2]
print(x)
print(sorted(x))
print(sorted(x, reverse = False))
print(x)
x = [7, 11, 3, 9,2]
x.sort()
print(x)

x = [ "cd", "ab", "gy", "fy", "ee"]
print(x)
print(sorted(x))
print(sorted(x, reverse = False))
print(x)
x.sort()
print(x)


#-------------------------TASK 5: USING TUPLES---------------------------------
"""
NOTE TUPLES ARE IMMUTABLE (JUST LIKE STRINGS AND NUMBERS).
Trying to delete, pop, append or reassign values in b will throw an error.
"""
a =[0,1,2,3,4,5,6,7,8,9]
del a[-1]
print(a)

b =(0,1,2,3,4,5,6,7,8,9)
del b[-1]
print(b)
b[0] = 51
b.pop(-1)
b.append("z")


#-------------------------TASK 6: LAMBDA-------------------------------
"""
    LAMBDA FUNCTIONS: SORTING A LIST OF TUPLES BY THEIR VALUES.
    
"""
a = [50,1,2,3,4,5,6,7,8,9]
b = (0,1,2,34,5,6,78,9)
c = (2,2,3,3,4,5,6,7,8,9)
my_favourite_fruits = ["apple", "oranges", "pears"]
x =["yw", "zs", "cs", "hd", "ab"]
y = ["ab", "cs", "hd", "yw", "zs"]
z = ["zs", "yw", "hd", "cs", "ab"]

y[0] = "zz"
y[-2] = "sd"

x2 = [("A", 3, z), ("c",1,y), ("b", 5, x)]

"""
    below we are sorting list of tuples x2. The key tells us what x2 should be sorted by.
    lambda function code block runs, the code block tells us to sort x2 by
    third value of the tuple.
    
"""
print(sorted(x2, key=lambda s:s[2][1][1]))
x2 = [("a", 3, z), ("c",1,y), ("b", 5, x)]
"""s represent each tuple, x2 tuples are sorted by item with index 0"""
print(sorted(x2, key=lambda s:s[1]))
"""sorting by  letter a """
print(sorted(x2, key = lambda s:s[2][1]))
"""sorting by number 1 """


























