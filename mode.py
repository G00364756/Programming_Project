# Aidan O'Connor - G00364756 - 05/04/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted

# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Below code adapted from following link = https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# Created formulas in tryit.py and using them in iris.py to create histograms

# Code to identify the mode of a data set. Will be adapted to return a bar chart of the mean of the mode of the data set.

def Plotmode(x):

    def splitSetosa(x): # Same as code in max_iris.py
        """Splits the original iris dataset into a list containing only Iris Setosa class with all the attributes i.e. Setosa = [[5.1,3.5,1.4,0.2,Iris-Setosa]...[5.0,3.3,1.4,0.2,Iris-Setosa]]"""
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

    def splitVersicolor(x): # Same as code in max_iris.py
        """Splits the original Iris dataset into a list containing only Iris Versicolor class with all the attributes i.e. Versicolor = [[5.1,3.5,1.4,0.2,Iris-Versiolor]...[5.0,3.3,1.4,0.2,Iris-Versicolor]]"""
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


    def splitVirginica(x): # Same as code in max_iris.py
        """Splits the original Iris dataset into a list containing only Iris Virginica class with all the attributes i.e. Setosa = [[5.1,3.5,1.4,0.2,Iris-Virginica]...[5.0,3.3,1.4,0.2,Iris-Virginica]]"""
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

    def modeSetosavalue(x):
        """return the estimated mode of the data for a particular attribute"""
        Mickey = [] # creates list Mickey
        if x > 3 or x < 0: # Only allows user to pick a number from 0 to 3
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width") # text to be included if user picks a number outside 0 to 3
            return(text) # return the text if user picks a number outside 0 to 3
        elif x>=0 or x<=3: # if 0 to 3 is selected by the user do the following...
            for m in range(len(splitSetosa(0))): 
                Mickey.append(float(splitSetosa(0)[m][x])) # Append Mickey with the values in splitSetosa specified by the user and convert them to the float type
        R1 = [] # Create 8 different lists R1 to R8
        R2 = []
        R3 = []
        R4 = []
        R5 = []
        R6 = []
        R7 = []
        R8 = []
        G1 = [float(n/10) for n in range(0, 10,1)] # Create list G1 to G8 that specifies the groups i.e. G1 = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        G2 = [float(n/10) for n in range(10, 20,1)]
        G3 = [float(n/10) for n in range(20, 30,1)]
        G4 = [float(n/10) for n in range(30, 40,1)]
        G5 = [float(n/10) for n in range(40, 50,1)]
        G6 = [float(n/10) for n in range(50, 60,1)]
        G7 = [float(n/10) for n in range(60, 70,1)]
        G8 = [float(n/10) for n in range(70, 80,1)]
        for m in G1: # for all the values in G1
            for i in Mickey: # and for all the values in Mickey
                if m == i: # if a value of G1 is equal to one of the values in Mickey do the following...
                    R1.append(i) # append the list R1 with the value of i that has been identified as equal
        for m in G2:
            for i in Mickey:
                if m == i:
                    R2.append(i)
        for m in G3:
            for i in Mickey:
                if m == i:
                    R3.append(i)
        for m in G4:
            for i in Mickey:
                if m == i:
                    R4.append(i)
        for m in G5:
            for i in Mickey:
                if m == i:
                    R5.append(i)
        for m in G6:
            for i in Mickey:
                if m == i:
                    R6.append(i)
        for m in G7:
            for i in Mickey:
                if m == i:
                    R7.append(i)
        for m in G8:
            for i in Mickey:
                if m == i:
                    R8.append(i)

        TupleG1 = len(R1) # Create a variable that is equal to the length of the R1 list, and so on...
        TupleG2 = len(R2)
        TupleG3 = len(R3)
        TupleG4 = len(R4)
        TupleG5 = len(R5)
        TupleG6 = len(R6)
        TupleG7 = len(R7)
        TupleG8 = len(R8)
        Groupings = [TupleG1,TupleG2,TupleG3,TupleG4,TupleG5,TupleG6,TupleG7,TupleG8] # create a list out of the variables created above
        mode = max(Groupings) # The estimate mode is the group that is the largest within the list Groupings
        # The below code deals with returning the estimated mode of the data set, this was formulated from mathematics identified in the research part of the project
        if mode == TupleG1: # if the mode is equal to the 1st value in the list Groupings then do the following...
            fminus1 = 0
            f = len(R1)
            fplus1 = len(R2)
            L = 0
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG2:
            fminus1 = len(R1)
            f = len(R2)
            fplus1 = len(R3)
            L = 0.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG3:
            fminus1 = len(R2)
            f = len(R3)
            fplus1 = len(R4)
            L = 1.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG4:
            fminus1 = len(R3)
            f = len(R4)
            fplus1 = len(R5)
            L = 2.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG5:
            fminus1 = len(R4)
            f = len(R5)
            fplus1 = len(R6)
            L = 3.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG6:
            fminus1 = len(R5)
            f = len(R6)
            fplus1 = len(R7)
            L = 4.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG7:
            fminus1 = len(R6)
            f = len(R7)
            fplus1 = len(R8)
            L = 5.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG8:
            fminus1 = len(R7)
            f = len(R8)
            fplus1 = 0
            L = 6.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        else:
            return("Mode outside the defined groupings!") # if the mode is not within the Groupings then return the text

    def modeVersicolorvalue(x): # This code does the exact same as the modeSetosavalue(x) code, except for the Versicolor iris class
        """return the estimated mode of the data for a particular attribute"""
        Mickey = []
        if x > 3 or x < 0: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitVersicolor(0))):
                Mickey.append(float(splitVersicolor(0)[m][x]))
        R1 = []
        R2 = []
        R3 = []
        R4 = []
        R5 = []
        R6 = []
        R7 = []
        R8 = []
        G1 = [float(n/10) for n in range(0, 10,1)] # list of values minus mean
        G2 = [float(n/10) for n in range(10, 20,1)]
        G3 = [float(n/10) for n in range(20, 30,1)]
        G4 = [float(n/10) for n in range(30, 40,1)]
        G5 = [float(n/10) for n in range(40, 50,1)]
        G6 = [float(n/10) for n in range(50, 60,1)]
        G7 = [float(n/10) for n in range(60, 70,1)]
        G8 = [float(n/10) for n in range(70, 80,1)]
        for m in G1:
            for i in Mickey:
                if m == i:
                    R1.append(i)
        for m in G2:
            for i in Mickey:
                if m == i:
                    R2.append(i)
        for m in G3:
            for i in Mickey:
                if m == i:
                    R3.append(i)
        for m in G4:
            for i in Mickey:
                if m == i:
                    R4.append(i)
        for m in G5:
            for i in Mickey:
                if m == i:
                    R5.append(i)
        for m in G6:
            for i in Mickey:
                if m == i:
                    R6.append(i)
        for m in G7:
            for i in Mickey:
                if m == i:
                    R7.append(i)
        for m in G8:
            for i in Mickey:
                if m == i:
                    R8.append(i)

        TupleG1 = len(R1)
        TupleG2 = len(R2)
        TupleG3 = len(R3)
        TupleG4 = len(R4)
        TupleG5 = len(R5)
        TupleG6 = len(R6)
        TupleG7 = len(R7)
        TupleG8 = len(R8)
        Groupings = [TupleG1,TupleG2,TupleG3,TupleG4,TupleG5,TupleG6,TupleG7,TupleG8]
        mode = max(Groupings)
        #The below code deals with returning the estimated mode of the data set
        if mode == TupleG1:
            fminus1 = 0
            f = len(R1)
            fplus1 = len(R2)
            L = 0
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG2:
            fminus1 = len(R1)
            f = len(R2)
            fplus1 = len(R3)
            L = 0.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG3:
            fminus1 = len(R2)
            f = len(R3)
            fplus1 = len(R4)
            L = 1.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG4:
            fminus1 = len(R3)
            f = len(R4)
            fplus1 = len(R5)
            L = 2.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG5:
            fminus1 = len(R4)
            f = len(R5)
            fplus1 = len(R6)
            L = 3.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG6:
            fminus1 = len(R5)
            f = len(R6)
            fplus1 = len(R7)
            L = 4.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG7:
            fminus1 = len(R6)
            f = len(R7)
            fplus1 = len(R8)
            L = 5.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG8:
            fminus1 = len(R7)
            f = len(R8)
            fplus1 = 0
            L = 6.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        else:
            return("Mode outside the defined groupings!")

    def modeVirginicavalue(x):  # This code does the exact same as the modeSetosavalue(x) code, except for the Viriginica iris class
        """return the estimated mode of the data for a particular attribute"""
        Mickey = []
        if x > 3 or x < 0: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitVirginica(0))):
                Mickey.append(float(splitVirginica(0)[m][x]))
        R1 = []
        R2 = []
        R3 = []
        R4 = []
        R5 = []
        R6 = []
        R7 = []
        R8 = []
        G1 = [float(n/10) for n in range(0, 10,1)] # list of values minus mean
        G2 = [float(n/10) for n in range(10, 20,1)]
        G3 = [float(n/10) for n in range(20, 30,1)]
        G4 = [float(n/10) for n in range(30, 40,1)]
        G5 = [float(n/10) for n in range(40, 50,1)]
        G6 = [float(n/10) for n in range(50, 60,1)]
        G7 = [float(n/10) for n in range(60, 70,1)]
        G8 = [float(n/10) for n in range(70, 80,1)]
        for m in G1:
            for i in Mickey:
                if m == i:
                    R1.append(i)
        for m in G2:
            for i in Mickey:
                if m == i:
                    R2.append(i)
        for m in G3:
            for i in Mickey:
                if m == i:
                    R3.append(i)
        for m in G4:
            for i in Mickey:
                if m == i:
                    R4.append(i)
        for m in G5:
            for i in Mickey:
                if m == i:
                    R5.append(i)
        for m in G6:
            for i in Mickey:
                if m == i:
                    R6.append(i)
        for m in G7:
            for i in Mickey:
                if m == i:
                    R7.append(i)
        for m in G8:
            for i in Mickey:
                if m == i:
                    R8.append(i)

        TupleG1 = len(R1)
        TupleG2 = len(R2)
        TupleG3 = len(R3)
        TupleG4 = len(R4)
        TupleG5 = len(R5)
        TupleG6 = len(R6)
        TupleG7 = len(R7)
        TupleG8 = len(R8)
        Groupings = [TupleG1,TupleG2,TupleG3,TupleG4,TupleG5,TupleG6,TupleG7,TupleG8]
        mode = max(Groupings)
        #The below code deals with returning the estimated mode of the data set
        if mode == TupleG1:
            fminus1 = 0
            f = len(R1)
            fplus1 = len(R2)
            L = 0
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG2:
            fminus1 = len(R1)
            f = len(R2)
            fplus1 = len(R3)
            L = 0.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG3:
            fminus1 = len(R2)
            f = len(R3)
            fplus1 = len(R4)
            L = 1.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG4:
            fminus1 = len(R3)
            f = len(R4)
            fplus1 = len(R5)
            L = 2.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG5:
            fminus1 = len(R4)
            f = len(R5)
            fplus1 = len(R6)
            L = 3.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG6:
            fminus1 = len(R5)
            f = len(R6)
            fplus1 = len(R7)
            L = 4.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG7:
            fminus1 = len(R6)
            f = len(R7)
            fplus1 = len(R8)
            L = 5.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        elif mode == TupleG8:
            fminus1 = len(R7)
            f = len(R8)
            fplus1 = 0
            L = 6.9
            w = 0.9
            Estmode = ((L +(f-fminus1)/((f-fminus1)+(f-fplus1))))
            return(Estmode)
        else:
            return("Mode outside the defined groupings!")

    x1 = (modeSetosavalue(x)) # set x1 to the value for modeSetosavalue(x)
    x2 = (modeVersicolorvalue(x)) # set x2 to the value for modeVersicolorvalue(x)
    x3 = (modeVirginicavalue(x)) # set x3 to the value for modeVirginicavalue(x)
    import matplotlib.pyplot as plt # import the library to plot graphs
    
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
        plt.title('Estimated Mode for Sepal Length bar chart')
    elif x == 1:
         #title is Sepal Width if x = 1
        plt.title('Estimated Mode for Sepal Width bar chart')
    elif x == 2:
         #title is Petal Length if x = 2
        plt.title('Estimated Mode for Petal Length bar chart')
    elif x == 3:
         #title is Petal Width if x = 3
        plt.title('Estimated Mode for Petal Width bar chart')    
    # function to show the plot
    plt.show()

Plotmode(x = int(input("0 = Sepal Length,\n1 = Sepal Width,\n2 = Petal Length,\n3 = Petal Width,\nEnter the number you wish to plot:")))