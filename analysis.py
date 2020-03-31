# Jody Bradley
# This program....

# Import the libraries which we will be using [1]:
import pandas as pd
from pandas import read_csv
import numpy as np

data = pd.read_csv('iris.csv')

summary = data.describe()

# file1 = open(r"Iris-data.txt", "a")
# Creates and opens a text file titled Iris-data.txt [3]

# np.savetxt(r'Iris-data.txt', summary.values, fmt='%d')
# Saves summary to text file Iris-data.txt. However, there are no headings [4].

summary.to_csv(r'Iris-data.txt')
# Saves summary to CSV file. Headings and indices now included.





# file1.close()
# Closes text file Iris-data.txt




# REFERENCES
# 1. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# 2.https://www.datacamp.com/community/tutorials/pandas-read-csv
# 3. https://www.geeksforgeeks.org/reading-writing-text-files-python/
#4. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file


