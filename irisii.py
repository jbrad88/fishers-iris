import csv
# imports csv module

f = open('iris.csv')
# stores reference to open file (as 'f').

csv_f = csv.reader(f)

for row in csv_f:
    x = (row[0])
    print(x)



#for row in csv_f:
 #   print(row[2])










#REFERENCES
# 1. https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737