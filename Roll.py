import csv
import numpy as np


def getDataSource(data_path):
   roll = []
   marks = []

   with open(data_path)as csv_file:
       csv_reader = csv.DictReader(csv_file)
       for row in csv_reader:
           roll.append(float(row["Roll No"]))
           marks.append(float(row["Marks In Percentage"]))

   return{
     "x" : roll, "y": marks
    }

def findColleration(DataSource):
    colleration = np.corrcoef(DataSource["x"],DataSource["y"])
    print("colleration between Roll No and Marks in Percentage is",colleration[0,1])

def setup():
    data_path = 'csv/Roll.csv'

    DataSource = getDataSource(data_path)
    findColleration(DataSource)

setup()


