# program that prints out a random number between 1 and 10
# author Andre Hoarau
import random
number = random.randint (1,10)
print (" the random number is {}" .format (number))
#extra step then to get the user to specifiy the range
import random
lower= int(input (" input the lower range "))
upper = int(input (" input the upper range "))
number = random.randint (lower,upper)
print (" the random number is {}" .format (number)) 
