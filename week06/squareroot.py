# This program will tale a positive floating point number and return an approximate square root.
# Author Andre Hoarau

# Let's get the input we need
#squarerootfind =float(input("Please input a positive number: "))
#Newton's method of square root approximation is based on refinement of a estimate of the square root until the difference between the new guess and the old guess is close enough
# to the square root
# we will just fill in the guess and let the program refine on it 
#guess1 = 1
#approximate = (guess1 + (squarerootfind/guess1))/2
# We will refine until the difference between the 2 guesses is 0.001
#while guess1 - approximate >= 0.001:

# so we define the functions to base it from a guess of one and a tolerance 0.001 
#def sqrt(squarerootfind):
#    guess1 = 1
#    approximate = (guess1 + (squarerootfind/guess1))/2
#    while guess1 - approximate >= 0.001:
#        approximate = (guess1 + (squarerootfind/guess1))/2
#    print(f"The square root of {squarerootfind} is approx {approximate}")
#squarerootfind =float(input("Please input a positive number: "))
#sqrt(squarerootfind)
# Lets refine it I realised I was not updating the guess so did that also added abs to ensure the difference isn't negative. # I also rounded the answer to 1 decimal as per the example.
def sqrt(squarerootfind):
    guess1 = squarerootfind/2
    approximate = (guess1 + (squarerootfind/guess1))/2
    while abs(guess1 - approximate) >= 0.000000001:
        guess1 = approximate
        approximate = (guess1 + (squarerootfind/guess1))/2
    approximatefinal= round(approximate,1)
    print(f"The square root of {squarerootfind} is approx {approximatefinal}")
squarerootfind =float(input("Please input a positive number: "))
sqrt(squarerootfind)
# sources: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo I also used chatgpt to dumb down the logic of how to arrive at the square root for me.

