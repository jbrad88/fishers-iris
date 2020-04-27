# Jody Bradley

# Import the libraries which we will be using [3] [8]:
import csv
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import seaborn as sns

# The first part of this program will output a summary of each variable to a single text file (in CSV format).
# This will give the user the mean, the standard variation, the minimum, the maximum of each of the four attributes
# (sepal length, sepal width, petal length and petal width).

df = pd.read_csv('iris.csv')
# Loads data from the CSV file 'iris.csv' into pandas dataframe [4].
col=['sepal_length','sepal_width','petal_length','petal_width','species']

# This below prints text for illustrative purposes to tell the user what the program is doing.
print(" ")
print("This program provides an analysis of the well-known Fisher's Iris data set.")
print(" ")
print("There are three species of Iris included in this data set, as follows:")
print(df.groupby('species').size())
# prints the number of samples for each of the three species.
print(" ")
print("The first ten rows of the sample gives an overview of the variables:")
print(" ")
print(df.head(n=11))
# prints the headings and the first 10 rows.
print(" ")
print("Below is a summary of each variable:") 
print(" ")
summary = df.describe()
# defining the df.describe() function as "summary". This function provides a a summary of the data set incl. count, mean, standard deviation, min and max values.
print(summary)
print(" ")

# Next, we want to create and opens a CSV file titled Iris-data [5] [6].
file1 = open(r"Iris-data.csv", 'a')

summary.to_csv(r'Iris-data.csv')
# Saves summary to a CSV file[7]

print("A text file of this data has now been saved in the program folder as a CSV file titled iris.csv.")
print(" ")

# Next we want to divide the data set into the three species [8]:
iris_setosa=df.loc[df["species"]=="Iris-setosa"]
iris_virginica=df.loc[df["species"]=="Iris-virginica"]
iris_versicolor=df.loc[df["species"]=="Iris-versicolor"]

# This next part of the program will save a histrogram as a PNG for each of the four variables [9]. We need to make sure to close the file after each .png file is saved. This
# is done using plt.clf after each.
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

# This final part of the program produces a matrix of relationships between each pair of variables using the Seaborn "pairplot" function [9].
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
#1. http://archive.ics.uci.edu/ml/datasets/iris
#2. https://www.techopedia.com/definition/32880/iris-flower-data-set
#3. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
#4. https://www.datacamp.com/community/tutorials/pandas-read-csv
#5. https://www.geeksforgeeks.org/reading-writing-text-files-python/
#6. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
#7. https://datatofish.com/export-dataframe-to-csv/
#8. https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
#9. https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#10. https://github.com/adobe-type-tools/python-scripts/blob/master/README.md

