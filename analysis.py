import pandas as pd
from pandas import read_csv
import numpy as np 

data = pd.read_csv('iris.csv')

print(data.describe())
