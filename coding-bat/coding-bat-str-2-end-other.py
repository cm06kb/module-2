# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:36:38 2018

@author: Gebruiker
"""

"""
#Question
#Given two strings, return True if either of the strings appears at the very 
#end of the other string, ignoring upper/lower case differences (in other words,
# the computation should not be "case sensitive"). Note: s.lower() returns the 
#lowercase version of a string.
#
#
#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True"""
#
#
#"""solved where each function only does one thing""""
#def end_other(a, b):  
#  lower_case_first_word, lower_case_second_word = make_words_lowercase(a, b)
#  first_word_length, second_word_length = get_length_ofwords(lower_case_first_word, lower_case_second_word)
#  word_in_word = is_either_word_in_other(lower_case_first_word, lower_case_second_word, first_word_length, second_word_length)
#  if word_in_word==False:
#      return False
#  else:
#      return is_word_at_end_of_other(lower_case_first_word, lower_case_second_word, first_word_length, second_word_length)
#
#def make_words_lowercase(a, b):
#  lower_case_first_word = a.lower()
#  lower_case_second_word = b.lower()
#  return (lower_case_first_word, lower_case_second_word)
#  
#def get_length_ofwords(lower_case_first_word, lower_case_second_word):
#  first_word_length = (len(lower_case_first_word))
#  second_word_length = (len(lower_case_second_word))
#  return (first_word_length, second_word_length)
#  
#def is_either_word_in_other(lower_case_first_word, lower_case_second_word, first_word_length, second_word_length):
#  if (lower_case_second_word in lower_case_first_word) or (lower_case_first_word in lower_case_second_word):
#    return is_word_at_end_of_other(lower_case_first_word, lower_case_second_word,first_word_length, second_word_length)
#  else:
#    return False
#end_other('Hiabc', 'abc')
#end_other('Hiabcx', 'bc')
#
#"""or alternative method""""
#def end_other(a, b):
#  lower_case_first_word = a.lower()
#  first_word_length = (len(lower_case_first_word))
#  lower_case_second_word = b.lower()
#  second_word_length = (len(lower_case_second_word))
#  print(lower_case_first_word[-second_word_length::])
#  print(lower_case_second_word[-first_word_length::])
#  
#  
#  if (lower_case_second_word in lower_case_first_word) or (lower_case_first_word in lower_case_second_word):
#    if (lower_case_first_word[-second_word_length::]== lower_case_second_word[-first_word_length::]):
#        print(True)
#    else:
#        print(False)
#  else:
#    print(False)
#
#
#end_other('Hiabc', 'abc')
#end_other('Hiabcx', 'bc')

#def count_evens(nums):
#  count = 0
#  print(len(nums))
#  for n in range(len(nums)-1):
#    if nums[n]%2 == 0:
#      count = count + 1
#    else:
#      count = count
#  return count
#     
#print(count_evens([1, 3, 5]))

#def big_diff(nums):
#    nums.sort()
#    answer = nums[-1] - nums[0]
#    print(answer)
#    
#big_diff([10, 3, 5, 6])

#def sum13(nums):
#  sum = 0
#  for n in nums:
#     if n==13:
#         nums.remove(n)
#         print(nums)
#     else:
#         sum += n
#         print(sum)
#  return sum
#  
#print(sum13([1, 2, 13, 2, 3, 13, 1]))


#def remove_six_to_seven(nums):
#    while 6 in nums:
#        index_6 = nums.index(6)
#        index_7 = (nums.index(7)+1)
#        nums2 = (nums[index_6:index_7])
#        for n in nums2:
#            if n in nums:
#                nums.remove(n)
#        return nums
#
#def sum67(nums):
#    while 6 in nums:
#        remove_six_to_seven(nums)
#
#    sum=0
#    for n in nums:
#        sum += n
#    return sum
#
#print(sum67([1, 2, 2, 6, 99, 99, 7]))
#print(sum67([1, 1, 6, 7, 2]))
#print(sum67([1, 2, 2]))
#print(sum67([6, 7, 1, 6, 7, 7]))


#def remove_six_to_seven(nums):
#      index_6 = nums.index(6)
#      index_7 = nums.index(7, index_6)
#      i = index_6
#      while i<=index_7:
#          nums.remove(nums[index_6])
#          i+=1
#      if 6 in nums:
#          remove_six_to_seven(nums)
#      else:    
#          return nums
#      
#
#def sum67(nums): 
#    sum = 0
#    if 6 in nums:
#        remove_six_to_seven(nums) 
#        for n in nums:
#            sum += n
#        return sum
#    else:
#        for n in nums:
#            sum += n
#    return sum
#
#
#
#print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))
#print(sum67([1, 1, 6, 7, 2]))
#print(sum67([6, 7, 1, 6, 7, 7]))


"""Given an array of ints, return True if the array contains a 2 next to a 2 somewhere."""

def has22(nums):
    if 2 in nums:
        num2 = nums[(nums.index(2))] 
        num_infront_2 = nums[(nums.index(2)-1)]
        num_after_2 = nums[(nums.index(2)+1)]
        return num_infront_2 == num2  or num2 == num_after_2
        
print(has22([1, 2, 2])) 
print(has22([1, 2, 1, 2])) 
#print(has22([2, 1, 2]))




