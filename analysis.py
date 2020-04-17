# Jody Bradley
# This program....

# Import the libraries which we will be using [1]:
import csv
import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The first part of this program will output a summary of each variable to a single text file (in CSV format).
# This will give the user the mean, the standard variation, the minimum, the maximum of each of the four attributes
# (sepal length, sepal width, petal length and petal width).

df = pd.read_csv('iris.csv')
# Loads data from the CSV file 'iris.csv' into pandas dataframe.
col=['sepal_length','sepal_width','petal_length','petal_width','species']

x = 2
if x == 2: 
    print(" ")
    print("This program provides an analysis of the well-known Fisher's Iris data set.")
    print(" ")
    print("The first five rows of the sample gives an overview of the variables:")
    print(df.head())
    print(" ")
    print("Below is a summary of each variable:") 
    print(" ")
    print(df.describe())
    print(" ")

summary = df.describe()

file1 = open(r"Iris-data.csv", 'a')
# Creates and opens a CSV file titled Iris-data [3]

summary.to_csv(r'Iris-data.csv')
# Saves summary to a CSV file[5]

print("A text file of this data has now been saved in the program folder as a CSV file titled iris.csv.")
print(" ")

# Divide the data set into the three species:
iris_setosa=df.loc[df["species"]=="Iris-setosa"]
iris_virginica=df.loc[df["species"]=="Iris-virginica"]
iris_versicolor=df.loc[df["species"]=="Iris-versicolor"]

# This next part of the program will save a histrogram as a PNG for each of the four variables [8].
sns.FacetGrid(df,hue="species",height=3).map(sns.distplot,"petal_length").add_legend()
plt.savefig("petal_length.png")
plt.clf()

sns.FacetGrid(df,hue="species",height=3).map(sns.distplot,"petal_width").add_legend()
plt.savefig("petal_width.png")
plt.clf()

sns.FacetGrid(df,hue="species",height=3).map(sns.distplot,"sepal_length").add_legend()
plt.savefig("sepal_length.png")
plt.clf()

sns.FacetGrid(df,hue="species",height=3).map(sns.distplot,"sepal_width").add_legend()
plt.savefig("sepal_width.png")
plt.clf()

# This final part of the program produces a matrix of relationships between each pair of variables.
sns.set_style("whitegrid")
sns.pairplot(df,hue="species",height=3)
plt.savefig("pairplot.png")
plt.clf()

print("Please refer to the program folder for the following files which have now been created:")
print("  - petal_length.png")
print("  - petal_width.png")
print("  - sepal_length.png")
print("  - sepal_width.png")
print("  - pairplot.png")

print(" ")
print("Thank you for using this program")


file1.close()
# Closes CSV file.


# REFERENCES
# 1. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# 2. https://www.datacamp.com/community/tutorials/pandas-read-csv
# 3. https://www.geeksforgeeks.org/reading-writing-text-files-python/
# 4. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
# 5. https://datatofish.com/export-dataframe-to-csv/
# 6. https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
# 7. https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib
# 8. https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
# 9. https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset



