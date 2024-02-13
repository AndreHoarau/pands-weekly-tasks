# write a program that prints out a random fruit
# author Andre Hoarau
# found the random.choise at w3 schools
# updated version to use a tuple and not a list as the values do not change
import random
fruit= ("banana", "grapes", "watermelon")
print("the random fruit is {}" .format(random.choice(fruit)))