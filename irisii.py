import pandas
from pandas import read_csv


f = open('iris.csv')
# stores reference to open file (as 'f').
# names = ['sepal-length', 'sepal-width', 'petal length', 'petal-width', 'class']
dataset = read_csv(f)

print(dataset.describe())



#REFERENCES
# 1.https://www.datacamp.com/community/tutorials/pandas-read-csv
# 2. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
