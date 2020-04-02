# Jody Bradley
# This program....

# Import the libraries which we will be using [1]:
import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt


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

plt.plot(df['sepal_length'], df['sepal_width'], 'bo') 
plt.title("sepal length vs sepal width")
plt.show()

#plt.savefig("scatter.png")
#plt.clf()

#df.hist(figsize=(10,5))
#plt.show()

file1.close()
# Closes CSV file.






# REFERENCES
# 1. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# 2. https://www.datacamp.com/community/tutorials/pandas-read-csv
# 3. https://www.geeksforgeeks.org/reading-writing-text-files-python/
# 4. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
# 5. https://datatofish.com/export-dataframe-to-csv/


