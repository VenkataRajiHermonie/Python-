"""Swapping two integers without using a third/temporary variable
or in built function

i/p--->x=10,y=20
o/p--->x=20,y=10"""

"""APPROACH 
This type of swapping can be done using arithmetic operations of addition and subraction.
it based on the associative law of integers which says

a+b=b+a

Step1: we add both the numbers into the any one of the integer
step2: we subract the other number from both the integers.
Step3:Swapping is done by the difference of the numbers is taken out of the updated integer"""

# User input is taken with type restriction as int
a=int(input("Enter the first integer"))
b=int(input("Enter the second integer"))

print("Integers before swapping a is",a,"b is ",b)

# Both the integers are summed and stored in a.Now a updated to a new value
a=a+b

# The updated value of a is reduced/subracted from the original b value.thus it changes to
# the inital value of a.
b=a-b

# Now the value swapped value of b is subracted from the sum (new value of a).Thus it has the
# initial value of b.
a=a-b

print("Integers after swapping a is",a,"b is ",b)

