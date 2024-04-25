# Week 03
# this program reads in 10 character account number and outputs the account number with only the last 4 digits showing and the first 6 digits replaced with xs.
# author: Andre Hoarau 
# reference: https://www.w3schools.com/python/python_strings_slicing.asp

acnnumber = input('Please enter a 10 digit account number: ')
sliceacn = (acnnumber[6: ])
print('XXXXXX{}' .format(sliceacn))
# extra getting the program to deal with accout numbers of any length 
# need to consider negative indexing as opposed to slice to the end 
acnnumber2= input('Enter an account numebr of any length: ')
sliceanyacn = (acnnumber2[-4:])
acnprecursor= (acnnumber2[:-4])
#need to convert this to all xs now replace function I can take the len of the acn number to be converted and multiply by X
xconvert= len(acnprecursor) * "X"
print( "{}{}".format(xconvert,sliceanyacn))