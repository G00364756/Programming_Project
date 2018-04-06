# Aidan O'Connor - G00364756 - 05/04/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted

# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Below code adapted from following link = https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# Created formulas in tryit.py and using them in iris.py to create histograms

# Code to identify the mode of a data set. Will be adapted to return a bar chart of the mean of the mode of the data set.

John = [4.9,4.6,5.3,2.4,2.5,2.1]
Range1 = []
Range2 = []
Range = []
G1 = [float(x/10) for x in range(0, 10,1)] # list of values minus mean
G2 = [float(x/10) for x in range(10, 20,1)]
G3 = [float(x/10) for x in range(20, 30,1)]

for m in G3:
    for i in John:
        if i == m:
            Range.append(i)


lenGroup1 = len(Range)
print(Range)
print(G1)