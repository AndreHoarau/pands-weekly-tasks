# program to subtract one number from another and list it as a sentence
# author Andre Hoarau
number_one = int(input('enter first number: '))
number_two = int(input('enter second number: '))
answer = number_one - number_two
print('{}  minus {} is {}'.format(number_one , number_two , answer))
# entering a non int number into the variables throws an error as we specidied on the input that int is required.
