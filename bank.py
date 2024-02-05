# weekly task 02 
# this program will 
# 1. Prompt the user and read in two money amounts (in cent)  2. Add the two amounts 3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Andre Hoarau
amount1 =float(input('Enter amount 1 (in cent) '))
amount2 =float(input ('enter amount 2 (in cent) '))
sum = (amount1 + amount2)
sum2= sum/100
sumprint=  f'The sum of these is €{sum2:.2f}'
print(sumprint)