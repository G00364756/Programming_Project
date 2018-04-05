# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted

# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Below code adapted from following link = https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# Created formulas in tryit.py and using them in iris.py to create histograms

# Creates a Histogram for the mean value for Sepal Length, Sepal Width, Petal Length and Petal Width for each of the Iris classes

def plotMean(x):

    def splitSetosa(x):
        """Splits the original iris dataset into a list containing only iris setosa class with all the attributes i.e. Setosa = [[5.1,3.5,1.4,0.2,Iris-setosa]...[5.0,3.3,1.4,0.2,Iris-setosa]]"""
        Dataset=[]
        Setosa=[]
        with open("iris.csv") as f:
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
        with open("iris.csv") as f:
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
        with open("iris.csv") as f:
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
    def meanSetosavalue(x):
        """Returns the maximum value for an attribute that belongs to the Setosa class i.e. Max sepal length for the setosa class is 5.8cm"""
        #Change the value of x to change the attribute you want to find the max of
        Mickey = []
        meanvalue = 0
        if x > 3: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitSetosa(0))):
                    Mickey.append(float(splitSetosa(0)[m][x]))
            meanvalue = (sum(Mickey))/(float(len(Mickey)))
            return(meanvalue)


    def meanVersicolorvalue(x):
        Minnie = []
        meanvalue = 0
        if x > 3: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitVersicolor(0))):
                Minnie.append(float(splitVersicolor(0)[m][x]))
            meanvalue = (sum(Minnie))/(float(len(Minnie)))
            return(meanvalue)


    def meanVirginicavalue(x):
        Pluto = []
        meanvalue = 0
        if x > 3: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitVirginica(0))):
                    Pluto.append(float(splitVirginica(0)[m][x]))
            meanvalue = (sum(Pluto))/(float(len(Pluto)))
            return(meanvalue)



    x1 = (meanSetosavalue(x))
    x2 = (meanVersicolorvalue(x))
    x3 = (meanVirginicavalue(x))

    import matplotlib.pyplot as plt
    
    # x-coordinates of left sides of bars 
    left = [1, 2, 3]
    
    # heights of bars
    height = [x1, x2, x3]
    
    # labels for bars
    tick_label = ['Setosa', 'Versicolor', 'Verginica']
    
    # plotting a bar chart
    plt.bar(left, height, tick_label = tick_label,
            width = 0.8, color = ['red', 'green','blue'])
    
    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')
    # plot title
    if x == 0:    
        #title is Sepal length if x = 0
        plt.title('Mean Sepal Length bar chart')
    elif x == 1:
         #title is Sepal Width if x = 1
        plt.title('Mean Sepal Width bar chart')
    elif x == 2:
         #title is Petal Length if x = 2
        plt.title('Mean Petal Length bar chart')
    elif x == 3:
         #title is Petal Width if x = 3
        plt.title('Mean Petal Width bar chart')    
    # function to show the plot
    plt.show()

plotMean(x = int(input("0 = Sepal Length,\n1 = Sepal Width,\n2 = Petal Length,\n3 = Petal Width,\nEnter the number you wish to plot:")))