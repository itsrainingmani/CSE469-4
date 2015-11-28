from __future__ import division
import csv

inp = []

def outlook_gini(outlook):
    vals = ["Rainy", "Sunny", "Overcast"]
    calc = [[0,0,0] for i in range(0,2)]
    for i in range(0,len(vals)):
        for j in range(0,14):
            if ((outlook['label'][j] == "Yes") and (outlook['outlook'][j] == vals[i])):
                calc[0][i] += 1
            elif ((outlook['label'][j] == "No") and (outlook['outlook'][j] == vals[i])):
                calc[1][i] += 1
    print calc
    denom = [(calc[0][i] + calc[1][i]) for i in range(0, len(vals))]
    ginicalc = [1.0 for i in range(0,3)]
    for i in range(0, len(vals)):
        for j in range(0, len(calc)):
            ginicalc[i] -= (calc[j][i]/denom[i])**(2)
    ogini = 0.0
    for i in range(0, len(vals)):
        ogini += ((denom[i]/14)*(ginicalc[i]))
    print ogini

def humid_gini(humid):
    vals = ["high", "normal"]
    calc = [[0,0] for i in range(0,2)]
    key = "humid"

def temp_gini(temp):
    vals = ["hot", "mild", "cool"]
    calc = [[0,0,0] for i in range(0,2)]
    key = "temp"

def wind_gini(wind):
    vals = ["true", "false"]
    calc = [[0,0] for i in range(0,2)]
    key = "wind"

with open("golf.csv", 'rb') as csvfile:
    golfReader = csv.reader(csvfile, delimiter=',')
    for row in golfReader:
        inp.append(row)

ddict = {}
ddict["outlook"] = [inp[i][0] for i in range(0, 14)]
ddict["temp"] = [inp[i][1] for i in range(0, 14)]
ddict["humid"] = [inp[i][2] for i in range(0, 14)]
ddict["windy"] = [inp[i][3] for i in range(0, 14)]
ddict["label"] = [inp[i][4] for i in range(0, 14)]
