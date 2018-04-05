# Programming_Project
Project work for the Programming Module (Data Analytics)
Name:                Aidan O'Connor
GMIT student number: G00364756
Created:             22/03/2018

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
[1]: https://en.wikipedia.org/wiki/Iris_flower_data_set  
[2]: http://www.ias.ac.in/article/fulltext/reso/002/09/0032-0037  
[3]: https://pdfs.semanticscholar.org/1ab8/ea71fbef3b55b69e142897fadf43b3269463.pdf  
[4]: https://www.youtube.com/watch?v=azXCzI57Yfc  
  
Sir Ronald Aylmer Fisher (17 February 1890 – 29 July 1962),  was a British statistician and geneticist. Over the course of his career he made substantial contributions to genetics and statistical science. Many consider Fisher as the man who laid the foundations of statistics as a science.[1],[2]
Fisher developed a linear discriminant model to distinguish between three species of Iris using a data set collected by Edgar Anderson.[1]

The Iris data set is aphiliated with both Anderson and Fisher. The reason Edgar Anderson collected the data was to quantify the morphologic variation of Iris flowers of three related species.[1]

Fifty samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor) were collected. Four attributes were measured from each sample: sepal length, sepal width, petal length and petal width, all in centimetres. [2]

Fisher's Linear Discriminant Analysis (LDA) is used to find a linear combination of features which characterizes or separates two or more classes of objects or events. This can be extremely useful in everyday life. For instance if the pharamceutical company are trialling a new type of drug to fight a certain disease, and they wish to know what type of people the drug helps cure and what type of people the drug does not help cure, then the use of LDA can aid the pharaceutical company in discriminating between these two classes of people (i.e. class1 = drug helps cure, class2 = drug does not help cure). In doing so they can better determine what types of people should take the drug and what type of people shouldn't. LDA becomes more valuable in separating classes as more attributes are necessary to be used in a dataset (e.g. can't clearly discriminate between cured people and not cured people in analysing gene X and gene Y, need to analyse more genes, new anlysis contains 20 genes, the use of more genes and LDA makes the discrimnation more clear). [3],[4]

## Identification of analysis that can be done to the data set
[5]: https://www.mathsisfun.com/data/standard-deviation.html
[6]: http://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html#sphx-glr-auto-examples-decomposition-plot-pca-vs-lda-py
[7]: https://en.wikipedia.org/wiki/Standard_deviation
[8]: https://betterexplained.com/articles/how-to-analyze-data-using-the-average/
[9] https://www.mathsisfun.com/data/frequency-grouped-mean-median-mode.html

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

In statistics, the standard deviation is a measure that is used to quantify the amount of variation or dispersion of a set of data values. A low standard deviation indicates that the data points tend to be close to the mean of the set, while a high standard deviation indicates that the data points are spread out over a wider range of values. The standard deviation of a random variable, statistical population, data set, or probability distribution is the square root of its variance.[7]

7. Principal Component Analysis (PCA)

Principal Component Analysis (PCA) applied to this data identifies the combination of attributes (principal components, or directions in the feature space) that account for the most variance in the data. Here we plot the different samples on the 2 first principal components.

8. Linear Discriminant Analysis (LDA)
Linear Discriminant Analysis (LDA) tries to identify attributes that account for the most variance between classes. In particular, LDA, in contrast to PCA, is a supervised method, using known class labels.

9. Compare attributes for each class with a graph plotted through python.

## 





