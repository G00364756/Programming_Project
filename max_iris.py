# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted

# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Below code adapted from following link = https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# Created formulas in tryit.py and using them in max_iris.py to create histograms

# Creates a Histogram for the maximum value for Sepal Length, Sepal Width, Petal Length and Petal Width for each of the Iris classes

def plotHisto(x): # Overarching formula which has formulas within it 

    def splitSetosa(x):
        """Splits the original iris dataset into a list containing only Iris Setosa class with all the attributes i.e. Setosa = [[5.1,3.5,1.4,0.2,Iris-Setosa]...[5.0,3.3,1.4,0.2,Iris-Setosa]]"""
        Dataset=[] # list created for "Dataset"
        Setosa=[] # list created for "Setosa"
        with open("iris.csv") as f: # opens the data file "iris.csv" and names the file "f"
            for line in f:  # for all the lines in "f" do the following...
                Dataset.append(line.split(",")) # split up the values in each line for the data set by recognising the comma (,) as the delimiter and add the values to the list named "Dataset"
            for x in range(len(Dataset)): # finds the number of values in the list "Dataset", uses the number of values as the range and iterates through the range by 1 every time. Acts as a counter. For each iteration do...
                for i in Dataset[x]: # for i in the Dataset list indexed x do the following...
                    if i == "Iris-setosa\n": # if i is equal to the string then do the following...
                        Setosa.append(Dataset[x]) # append the setosa array with the list indexed x in "Dataset"
                    else: # otherwise...
                        continue # keep going with the code
            return(Setosa) # return the list Setosa


    def splitVersicolor(x): # Does the exact same as splitSetosa formula except does it for the Versicolor Iris class
        """Splits the original iris dataset into a list containing only Iris Versicolor class with all the attributes i.e. Versicolor = [[5.1,3.5,1.4,0.2,Iris-Versicolor]...[5.0,3.3,1.4,0.2,Iris-Versicolor]]"""
        Dataset=[] # list created for "Dataset"
        Versicolor=[] # list created for "Versicolor"
        with open("iris.csv") as f: # opens the data file "iris.csv" and names the file "f"
            for line in f:  # for all lines in "f" do the following...
                Dataset.append(line.split(",")) # split up the values in each line for the data set by recognising the comma (,) as the delimiter and add the value to the list named "Dataset"
            for x in range(len(Dataset)): # finds the number of values in the list "Dataset", uses the number of values as the range and iterates through the range by 1 every time. Acts as a counter. For each iteration do...
                for i in Dataset[x]: # for i in the Dataset list indexed x do the following...
                    if i =="Iris-versicolor\n": # if i is equal to the string then do the following...
                        Versicolor.append(Dataset[x]) # append the setosa array with the list indexed x in "Dataset"
                    else: # otherwise...
                        continue # keep going with the code
            return(Versicolor) # return the list Versicolor


    def splitVirginica(x): # Does the exact same as splitSetosa formula except does it for the Virginica Iris class
        """Splits the original iris dataset into a list containing only Iris Virginica class with all the attributes i.e. Virginica = [[5.1,3.5,1.4,0.2,Iris-Virginica]...[5.0,3.3,1.4,0.2,Iris-Virginica]]"""
        Dataset=[] # list created for "Dataset"
        Virginica=[] # list created for "Virginica"
        with open("iris.csv") as f: # opens the data file "iris.csv" and names the file "f"
            for line in f:  # for all lines in "f" do the following...
                Dataset.append(line.split(",")) # split up the values in each line for the data set by recognising the comma (,) as the delimiter and add the value to the list named "Dataset"
            for x in range(len(Dataset)): # finds the number of values in the list "Dataset", uses the number of values as the range and iterates through the range by 1 every time. Acts as a counter. For each iteration do...
                for i in Dataset[x]: # for i in the Dataset list indexed x do the following...
                    if i =="Iris-virginica\n": # if i is equal to the string then do the following...
                        Virginica.append(Dataset[x]) # append the setosa array with the list indexed x in "Dataset"
                    else: # otherwise...
                        continue # keep going with the code
            return(Virginica) # return the list Virginica

    #IMPORTANT NOTE: The below definitions are reliant on the above definitions.
    def maxSetosavalue(x):
        """Returns the maximum value for an attribute that belongs to the Setosa class i.e. Max sepal length for the setosa class is 5.8cm"""
        # Change the value of x to change the attribute the user wishes to find the maximum of i.e. 0 is for sepal length, 1 is for sepal width
        Mickey = [] # list named "Mickey" created
        maximumvalue = 0 # creates a variable named maximum value and sets its value at 0
        if x > 3 or x < 0: # if statement - do the following if x is greater than 3
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width") # tell the user that the only options are 0 to 3 if a number greater than 3 is selected
            return(text) # return the text
        elif x>=0 or x<=3: # if the user selection is within the range 0 to 3 do the following...
            for m in range(len(splitSetosa(0))): # for the length of the Setosa list do the following...
                    Mickey.append(splitSetosa(0)[m][x]) # append the list Mickey with the values in the user specified column
            maximumvalue = float(max(Mickey)) # get the maximum value of the list Mickey
            return(maximumvalue) # return the maximum value


    def maxVersicolorvalue(x):
        """Returns the maximum value for an attribute that belongs to the Versicolor class"""
        # Change the value of x to change the attribute the user wishes to find the maximum of i.e. 0 is for sepal length, 1 is for sepal width
        Minnie = [] # list named "Minnie" created
        maximumvalue = 0 # creates a variable named maximum value and sets its value at 0
        if x > 3: # if statement - do the following if x is greater than 3
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Versicolor sepal length\n 1 = Versicolor sepal width\n 2 = Versicolor petal length\n 3 = Versicolor petal width") # tell the user that the only options are 0 to 3 if a number greater than 3 is selected
            return(text) # return the text
        elif x>=0 or x<=3: # if the user selection is within the range 0 to 3 do the following...
            for m in range(len(splitVersicolor(0))):  # for the length of the Setosa list do the following...
                Minnie.append(splitVersicolor(0)[m][x]) # append the list Minnie with the values in the user specified column
            maximumvalue = float(max(Minnie)) # get the maximum value of the list Minnie
            return(maximumvalue)  # return the maximum value


    def maxVirginicavalue(x):
        """Returns the maximum value for an attribute that belongs to the Virginica class"""
        # Change the value of x to change the attribute the user wishes to find the maximum of i.e. 0 is for sepal length, 1 is for sepal width
        Pluto = [] # list named "Pluto" created
        maximumvalue = 0 # creates a variable named maximum value and sets its value at 0
        if x > 3: # if statement - do the following if x is greater than 3
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Virginica sepal length\n 1 = Virginica sepal width\n 2 = Virginica petal length\n 3 = Virginica petal width") # tell the user that the only options are 0 to 3 if a number greater than 3 is selected
            return(text)  # return the text
        elif x>=0 or x<=3: # if the user selection is within the range 0 to 3 do the following...
            for m in range(len(splitVirginica(0))): # for the length of the Setosa list do the following...
                Pluto.append(splitVirginica(0)[m][x]) # append the list Pluto with the values in the user specified column
            maximumvalue = float(max(Pluto)) # get the maximum value of the list Pluto
            return(maximumvalue) # return the maximum value



    x1 = (maxSetosavalue(x)) # give x1 the value of the result of the maxSetosavalue formula
    x2 = (maxVersicolorvalue(x)) # give x2 the value of the result of the maxVersicolorvalue formula
    x3 = (maxVirginicavalue(x)) # give x3 the value of the result of the maxVirginicavalue formula

    import matplotlib.pyplot as plt # import the library for plotting graphs etc. as "plt"
    
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
        plt.title('Max Sepal Length bar chart')
    elif x == 1:
         #title is Sepal Width if x = 1
        plt.title('Max Sepal Width bar chart')
    elif x == 2:
         #title is Petal Length if x = 2
        plt.title('Max Petal Length bar chart')
    elif x == 3:
         #title is Petal Width if x = 3
        plt.title('Max Petal Width bar chart')    
    # function to show the plot
    plt.show()

plotHisto(x = int(input("0 = Sepal Length,\n1 = Sepal Width,\n2 = Petal Length,\n3 = Petal Width,\nEnter the number you wish to plot:"))) # initialise the code with user input for the "x" value which is integral to all formulas within the code, then plot the result