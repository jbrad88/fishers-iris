# This is a step-by-step from the internet. I am trialling this to assist
# me with this task. See references below.

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
# load the libraries which we will be using.

# Next we will load the data set. NOTE: For the assignment we are using a downloaded CSV file. Therefore
# a different approach will be required to loan the data set.
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# We can see how many instances (rows) and attributes (columns) the data contains using the 'shape' property.
print(dataset.shape)

# We can see a summary of each attribute using the 'describe' property.
print(dataset.describe())




# REFERENCES
# 1. https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
