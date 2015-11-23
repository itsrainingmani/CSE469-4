import csv

def initialgini(ddata, label):
    numPass = 0
    tSize = 0
    safety= 0

data = []

with open("car.csv", "rb") as csvfile:
    golf = csv.reader(csvfile, delimiter= ',')
    for row in golf:
        data.append(row)

ddata = []

ddata.append([data[i][0] for i in xrange(14)])
ddata.append([data[i][1] for i in xrange(14)])
ddata.append([data[i][2] for i in xrange(14)])
ddata.append([data[i][3] for i in xrange(14)])

label = ["unacc", "acc", "good", "vgood"]
