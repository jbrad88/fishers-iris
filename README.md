# fishers-iris
# Programming and Scripting Project 2020

# Iris flower data set

## Table of contents
* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Technologies](#technologies)
* [General Usage Information](#general_usage_information)
* [Findings](#findings)
* [References](#references)

## Introduction

The Iris flower data set (also known as Fisher's Iris data set) is a well known multivariate data set. It was introduced by Ronald Fisher (a British statistician and geneticist)in 1936, in his paper titled "The use of multiple measurements in taxonomic problems". This dataset can be accessed on the UCI Machhine Learning Repository [1].

The data set consists of 3 classes of 50 samples each (i.e. 150 samples in total), where each class refers to each of the three species of Irish (Iris setosa, Iris virginica and Iris versicolor). Four attributes were measured from each of the 150 samples: (i) the sepal length in cm; (ii) the sepal width in cm; (iii) the petal length in cm; and (iv) the petal width in cm.

<<<<<<< HEAD
The Iris Flower Data Set is widely used as a test case for machine learning. New types of sorting models and taxonomy algorithms often use the Iris flower data set as an input, to examine how various technologies sort and handle data sets [2].
=======
![fig1](https://miro.medium.com/max/362/1*XN85Vu-SmkJc3TkwgTx5Kw.jpeg)

The Iris Flower Data Set is widely used as a test case for machine learning. 
>>>>>>> 956632d2a09b5033333c4f19efc4e6bab51ef1f5

This program inputs the Iris flower data set and outputs a histrogram for each of the four variables (saved as png files) and a scatter plots of each pair of variables (i.e. sepal width v sepal length, and petal width v petal length).

## Prerequisites

Before you continue, make sure that you have met the following requirements:
* You have installed Python 3.7.4
* You have a basic understanding of graph theory.

## Technologies

- Python 3.7.4
- pandas - Python Data Analysis Library
- NumPy
- Matplotlib: Python plotting 

## General Usage Information
1. Download ZIP package and unzip it.
2. On a new command line, navigate to the directory containing the (now unzipped) downloaded folder.
3. Run the "analysis program" by simply typing "python" followed by the file name, i.e. python analysis.py
4. When the program has run you will see an overview of the data set, showing the three species of Iris included in the data set, the first ten rows of the sample, giving the user a taste of the data which we will be looking at, and a summery of each variable.
5. Running the program will also create the following files:

-> Summary of the data set saved as "Iris-data.csv"

-> Four histograms saved as: "petal_length.png", "petal_width.png", "sepal_length.png" and "sepal_width.png"

and

-> "Pairplot.png" showing a matrix of the relationships between each variable. 


## Findings 

### Summary
*This file provides a summary of the data set using the "describe()" function, giving the user the "count" (the number of samles), the "mean" (average value), the "std" (standard deviation), the "min" (minimum value), the "max" (maximum value), and the lower (25%), upper (75%) and the middle (50%) percentile. Using this table for example, we can see that the maximum sepal length is 7.9cm, while the minimum sepal length is 4.3cm. The average (mean) sepal width is 5.843cm. 

### Histograms
* A histrogram is a graphical display of data using bars of different heights, representing the number of samples in a given range.
* Running the analysis.py program creates 4 histograms, showing the distribution of the variables of the data set.
* The Iris Setosa species is easily identified from the other two species by its petal length.
* All three species overlap in their sepal length and sepal width attributes.

## Scatter Plots
* Scatter plots show the relationship between two data sets, i.e. their correlation.
* Running the analysis.py program creates a file "pairplot.png" which shows a matrix of the relationships between each variable.
* There is a strong correlation between petal length and petal width.



# REFERENCES
1. http://archive.ics.uci.edu/ml/datasets/iris
2. https://www.techopedia.com/definition/32880/iris-flower-data-set
3. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
4. https://www.datacamp.com/community/tutorials/pandas-read-csv
5. https://www.geeksforgeeks.org/reading-writing-text-files-python/
6. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
7. https://datatofish.com/export-dataframe-to-csv/
8. https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
9. https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
10. https://github.com/adobe-type-tools/python-scripts/blob/master/README.md
