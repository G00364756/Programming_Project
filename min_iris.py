# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted

# 3. Minimum Value Comparison:-
# Identify the minimum value of each of the attributes for 
# each class and compare the results.

# Results in a bar chart of the minimum value of a user selected attribute for each Iris Class.

def plotHisto(x):

    def splitSetosa(x): # Same code as in max_iris.py
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


    def splitVersicolor(x): # Same code as in max_iris.py
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


    def splitVirginica(x): # Same code as in max_iris.py
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
    def minSetosavalue(x):
        """Returns the minimum value for an attribute that belongs to the Setosa class e.g. Min sepal length for the setosa class is 3.1cm (Example not real value)"""
        #Change the value of x to change the attribute you want to find the max of
        Mickey = []
        minimumvalue = 0
        if x > 3: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Setosa sepal length\n 1 = Setosa sepal width\n 2 = Setosa petal length\n 3 = Setosa petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitSetosa(0))): # for the length of the 1st column of the list "splitSetosa" do the following...
                    Mickey.append(splitSetosa(0)[m][x]) # append Mickey with the values in splitSetosa specified by the user
            minimumvalue = float(min(Mickey))   # get the minimum value for the list Pluto and set the value to a float type value
            return(minimumvalue) # return the value for minimumvalue


    def minVersicolorvalue(x):
        """Returns the minimum value for an attribute that belongs to the Versicolor class e.g. Min sepal length for the versicolor class is 3.1cm (Example not real value)"""
        Minnie = []
        minimumvalue = 0
        if x > 3: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Versicolor sepal length\n 1 = Versicolor sepal width\n 2 = Versicolor petal length\n 3 = Versicolor petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitVersicolor(0))): # for the length of the 1st column of the list "splitVersicolor" do the following...
                Minnie.append(splitVersicolor(0)[m][x]) # append the list Pluto with the values specified by the user
            minimumvalue = float(min(Minnie))  # get the minimum value for the list Pluto and set the value to a float type value
            return(minimumvalue) # return the value for minimumvalue


    def minVirginicavalue(x):
        """Returns the minimum value for an attribute that belongs to the Virinica class e.g. Min sepal length for the virginica class is 3.1cm (Example not real value)"""
        Pluto = []
        minimumvalue = 0
        if x > 3: 
            text =("No dice! Last column in this dataset is a string!\n Please pick a value for x between 0 and 3.\n 0 = Virginica sepal length\n 1 = Virginica sepal width\n 2 = Virginica petal length\n 3 = Virginica petal width")
            return(text)
        elif x>=0 or x<=3:
            for m in range(len(splitVirginica(0))): # # for the length of the 1st column of the list "splitVirginica" do the following...
                    Pluto.append(splitVirginica(0)[m][x]) # append the list Pluto with the values specified by the user
            minimumvalue = float(min(Pluto)) # get the minimum value for the list Pluto and set the value to a float type value
            return(minimumvalue) # return the value for minimumvalue



    x1 = (minSetosavalue(x)) # set x1 to the value for minSetosavalue(x)
    x2 = (minVersicolorvalue(x)) # set x2 to the value for minVersicolorvalue(x)
    x3 = (minVirginicavalue(x)) # set x3 to the value for minVirginicavalue(x)

    import matplotlib.pyplot as plt # import the library for graphs
    
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
        plt.title('Min Sepal Length bar chart')
    elif x == 1:
         #title is Sepal Width if x = 1
        plt.title('Min Sepal Width bar chart')
    elif x == 2:
         #title is Petal Length if x = 2
        plt.title('Min Petal Length bar chart')
    elif x == 3:
         #title is Petal Width if x = 3
        plt.title('Min Petal Width bar chart')    
    # function to show the plot
    plt.show()

plotHisto(x = int(input("0 = Sepal Length,\n1 = Sepal Width,\n2 = Petal Length,\n3 = Petal Width,\nEnter the number you wish to plot:"))) # initialise the code with user input, when user has specified the value of x run the code in it's entirety to return a bar chart of the attribute for each iris class