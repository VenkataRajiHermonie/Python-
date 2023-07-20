# To write a program to sort following without using automated sort functionality

# i/p= a=[2,3,5,1,9,4]
# o/p= 1,2,3,4,5,9

"""APPROACH

Considering that the length of the list .i.e array is not of fixed length,
thus may be same or different for every given input,we can apply a brute force
approach."""

"""The steps followed in this approach are:
1.Find the length of the arrayi.e.(list) considered as n.
2.Consider the ith element of the array to be the smallest (minimum) number
  and parse through the entire array from its next ith position
  
  For instance taking the above given example,-->2,3,5,1,9,4
  iteration 1----> i=0 thus a[0]=2,the following indices starting from 1 are compared 
  with a[0] only.
  after iteration 1,the list will be-->1,3,5,2,9,4
  iteration 2: 1st index element ,a[1] which is 3 will be compared from indices
  2 to n.
  NOTE:this loop is performed in a forward fashion,thus the iteration does not 
  come back to previous indices.
  
  
  
  3.If the ith+1 element is smaller then a swap is performed,else the comparision is
  continued till n-1 element"""

# METHOD 1:
"""By asking the user to provide the length of the input beforehand,
# we can ensure the proper number of exact insertions into the without
# wasting the memory using the for loop"""

# Input from the user
n=int(input("Please provide length of the array"))

# An empty list "a" is declared to append/insert the user values at runtime
a=[]

#Taking user input based on length of the list

#range funtion is used in combination with for loop for iteration
for i in range(0,n):

    #user input is inserted at the rear of the list
  a.append(int(input("Enter the element")))
print("list before sorting",a)

# Sorting logic

"""Two for loops are used for comparision 
Loop 1 from (0 to last but 1 element--(n-1)) is the one which is compared.
It is assumed to be the least of its succesive elements.
 
 Loop 2 from (loop1_element+1---(i+1),n) is compared for every element of the previous loop
 
Both the loops traverse in forward direction"""
for i in range(0,n-1):
    for j in range(i+1,n):
      # if condition to check which element is smaller or of same value(duplicate).
      # Thus = is also used in teh condition.
      if a[i]>=a[j]:
      #Swapping is done if smaller elemnent is found at the back of the list than ith position.
        a[i],a[j]=a[j],a[i]

# output
print("list after sorting is",a)


# METHOD 2:
"""If the user is not sure of the length of the array,we can use a map
function to take the input as string and then convert it into list of numbers
and continue the sort function."""

#NOTE:here int keyword makes sure the input is of type integer,thus enforcing type security during conversion
# from string to int.Other alphabets or special charecters if found will be thrown as error
# The input is split by a demilimter comma is this case.

"""The map funtion returns an iterator object as result,thus a suitable iterator such as list,tuple etc must be
used in combination to get the output from it in a parsable format"""

#Take the input
a=list(map(int,input("Please enter the list of numbers ").split(",")))

#find the length
#As length of list is unknown,it is found by in-built len() function
n=len(a)

# Perform sorting
# The logic is same as above method
print("list before sorting",a)
for i in range(0,n-1):
    for j in range(i+1,n):
      if a[i]>=a[j]:
        a[i],a[j]=a[j],a[i]

# output
print("list after sorting is",a)

# METHOD 3:
"""The input is directly given in the code.
It can be taken in either of the above two methods"""

"""A function is used for the resuability of the code.
It seperates and constraints the sorting logic within the function 
block,thus giving a proper structure to the program unlike 
the monolithic programming construct."""


a=[2,3,5,1,9,4]

# A  function (in python def keyword is used) with the name sorting which
# takes a list is taken as the parameter.This parameter is called as arr.
def sorting(arr):

    # Logic is same as used in the above two methods
    n=len(arr)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] >= a[j]:
                a[i], a[j] = a[j], a[i]
    # The result is stored and returned to the argument which will be passed during the function call.
    return arr
# prints the ouput

# The function "sorting" is called with the argument a,which is out input.It prints the sorted
# list as output as the execution call goes to the sorting function block.
print(sorting(a))