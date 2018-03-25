# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted
# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Adapted from code learned from lectures by Dr. Ian McGlouglin.

#This code splits the data set into the 3 different classes of iris and find the maximum sepal length for each class

def splitSetosa(x):
    """Splits the original iris dataset into a list containing only iris setosa class with all the attributes i.e. Setosa = [[5.1,3.5,1.4,0.2,Iris-setosa]...[5.0,3.3,1.4,0.2,Iris-setosa]]"""
    Dataset=[]
    Setosa=[]
    with open("Data_sets/iris.csv") as f:
        for line in f:  
            Dataset.append(line.split(","))
        for x in range(len(Dataset)):
            for i in Dataset[x]:
                if i == "Iris-setosa\n":
                    Setosa.append(Dataset[x])
                else:
                    continue
        return(Setosa)


def splitVersicolor(x):
    """Splits the original iris dataset into a list containing only iris setosa class with all the attributes i.e. Setosa = [[5.1,3.5,1.4,0.2,Iris-setosa]...[5.0,3.3,1.4,0.2,Iris-setosa]]"""
    Dataset=[]
    Versicolor=[]
    with open("Data_sets/iris.csv") as f:
        for line in f:  
            Dataset.append(line.split(","))
        for x in range(len(Dataset)):
            for i in Dataset[x]:

                if i =="Iris-versicolor\n":
                    Versicolor.append(Dataset[x])
                else:
                    continue
        return(Versicolor)


def splitVirginica(x):
    """Splits the original iris dataset into a list containing only iris setosa class with all the attributes i.e. Setosa = [[5.1,3.5,1.4,0.2,Iris-setosa]...[5.0,3.3,1.4,0.2,Iris-setosa]]"""
    Dataset=[]
    Virginica=[]
    with open("Data_sets/iris.csv") as f:
        for line in f:  
            Dataset.append(line.split(","))
        for x in range(len(Dataset)):
            for i in Dataset[x]:
                if i =="Iris-virginica\n":
                    Virginica.append(Dataset[x])
                else:
                    continue
        return(Virginica)

#IMPORTANT NOTE: The below definitions are reliant on the above definitions.
def maxSetosavalue(x):
    """Returns the maximum value for an attribute that belongs to the Setosa class i.e. Max sepal length for the setosa class is 5.8cm"""
    #Change the value of x to change the attribute you want to find the max of
    Mickey = []
    maximumvalue = 0
    if x > 3: 
        text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
        return(text)
    elif x>=0 or x<=3:
        for m in range(len(splitSetosa(0))):
                Mickey.append(splitSetosa(0)[m][x])
        maximumvalue = float(max(Mickey))
        #The below if statements ensure the value of x is connected with the right attribute name i.e. 0 = sepal length, 1 = sepal width...)
        if x == 0:
            return(('{}{}{}'.format("The maximum sepal length for the Iris-Setosa class is ", maximumvalue, "cm")))
        elif x == 1:
            return(('{}{}{}'.format("The maximum sepal width for the Iris-Setosa class is ", maximumvalue, "cm")))
        elif x == 2:
            return(('{}{}{}'.format("The maximum petal length for the Iris-Setosa class is ", maximumvalue, "cm")))
        elif x == 3:
            return(('{}{}{}'.format("The maximum petal width for the Iris-Setosa class is ", maximumvalue, "cm")))
        else:
            pass
    else:
        pass
print(maxSetosavalue(0))

def maxVersicolorvalue(x):
    Minnie = []
    maximumvalue = 0
    if x > 3: 
        text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
        return(text)
    elif x>=0 or x<=3:
        for m in range(len(splitVersicolor(0))):
            Minnie.append(splitVersicolor(0)[m][x])
        maximumvalue = float(max(Minnie))
        #The below if statements ensure the value of x is connected with the right attribute name i.e. 0 = sepal length, 1 = sepal width...)
        if x == 0:
            return(('{}{}{}'.format("The maximum sepal length for the Iris-Versicolor class is ", maximumvalue, "cm")))
        elif x == 1:
            return(('{}{}{}'.format("The maximum sepal width for the Iris-Versicolor class is ", maximumvalue, "cm")))
        elif x == 2:
            return(('{}{}{}'.format("The maximum petal length for the Iris-Versicolor class is ", maximumvalue, "cm")))
        elif x == 3:
            return(('{}{}{}'.format("The maximum petal width for the Iris-Versicolor class is ", maximumvalue, "cm")))
        else:
            pass


def maxVirginicavalue(x):
    Pluto = []
    maximumvalue = 0
    if x > 3: 
        text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
        return(text)
    elif x>=0 or x<=3:
        for m in range(len(splitVirginica(0))):
                Pluto.append(splitVirginica(0)[m][x])
        maximumvalue = float(max(Pluto))
        #The below if statements ensure the value of x is connected with the right attribute name i.e. 0 = sepal length, 1 = sepal width...)
        if x == 0:
            return(('{}{}{}'.format("The maximum sepal length for the Iris-Virginica class is ", maximumvalue, "cm")))
        elif x == 1:
            return(('{}{}{}'.format("The maximum sepal width for the Iris-Virginica class is ", maximumvalue, "cm")))
        elif x == 2:
            return(('{}{}{}'.format("The maximum petal length for the Iris-Virginica class is ", maximumvalue, "cm")))
        elif x == 3:
            return(('{}{}{}'.format("The maximum petal width for the Iris-Virginica class is ", maximumvalue, "cm")))
        else:
            pass