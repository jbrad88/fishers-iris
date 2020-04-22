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

![fig1](https://miro.medium.com/max/362/1*XN85Vu-SmkJc3TkwgTx5Kw.jpeg)

The Iris Flower Data Set is widely used as a test case for machine learning. 

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
4. When the program has been succesfully run, it will create the following files:

### Summary of the data set saved as "Iris-data.csv"

This file provides a summary of the data set using the "describe()" function, giving the user the "count" (the number of samles), the "mean" (average value), the "std" (standard deviation), the "min" (minimum value), the "max" (maximum value), and the lower (25%), upper (75%) and the middle (50%) percentile.

-> Four histograms saved as: "petal_length.png", "petal_width.png", "sepal_length.png" and "sepal_width.png"

and

-> "Pairplot.png" showing a matrix of the relationships between each variable. 


## Findings 

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
2. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
3. https://www.datacamp.com/community/tutorials/pandas-read-csv
4. https://www.geeksforgeeks.org/reading-writing-text-files-python/
5. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
6. https://datatofish.com/export-dataframe-to-csv/
7. https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
8. https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib
9. https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
10. https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
11. https://github.com/adobe-type-tools/python-scripts/blob/master/README.md
