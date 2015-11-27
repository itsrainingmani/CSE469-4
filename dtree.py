import csv

def initialgini(data, label):
    numPass = 0
    tSize = 0
    safety= 0

data = []

with open("golf.csv", "rb") as csvfile:
    golf = csv.reader(csvfile, delimiter= ',')
    for row in golf:
        data.append(row)

#label = ["unacc", "acc", "good", "vgood"]
label = ["yes","no"]
