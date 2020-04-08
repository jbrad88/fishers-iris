# Jody Bradley
# This program....

# Import the libraries which we will be using [1]:
import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The first part of this program will output a summary of each variable to a single text file (in CSV format).
# This will give the user the mean, the standard variation, the minimum, the maximum of each of the four attributes
# (sepal length, sepal width, petal length and petal width).

df = pd.read_csv('iris.csv')
# Loans data from the CSV file 'iris.csv' into pandas dataframe.

summary = df.describe()

file1 = open(r"Iris-data.csv", 'a')
# Creates and opens a CSV file titled Iris-data [3]

summary.to_csv(r'Iris-data.csv')
# Saves summary to a CSV file[5]

# This next part of the program will save a histrogram as a PNG for each of the four variables.
plt.hist(df["sepal_length"])
plt.title("Sepal Length")
plt.savefig("sepal_length.png")
plt.clf()
# Saves histrogram for Sepal Length as PNG

plt.hist(df["sepal_width"])
plt.savefig("sepal_width.png")
plt.clf()
# Saves histrogram for Sepal width as PNG

plt.hist(df["petal_length"])
plt.savefig("petal_length.png")
plt.clf()
# Saves histrogram for petal length as PNG

plt.hist(df["petal_width"])
plt.savefig("petal_width.png")
plt.clf()
# Saves histrogram for petal width as PNG

# This next part of the program will save a scatter plot of each pair of variables: (i) sepal length to sepal width;
# and (ii) petal length to petal width.

plt.plot(df["sepal_length"], df["sepal_width"], 'b,') 
plt.title("Sepal Length vs Sepal Width")
plt.savefig("sepal_scatter.png")
plt.clf()

plt.plot(df["petal_length"], df["petal_width"], 'b,') 
plt.title("Petal Length vs Petal Width")
plt.savefig("petal_scatter.png")
plt.clf()


file1.close()
# Closes CSV file.






# REFERENCES
# 1. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# 2. https://www.datacamp.com/community/tutorials/pandas-read-csv
# 3. https://www.geeksforgeeks.org/reading-writing-text-files-python/
# 4. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
# 5. https://datatofish.com/export-dataframe-to-csv/
# 6. https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python


