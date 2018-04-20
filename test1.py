    
def splitSetosa(x):
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


def modeSetosavalue(x):
    """return the estimated mode of the data for a particular attribute"""
    Mickey = []
    if x > 3: 
        text =("No dice! Last column in this dataset is a string! Please run the file again and pick a number between 0 and 3.")
        return(text)
    elif x>=0 or x<=3:
        for m in range(len(splitSetosa(0))):
            Mickey.append(float(splitSetosa(0)[m][x]))
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
    if mode == TupleG1:
        return (print("Group 1:- 0.0 - 0.9,\nFrequency of group:-", mode ))
    elif mode == TupleG2:
        return (print("Group 2:- 1.0 - 1.9,\nFrequency of group:-", mode ))
    elif mode == TupleG3:
        return (print("Group 3:- 2.0 - 2.9,\nFrequency of group:-", mode ))
    elif mode == TupleG4:
        return (print("Group 4:- 3.0 - 3.9,\nFrequency of group:-", mode ))
    elif mode == TupleG5:
        return (print("Group 5:- 4.0 - 4.9,\nFrequency of group:-", mode ))
    elif mode == TupleG6:
        return (print("Group 6:- 5.0 - 5.9,\nFrequency of group:-", mode ))
    elif mode == TupleG7:
        return (print("Group 7:- 6.0 - 6.9,\nFrequency of group:-", mode ))
    elif mode == TupleG8:
        return (print("Group 8:- 7.0 - 7.9,\nFrequency of group:-", mode ))
    else:
        return (print("Mode outside the defined groupings!"))

print(modeSetosavalue(x = int(input("0 = Sepal Length,\n1 = Sepal Width,\n2 = Petal Length,\n3 = Petal Width,\nEnter the number you wish to plot:"))))
