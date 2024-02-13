# write a program that prints out a random fruit
# author Andre Hoarau
# found the random.choise at w3 schools
# i also will include Andrew's solution
import random
fruit= ["banana", "grapes", "watermelon"]
print("the random fruit is {}" .format(random.choice(fruit)))

fruits = [ "pineapple" , "papaya", "kiwi"]
index = random.randint (0,len(fruits) - 1)
fruit2 = fruits [index]
print (" a random fruit: {}" .format(fruit2))