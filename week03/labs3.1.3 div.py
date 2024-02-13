# a program that reads in two number and divdes the first one by the second and give the intefer result and the remainder
# Author Andre Hoarau
x = int(input("enter a first number "))
y = int(input("enter a second number "))
answer = int(x/y)
remainder= x%y
print( "{} divided by {} is {} with remainder {}" .format (x , y ,answer, remainder))