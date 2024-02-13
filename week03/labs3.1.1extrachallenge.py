# extra program question
# author Andre Hoarau
#message = 'I have eaten ' + 99 + ' burritos.'
#print (message)
# message creates an error as we are using the old format and the message needs to be all of one type in this case string
message = f"I have eaten " + str(99) + " burritos."
print (message)
# eggs is a valid variable name and 100 is not as variables cannot begin with a number 
# 3 functions to get integer floating point number or string version of a value are = int, fl, str.