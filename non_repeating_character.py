"""  To write a program to find the non-repeating character from a string

i/p-->a="My name is Amit Mahipal"
o/p--> y--if only first non-repeating alphabet to be considered
       y,s,e,h,t,p,l,n if all are to be printed
Assumption--->The string has only alphabets seperated by white spaces.
"""

# Take the input

"""All the String manipulation is done in a one-liner which is as follows

1.The white spaces are removed using the replace() function (white space is replaced with empty string) 
so all the words in the sentence come together.This makes parsing easier without the burden of white space

2.lower() is used to convert the uppercase alphabets to lower as it is easy to count the occurences of alphabet"""

str=(input("Please enter the input").replace(" ","")).lower()

# char is a list which is set of all unique/distict alphabets present in the given input string
# set is more like a hashtable,it is an un-ordered collection in python,thus the sequence
# occurence is at risk to change while checking iteration.

# Thus to freeze it and obtain an stable collection,list is used as conversion
# Using list fixes the set's element to a certain index untill the program specifically
# and explicilty asks to change the index postiton,unlike the set

char=list(set(str))

# For every alphabet in the list which considered as i,its occurences are checked with the string which is in
# lowercase and does not have whitespaces.
for i in char:

    # if the occurence (str.count(i)) is 1,it means it is non-repeating
    if str.count(i)==1:
        # all the non-repeating alphabets are printed
        print(i)



