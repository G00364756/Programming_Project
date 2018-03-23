# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted
# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Adapted from code learned from lectures by Dr. Ian McGlouglin.
# Learned how to append to a list from python tutorial = https://docs.python.org/3/library/array.html?highlight=append#array.array.append

#Create a number of lists
sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
iris_class = []
s_l = []
s_w = []
p_l = []
p_w = []
i_c = []

with open("Data_sets/iris.csv") as f:#Open the csv file which will now be called "f"
    for line in f:
        jay = line.split(",") #for each line in the dataset split the lines into new individual lists e.g. [3.5,1.4,0.2,Iris-setosa][4.9,3.0,1.4,0.2,Iris-setosa]
        s_l.append(jay[0])    #Append the list "s_l" with the 1st value in each of the newly created lists

    for i in s_l:
        sepal_length.append(float(i)) #Convert all the values in "s_l" into float and append them to a new list called "sepal_length"
    v = sepal_length[0] + sepal_length[1] #add value in position 0 with value in position 2 to verifiy that the list contains floats and the correct values
    print((sepal_length[1]))
    print(len(sepal_length)) # count how many rows there are in the dataset