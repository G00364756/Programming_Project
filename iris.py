# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted

# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Below code copied from following link = https://pythonspot.com/matplotlib-histogram/ - Will be adapted to use for the iris dataset

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
 
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5 #states how many bins there will be in the histogram
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
