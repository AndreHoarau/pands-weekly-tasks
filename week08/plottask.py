# A program that displays a normal distribution of 1000 values with mean of 5 and a standard deviation of 2 and a plot of the function h(x)=x^3 in the range of 0 to 10 on one set of axes.
# Make the plot look nice too
# Author Andre Hoarau
# First we need to import numpy and matplotlib
'''import numpy as np
import matplotlib.pyplot as plt
# For the histogram we need to generate our number array we also want to make sure that it is the same "random" array so we will seed it.
#The numpy.random.normal(mean, std deviation, size) source: https://www.w3schools.com/python/python_ml_normal_data_distribution.asp
np.random.seed(1)
array1= np.random.normal(5,2,1000)
print(array1)
#This was a check above and we are generating the same random array. Now we will generate the histogram source: https://www.w3schools.com/python/matplotlib_histograms.asp
plt.hist(array1)
plt.show()
# So far we have generated out array and successfully shown the histogram
# Now we need to plot h(x)=x^3
# Lets generate out range
x_values = np.arange(11)
# This generates range 0 to 10 inclusive/
y_values= x_values**3
#This cuves the x values
plt.plot(x_values, y_values)
plt.show()'''
# We then plot the values and show them with the histogram Source:https://w3schools.com/python/matplotlib_plotting.asp
#Now to make it look nicer.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
array1= np.random.normal(5,2,1000)
plt.hist(array1)
x_values = np.arange(11)
y_values= x_values**3
plt.plot(x_values, y_values)
#Label the x and y axis
plt.xlabel("Range")
plt.ylabel("Frequency")
# Let's add a title.
# Source for making it look nicer: https://www.w3schools.com/python/matplotlib_labels.asp
plt.title("Histogram 1000 Values Mean = 5, Std. Deviation = 2\n h(x)=x^3 (x 0-10 inclusive)")
plt.show()

