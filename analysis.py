# Jody Bradley
# This program....

# Import the libraries which we will be using [1]:
import pandas as pd
from pandas import read_csv
import numpy as np

data = pd.read_csv('iris.csv')

summary = data.describe()

file1 = open(r"Iris-data.csv", "a")
# Creates and opens a CSV file titled Iris-data [3]

summary.to_csv(r'Iris-data.csv')
# Saves summary to a CSV file[5]

file1.close()
# Closes CSV file.






# REFERENCES
# 1. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# 2.https://www.datacamp.com/community/tutorials/pandas-read-csv
# 3. https://www.geeksforgeeks.org/reading-writing-text-files-python/
# 4. https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
# 5. https://datatofish.com/export-dataframe-to-csv/


