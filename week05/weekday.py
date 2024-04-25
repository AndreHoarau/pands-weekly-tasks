# Week 05
# This program outputs whether or not today is a weekday
# If it is a weekday the program will say "Yes, unfortunately today is a weekday." otherwise it will say "It is the weekend, yay!"
# Author: Andre Hoarau
# Date is not a python data type so we import datetime
import datetime
# datetime.datetime.now() give thes current date
# We can use strftime() method to construct a readable string of the date where we just look at the day of the week.
today = datetime.datetime.now()
todaystring =today.strftime("%A")
# We could just use an if statment and list all the days with ors but lets try use a dictionary to define our weekdays and weekends with a key and then a tuple in the value 
daysofweek= {"Weekday":("Monday","Tuesday","Wednesday","Thursday","Friday"),"Weekend":("Saturday,Sunday")}
#Lets look at the dictionary and compare to the date
if todaystring in daysofweek["Weekday"]:
    print("Yes, unfortunately today is a weekday.")
else: 
    print("It is the weekend, yay!")
# Sources: https://www.w3schools.com/python/python_datetime.asp 
# Asked ChatGPT to clarify how to probe the key value pairs in the dictionray
# Was also able to test this be manual input of the date to see if the weekend values change and it does. Will test again on a weekend! 