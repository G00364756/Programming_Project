# Programming_Project
Project work for the Programming Module (Data Analytics)
Name:                Aidan O'Connor
GMIT student number: G00364756
Created:             22/03/2018
Due date:            29/04/2018

## Background of Project:  
This project is part of the Programming Module for the Data Analytics course offered by the Galway-Mayo Institute of Technology, taught by Dr. Ian McGloughlin. The aim of this project is to investigate the data set known as the "iris data set", created by Sir Ronald Aylmer Fisher, with the Python programming language, based on research conducted into the value that can be gained from the data set with respect to data analytics. In doing so, I hope to demonstrate my proficiency in project management, programming, research and demonstrating work to others who may be unfamiliar with the material.

## Project Plan:

1. Research  
Goals include -  
* Investigating what the data set contains  
* The background behind the creation of the data set  
* The relevance and importance of the data set to data analytics  
* Possible analysis that can be done to the data set  

2. Creating code to analyse the data set  
Goals include -  
* (Feeds on from research) Identify what type of analysis would be appropriate to use on the data set  
* Code the analysis using the python programming language  
* Regularly comment on code to help a third party understand the functionality  
* Reference code that has been adapted or copied from other sources  
* Commit code work to github regularly to demonstrate the time given to the project and the many different stages of change  
* Attach relevant graphs, photos and other files to github repository to form part of the project  

## Introduction to the Iris Data Set and Linear Data Analysis
#### Refernces 
[1]: https://en.wikipedia.org/wiki/Iris_flower_data_set  
[2]: http://www.ias.ac.in/article/fulltext/reso/002/09/0032-0037  
[3]: https://pdfs.semanticscholar.org/1ab8/ea71fbef3b55b69e142897fadf43b3269463.pdf  
[4]: https://www.youtube.com/watch?v=azXCzI57Yfc  
  
Sir Ronald Aylmer Fisher (17 February 1890 – 29 July 1962),  was a British statistician and geneticist. Over the course of his career he made substantial contributions to genetics and statistical science. Many consider Fisher as the man who laid the foundations of statistics as a science.[1],[2]
Fisher developed a linear discriminant model to distinguish between three species of Iris using a data set collected by Edgar Anderson.[1]

The Iris data set is aphiliated with both Anderson and Fisher. The reason Edgar Anderson collected the data was to quantify the morphologic variation of Iris flowers of three related species.[1]

Fifty samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor) were collected. Four attributes were measured from each sample: sepal length, sepal width, petal length and petal width, all in centimetres. [2]

