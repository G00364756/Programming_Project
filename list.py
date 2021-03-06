# Aidan O'Connor - G00364756 - 22/03/2018 
# Programming_Project - Investigate the iris data set and 
# create analysis based on research previously conducted
# References:
# Link to csv file = https://archive.ics.uci.edu/ml/datasets/iris
# Adapted from code learned from lectures by Dr. Ian McGlouglin.
# Learned how to append to a list from python tutorial = https://docs.python.org/3/library/array.html?highlight=append#array.array.append
# "try" and "except" = https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python 
# "rstrip" to get rid of "\n" appearing in string = https://stackoverflow.com/questions/38855670/how-to-append-a-string-into-a-list-without-its-new-line-n-in-python-3?rq=1
# Ran into an issue with the input from the user becoming a string rather than an integer so I used "int" to convert the input from user to an integer so the split function could execute.

def split(x):
    """Takes the dataset and splits the specified column into a list"""
    with open("iris.csv") as f:#Open the csv file which will now be called "f"
            attribute=[] # list with name "attribute"
            feature=[] # list with name feature
            for line in f: # for loop - iterates through all the values in f
                jay = line.split(",") #for each line in the dataset split the lines into new individual lists e.g. [3.5,1.4,0.2,Iris-setosa][4.9,3.0,1.4,0.2,Iris-setosa]
                feature.append(jay[x])    #Append the list "s_l" with the 1st value in each of the newly created lists
            for i in feature: # for loop - iterates through all the values in the list "feature"
                try: # try will try the following condition for all the values of i in feature
                    attribute.append(float(i)) # Convert all the values in "s_l" into float and append them to a new list called "sepal_length"
                except: # if try does not work the loop will move to "except" and will attempt the contained code
                    attribute.append(i.rstrip()) # strips the "\n" from the string values for iris class in column 5
            if x == 0: # if statement - condition of x equal to 0 has to be met for the contained code to be executed
                sepal_length = [] # list for sepal length created
                sepal_length = attribute # makes the list "sepal_length" have all the same values as "attribute"
                return(sepal_length) # return the list "sepal_length"
            elif x == 1: # elif statement which does the same as the above if statement but only if the condition x equal to 1 is met. All other elif statements below are similar.
                sepal_width = []
                sepal_width = attribute
                return(sepal_width)
            elif x == 2:
                petal_length = []
                petal_length = attribute
                return(petal_length)
            elif x == 3:
                petal_width = []
                petal_width = attribute
                return(petal_width)
            elif x == 4:
                iris_class = []
                iris_class = attribute
                return(iris_class)
            else: # if none of the conditions above are met the else condition is met and will execute the below code
                return("No dice! This data set contains coulmn 0 to 4, try a number between 0 and 4") # Returns string telling user to try again
print(split(int(input("0 = Sepal Length,\n1 = Sepal Width,\n2 = Petal Length,\n3 = Petal Width,\n4 = Iris Class,\nEnter the number for the column you wish to split into a list:")))) # on execution of list.py this code initiates the whole file. The user is asked to input a number and the code converts it to an integer so that it can be used to initiate the split formula as defined previously and prints the result to the terminal.