"""
List Sum:
(1: Create a function that takes a list of numbers as input,)  and (2 : returns the sum of all the elements in the list.)
"""

#pseudocode
# define our function
# function takes in a list
# add the elements of the list
# return the sum.


#solution
# Time complexity
# O(n)

# def sum_numbers(lst=None):
#     total = 0
#     for i in lst:
#         total += i
#         # sum = sum + i

#     return total


# total = sum_numbers([1,2,3,4,5,6,7,8,9,10])
# print(total)

#O(n)
def sum_numbers(lst=None):
    if lst is None or not isinstance(lst, list):
        raise ValueError("input not allowed")
    
    total = sum(lst)
    return total


try:
    # total = sum_numbers([1,2,3,4,5,6,7,8,9,10])
    total = sum_numbers((1,2,3,4,5,6,7,8,9,10))

    # total = sum_numbers("Gems")
    print(total)
except ValueError as ve:
    print(f"Error: {ve}")


















# lists = []

# isaac_code([1,2,3,4])
#isaac_code("oihjoihjoi")

#Nalu sketch.
#planing phase
#import Numpy
# consider try and except block. isinstance(lst, list);
# list of Numbers

#################################
# prompt the user for input.
# check if the input are valid numbers
# create a variable for sum
# loop through the Numbers and add them to the sum.
# return or print






