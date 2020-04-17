# fishers-iris
# Programming and Scripting Project 2020

# Iris flower data set

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)


## Introduction

The Iris flower data set (also known as Fisher's Iris data set) is a well known multivariate data set. It was introduced by Ronald Fisher (a British statistician and geneticist)in 1936, in his paper titled "The use of multiple measurements in taxonomic problems". 

The data set consists of 3 classes of 50 samples each (i.e. 150 samples in total), where each class refers to each of the three species of Irish (Iris setosa, Iris virginica and Iris versicolor). Four attributes were measured from each of the 150 samples: (i) the sepal length in cm; (ii) the sepal width in cm; (iii) the petal length in cm; and (iv) the petal width in cm [1].

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









#References
[1] UC Irvine Machine Learning Repository. Iris data set.
https://archive.ics.uci.edu/ml/datasets/Iris
[2] https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d


