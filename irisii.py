import csv
# imports csv module

f = open('iris.csv')
# stores reference to open file (as 'f').

csv_f = csv.reader(f)

for row in csv_f:
    sepal_length = (row[0])
    sepal_width = (row[1])
    petal_length = (row[2])
    petal_width = (row[3])
    variety = (row[4])
   



#for row in csv_f:
 #   print(row[2])










#REFERENCES
# 1. https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737