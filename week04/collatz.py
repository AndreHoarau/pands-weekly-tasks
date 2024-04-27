# Week 04
# Write a program that instructs a user to input any positive integer.
# The program will then divide the number by 2 if it is even or multiply it by 3 and add 1 if it is odd.
# The program will keep doing this with the previous integer until it reaches 1, at which point the program will end.
# The program will list all the numbers it took to get to 1.
# Author: Andre Hoarau

# Let's set up our list.
initial = int(input(" Input a positive integer: "))
list1 = [initial]
# The initial number entered is part of list 1.
# While the number 'initial' is not equal to 1, we need to determine if it is even or odd. If it is even, then we need to divide by 2; otherwise, we need to multiply by 3 and add 1.
while initial != 1:
    # So if there is a modulus remainder of 0 it is even.
    if initial % 2 == 0:
        initial= int(initial / 2)
    # Otherwise it is odd.
    else:
       initial =  int((initial * 3) +1)
# We then want to add the new 'initial' value to the old 'initial' value, so we append it.
    list1.append(initial)
# Once the loop is exited, we can then print the list.
print(f"{list1}")

# Source: I looked at lists and looping lists on W3Schools: https://www.w3schools.com/python/python_lists_loop.aspn