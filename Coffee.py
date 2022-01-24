from calendar import week
import csv
import numpy as np




def getDataSource(data_path):
    week = []
    ml = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            week.append(float(row["week"]))
            ml.append(float(row["Coffee in ml"]))

    return{
        "x" : week, "y": ml
    }

def findColleration(dataSource):
    colleration = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Colleration between week and coffee in ml is ",colleration[0,1])

def setup():
    data_path = 'csv/coffee.csv'

    DataSource = getDataSource(data_path)
    findColleration(DataSource)

setup()

    