Fisher's Linear Discriminant Analysis (LDA) is used to find a linear combination of features which characterizes or separates two or more classes of objects or events. This can be extremely useful in everyday life. For instance if the pharamceutical company are trialling a new type of drug to fight a certain disease, and they wish to know what type of people the drug helps cure and what type of people the drug does not help cure, then the use of LDA can aid the pharaceutical company in discriminating between these two classes of people (i.e. class1 = drug helps cure, class2 = drug does not help cure). In doing so they can better determine what types of people should take the drug and what type of people shouldn't. 
LDA becomes more valuable in separating classes as more attributes are necessary to be used in a dataset (e.g. can't clearly discriminate between cured people and not cured people in analysing gene X and gene Y, need to analyse more genes, new anlysis contains 20 genes, the use of more genes and LDA makes the discrimination more clear). [3],[4]

## Identification of analysis that can be done to the data set
#### References:
[5]: https://www.mathsisfun.com/data/standard-deviation.html
[6]: http://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html#sphx-glr-auto-examples-decomposition-plot-pca-vs-lda-py
[7]: https://en.wikipedia.org/wiki/Standard_deviation
[8]: https://betterexplained.com/articles/how-to-analyze-data-using-the-average/
[9]: https://www.mathsisfun.com/data/frequency-grouped-mean-median-mode.html

1. Split data by class

Split up the data set into classes (i.e. Setosa Versicolor and Verginica).

This 1st step in the analysis of the data is very important. It allows the data to be split separately into classes, allowing analysis of the class itself without being comprimised by data from another class. Later a comparison of the analysis of the classes can give valuable information.

2. Maximum value comparison

Identify the maximum value of each of the attributes for each class and compare the results.

This is a simple concept in which the maximum value of each attribute is identified for each class. By obtaining the single largest values for an attribute (i.e. sepal length, sepal width... etc.) within each class, the classes can then be compared to identify which class gives the largest value for each attribute (i.e. Iris Setosa class has a max value of 7.2cm whereas Iris Versicolor class has a max value of 6.3cm [NB - not actual values just an example]). This is a very simplistic analysis and does not always suggest that Iris Setosas have a longer sepal length than Iris Versicolors. The sample that lead to the data that gave the maximum value may have been an extrememly unusual case for the iris class and could completely misrepresent the iris class. A more comprehensive analysis is needed to come to solid conclusions.

3. Minimum value comparison

Identify the minimum value of each of the attributes for each class and compare the results.

This is similar to the maximum value concept. However this time the minimum value of each attribute is identified for each class. Again this is a very simplistic analysis and does not always suggest that Iris Versicolors have a shorter sepal length than Iris Setosas. The sample that lead to the data that gave the minimum value may have been an extrememly unusual case for the iris class and could completely misrepresent the iris class. A more comprehensive analysis is needed to come to conclusions.

4. Mean value comparison

Identify the mean value of each of the attributes for each class and compare the results.

The mean is often described as the average value of a set of numbers. By identifiying the mean of each of the attributes for each of the classes, a more reliable estimate can be established:- of which class, on average, would have the largest or the smallest attributes (i.e. sepal length, sepal width, etc.). This is a more comprehensive way of analysing data. In getting the mean value for the iris data set we can get results such as:- Iris Setosa class has an average sepal length of 4.5cm, Iris Versicolor has an average sepal length of 4.7cm (NB - This is only an example of a possible result and does not reflect the results of the data set). From results such as this conclusions can be drawn that on average Iris Versicolor will, on average, have longer sepal lengths than Iris Setosas (NB - Again this is just an example of a conclusion that could be drawn and do not reflect any conclusions drawn from analysis of the data set). Getting the mean value of the attributes and comparing the mean values, is a better analysis technique than just getting the maximum and minimum values of each attribute and comparing the maximum and minimum values. More accurate representation of data class can be given by using a comparison of the mean vs the aforementioned technique. However there are cons to using the mean value comparison as an analysis technique. The mean value can be skewwed by a value/s which lie vastly outside the normal range of values.[8]

5. Mode value comparison

Identify the mode of each of the attributes for each class and compare the results.

The mode is another very effective analysis tool. The mode is the most common number in a range of numbers (i.e. [1,1,2,4,8,9,9,9,11,12,12,13] in this range the mode is 9 as it occured 3 times which is more than any other number in the range). Using the mode may be difficult in the context of iris data set as the values seem to be extremely varied, however an estimated mode method can be used where the range of values in the data are grouped together(i.e. first group [0.0-1.9], second group [1.0-2.9]...etc.). Grouping the data and obtaining the frequency of the occurence of values within that grouping gives a more accurate reflection of the most common value for a class, which will be the mode. This type of analysis may be more accurate than the use of the mean method, it negates the issue of skew as values that are not of the norm will be dismissed in a scientific manner. [9]

6. Identify the standard deviation of the attributes for each class.

The standard deviation is a measure of the amount of variation or dispersion of a set of data values. A low standard deviation indicates that the data points tend to be close to the mean of the set, while a high standard deviation indicates that the data points are spread out over a wider range of values. The standard deviation of a random variable, statistical population, data set, or probability distribution is the square root of its variance.[7]

7. Principal Component Analysis (PCA)

Principal Component Analysis (PCA) applied to this data identifies the combination of attributes (principal components, or directions in the feature space) that account for the most variance in the data. Here we plot the different samples on the 2 first principal components.

8. Linear Discriminant Analysis (LDA)
Linear Discriminant Analysis (LDA) tries to identify attributes that account for the most variance between classes. In particular, LDA, in contrast to PCA, is a supervised method, using known class labels.

9. Plot graphs

Compare attributes for each class with a graph plotted for each of the analysis methods described.

## Decision of the analysis that will be conducted on this data set
The analysis methods that will be conducted as part of this project will be the following:

#### Deliverables
1. Split data by class
2. Maximum value comparison
3. Minimum value comparison
4. Mean value comparison
5. Mode value comparison
6. Identification of the standard deviation of an attribute for each class
7. Plot graphs

All the analysis methods will be built from the ground up from knowledge gained through studying course notes from the Data Analytics Programming module and learnings from external sources on the world wide web.

Based on conducted research the decision was made to exclude no. 7 Principle Component Analysis and no. 8 Linear Discriminant Analysis methods from the project. From research it would appear that building code for both methods from the ground up would be extremely time consuming unless using powerful tools like "numpy" or "pandas". Pre-built code has been identified from sources on the Github application, which could be implimented to conduct the PCA and LDA analysis methods however there is no benefit in using this pre-built code. The aim of this project is to demonstrate the student's proficiency with python from what has been learned so fat, and also to demonstrate project management skills. Excluding the PCA and LDA methods means that the deliverables numbered 1-7 above will be met within the timeframe of the project and will be done with the project aims in mind (i.e. demonstration of learnings).

## Python code files
Below is a list of the python files, within the project repository on Github, developed to output the deliverables already identified in the decision making stage of this document.

### list.py
1st attempt at deliverable 1

This code asks the user which column of data they wish to split into a separate list, once the user enters their selection the code executes and outputs the resulting list to the terminal. This is code that was developed initially while experimenting on how to get the deliverable "Split data into class".

### type.py
2nd attempt at deliverable 1 and 2 combined

This code splits the the data up into Iris class then it find the maximum value of a predetermined attribute. No user input in this code. Changes made subsequently to make code more user interactive as can be seen in max_iris.py

### test1.py
1st attempt at deliverable 6

This code was developed to test code that was to be inserted into mode.py pending satisfactory performance in tests.

### tryit.py
1st attempt at deliverable 2

This code was developed to give the maximum value for an attribute for each class of Iris. This code was subsequently built on to plot a graph which can be observed in max_iris.py

### max_iris.py
Deliverable 1,2 and 7 addressed with this code

This code uses a number of defined functions to produce its output.  The code asks the user for an input initially. This input corresponds to an attribute for each Iris class. The user inserts their preference and the code executes fully. The code will plot a graph of the maximum value, for the user specified attribute, for each Iris class, as a bar chart.

### min_iris.py
Deliverable 1,3 and 7 addressed with this code

Adapted from max_iris.py, this code uses a number of defined functions to produce its output.  The code asks the user for an input initially. This input corresponds to an attribute for each Iris class. The user inserts their preference and the code executes fully. The code will plot a graph of the minimum value, for the user specified attribute, for each Iris class, as a bar chart.

### mean.py
Deliverable 1,4 and 7 addressed with this code

Adapted from max_iris.py, this code uses a number of defined functions to produce its output.  The code asks the user for an input initially. This input corresponds to an attribute for each Iris class. The user inserts their preference and the code executes fully. The code will plot a graph of the mean, for the user specified attribute, for each Iris class, as a bar chart.

### mode.py
Deliverable 1,5 and 7 addressed with this code

Adapted from mean.py, this code uses a number of defined functions to produce its output.  The code asks the user for an input initially. This input corresponds to an attribute for each Iris class. The user inserts their preference and the code executes fully. The code will plot a graph of the mode, for the user specified attribute, for each Iris class, as a bar chart.

### stnddev.py
Deliverable 1,6 and 7 addressed with this code

Adapted from mean.py, this code uses a number of defined functions to produce its output.  The code asks the user for an input initially. This input corresponds to an attribute for each Iris class. The user inserts their preference and the code executes fully. The code will plot a graph of the standard deviation, for the user specified attribute, for each Iris class, as a bar chart.

### Note: All deliverables are met with the above python files

## Investigative Analysis Results

Please find screen captures of the outputs of all executed python code as described in the previous section of this READme file.

### list.py 

Please see the following screencaptures for demonstration of the result:-

### test1.py 

Please see the following screencaptures for demonstration of the result:-

### tryit.py 

Please see the following screencaptures for demonstration of the result:- 

### max_iris.py results:

Attribute     | Setosa        | Versicolor    | Verginica     |
------------- | ------------- |-------------- | ------------- |
Sepal_length  | 5.8cm         | 7.0cm         | 7.9cm         |
Sepal_width   | 4.4cm         | 3.4cm         | 3.8cm         |
Petal_length  | 1.9cm         | 5.1cm         | 6.9cm         |
Petal_width   | 0.6cm         | 1.8cm         | 2.5cm         |

### min_iris.py results:

Attribute     | Setosa        | Versicolor    | Verginica     |
------------- | ------------- |-------------- | ------------- |
Sepal_length  | 4.3cm         | 4.9cm         | 4.9cm         |
Sepal_width   | 2.3cm         | 2.0cm         | 2.2cm         |
Petal_length  | 1.0cm         | 3.0cm         | 4.5cm         |
Petal_width   | 0.1cm         | 1.0cm         | 1.4cm         |

### mean.py results:

Attribute     | Setosa        | Versicolor    | Verginica     |
------------- | ------------- |-------------- | ------------- |
Sepal_length  | 5.0cm         | 6.0cm         | 6.6cm         |
Sepal_width   | 3.4cm         | 2.8cm         | 3.0cm         |
Petal_length  | 1.5cm         | 4.3cm         | 5.6cm         |
Petal_width   | 0.3cm         | 1.3cm         | 2.0cm         |

### mode.py results:

Attribute     | Setosa        | Versicolor    | Verginica     |
------------- | ------------- |-------------- | ------------- |
Sepal_length  | 5.1cm         | 5.8cm         | 6.5cm         |
Sepal_width   | 3.4cm         | 2.6cm         | 3.1cm         |
Petal_length  | 1.4cm         | 4.3cm         | 5.5cm         |
Petal_width   | 0.5cm         | 1.4cm         | 2.1cm         |

### stddev.py results:

Attribute     | Setosa        | Versicolor    | Verginica     |
------------- | ------------- |-------------- | ------------- |
Sepal_length  | 0.4cm         | 0.5cm         | 0.6cm         |
Sepal_width   | 0.4cm         | 0.3cm         | 0.3cm         |
Petal_length  | 0.2cm         | 0.5cm         | 0.5cm         |
Petal_width   | 0.1cm         | 0.2cm         | 0.3cm         |

## Summary of investigations


## End