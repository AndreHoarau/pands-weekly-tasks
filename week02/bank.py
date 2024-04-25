# Week 02
# This program will 
# 1. Prompt the user and read in two money amounts (in cent)  2. Add the two amounts 3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Andre Hoarau
# Source: the slack channel had a discussion for the use of remainder 
# Other Sources: 
# Request the first and second amounts as inputs in cent. We want to avoid floating point numbers so specifying int here will ensure the input is only an integer.
# We cannot have a parital cent so this makes sense.
amount1 =int(input('Enter amount 1 (in cent) '))
amount2 =int(input ('enter amount 2 (in cent) '))
# We then add the 2 amounts together.
sum = (amount1 + amount2)
# We then get our euro amount by dividing the cents by 100. // Is integer division so it will always round down to the nearest int.
integer= sum // 100
remainder = sum%100
sumprint=  f'The sum of these is €{integer}.{remainder}'
print(sumprint)