# Week 03
# This program reads in 10 character account number and outputs the account number with only the last 4 digits showing and the first 6 digits replaced with xs.
# Author: Andre Hoarau 

# Ask the user to input the 10 digit account number.
acnnumber = input('Please enter a 10 digit account number: ')
# We then slice the account number starting from the index to 6 from the end this will give us the last 4 digits.
sliceacn = (acnnumber[6: ])
# We then print the first 6 xs and add the last 4 digits.
print('XXXXXX{}' .format(sliceacn))
# Extra getting the program to deal with account numbers of any length. 
# Need to consider negative indexing as opposed to slice to the end.
# We ask for an account number of any length.
acnnumber2= input('Enter an account number of any length: ')
# We then negative index to take the last 4 digits and all the digits before the last 4 digits.
sliceanyacn = (acnnumber2[-4:])
acnprecursor= (acnnumber2[:-4])
# Need to convert this to all xs now replace function I can take the len of the acn number to be converted and multiply by X
xconvert= len(acnprecursor) * "X"
print( "{}{}".format(xconvert,sliceanyacn))

# References: This had the information on string slicing https://www.w3schools.com/python/python_strings_slicing.asp