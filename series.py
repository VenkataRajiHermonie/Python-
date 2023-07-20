"""Write a program to generate a series when first two elements are given
where a=1,b=2

c=2*(b-a)=2
d=2*(c-b)=0
e=2*(d-c) and so on

Assuming the number of terms in the series "n" is not fixed and a and b are always same"""

# APPROACH:
"""The terms in the series are generated using the given expression 2*(b-a) where the values of 
a and b keep changing based on the updated value of the new term in the series"""


a=1
b=2

# User prompted to enter the total number of terms (a and b inclusive) to be present in the series
n=int(input("Enter the number of terms in the series"))

# The first two terms are printed as we know them
# end which is an optional parameter in the print statement is used to print all
# the terms in the same single line seperated by a blank space
print(a,b,end=" ")

# logic

# range is taken as n-2,as we already printed 2 of terms of the n numbered series
for i in range(n-2):

    # temp is a variable which is the new addition to the series as keeps on updating
    temp=2*(b-a)

    # after printing the new term,the values of the a,b are updated
    print(temp,end=" ")

    # a is the second last term of updation
    a=b

    # b is the new term which is just calculated and updated
    b=temp
