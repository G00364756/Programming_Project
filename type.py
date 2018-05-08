# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted
# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Adapted from code learned from lectures by Dr. Ian McGlouglin.

# This code splits the data set into the 3 different classes of iris and find the maximum sepal length for each class.
# It was the first development of the list.py and list.py was adapted from type.py

Ace=[]
King=[]
Queen=[]
Jack=[]
with open("iris.csv") as f:
    for line in f:  
        Ace.append(line.split(","))
    for x in range(len(Ace)):
        for i in Ace[x]:
            if i == "Iris-setosa\n":
                King.append(Ace[x])
            elif i =="Iris-versicolor\n":
                Queen.append(Ace[x])
            elif i =="Iris-virginica\n":
                Jack.append(Ace[x])
            else:
                continue
    #end of first part
    Mickey = []
    for m in range(len(King)):
            Mickey.append(King[m][0])
    print('{}{}{}'.format("The maximum sepal length for the Iris Setosa class is ", max(Mickey), "cm"))
    Minnie = []
    for m in range(len(Queen)):
            Minnie.append(Queen[m][0])
    print('{}{}{}'.format("The maximum sepal length for the Iris Versicolor class is ", max(Minnie), "cm"))
    Pluto = []
    for m in range(len(Jack)):
            Pluto.append(Jack[m][0])
    print('{}{}{}'.format("The maximum sepal length for the Iris Virginica class is cm ",max(Pluto), "cm"))