#This program will read in a txt file and output the number of e's that it contains. 
# Author Andre Hoarau
# I will initially build for just the txt file and then will handle error handling 
# Lets define out filename 
'''FILENAME = "test.txt"
#Lets create a function that opens that file in read mode. It then returns the count of the letter based on the read.
def ecounter():
    with open(FILENAME,'r') as f:
        lines = f.read()
        letter = 'e'
        return lines.count(letter)
# print the function to test it
print(ecounter())
# So far this will count a file that exists. '''
# Source that was helpful was https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# I also read the W3 Schools pieve on files here: https://www.w3schools.com/python/python_file_handling.asp
# Looking at the file name as an argument on the command line now 
# From: https://www.geeksforgeeks.org/command-line-arguments-in-python/ and ChatGPT simplifying it for me 
# Need to import the module for arguments sys
import sys
#Need to import OS to check the file for more error handling
import os
#We cannot use filename like above as we need to be able to pass an argument to it.
def ecounter(letter, filename):
    with open(filename,'r') as f:
        return filename.count(letter)
#Need to ensure we have the correct amount of arguments
if len(sys.argv) != 3:
    print("The usage includes python .\es.py <letter>, <filename>")
    sys.exit(1)
#Extract command line arguments:
    
letter = sys.argv[1]
filename =sys.argv[2]
if not os.path.exists(filename):
    print("This file name does not exist")
    sys.exit(1)
elif not filename.lower().endswith('.txt'):
    print("This is not a text file")
    sys.exit(1)
letter = sys.argv[1]
filename =sys.argv[2]
# print the function to test it
print(ecounter(letter,filename))
# Next to deal with error handling



