from __future__ import division
import csv

inp = []

def outlook_gini(outlook):
    vals = ["Rainy", "Sunny", "Overcast"]
    calc = [[0,0,0] for i in range(0,2)]
    print calc
    for i in range(0,len(vals)):
        for j in range(0,14):
            if ((outlook['label'][j] == "Yes") and (outlook['outlook'][j] == vals[i])):
                calc[0][i] += 1
            elif ((outlook['label'][j] == "No") and (outlook['outlook'][j] == vals[i])):
                calc[1][i] += 1
    print calc
    denom = [(calc[0][i] + calc[1][i]) for i in range(0, len(vals))]
    print denom
    ginicalc = [1.0 for i in range(0,len(vals))]
    for i in range(0, len(vals)):
        for j in range(0, len(calc)):
            ginicalc[i] -= (calc[j][i]/denom[i])**(2)
    print ginicalc
    ogini = 0.0
    for i in range(0, len(vals)):
        ogini += ((denom[i]/14)*(ginicalc[i]))
    print ogini

def humid_gini(humid):
    vals = ["High", "Normal"]
    calc = [[0,0] for i in range(0,2)]
    key = "humid"
    for i in range(0,len(vals)):
        for j in range(0,14):
            if ((humid['label'][j] == "Yes") and (humid[key][j] == vals[i])):
                calc[0][i] += 1
            elif ((humid['label'][j] == "No") and (humid[key][j] == vals[i])):
                calc[1][i] += 1
    print calc
    denom = [(calc[0][i] + calc[1][i]) for i in range(0, len(vals))]
    ginicalc = [1.0 for i in range(0,len(vals))]
    for i in range(0, len(vals)):
        for j in range(0, len(calc)):
            ginicalc[i] -= (calc[j][i]/denom[i])**(2)
    ogini = 0.0
    for i in range(0, len(vals)):
        ogini += ((denom[i]/14)*(ginicalc[i]))
    print ogini

def temp_gini(temp):
    vals = ["hot", "mild", "cool"]
    calc = [[0,0,0] for i in range(0,2)]
    key = "temp"
    for i in range(0,len(vals)):
        for j in range(0,14):
            if ((outlook['label'][j] == "Yes") and (outlook[key][j] == vals[i])):
                calc[0][i] += 1
            elif ((outlook['label'][j] == "No") and (outlook[key][j] == vals[i])):
                calc[1][i] += 1
    print calc
    denom = [(calc[0][i] + calc[1][i]) for i in range(0, len(vals))]
    ginicalc = [1.0 for i in range(0,len(vals))]
    for i in range(0, len(vals)):
        for j in range(0, len(calc)):
            ginicalc[i] -= (calc[j][i]/denom[i])**(2)
    ogini = 0.0
    for i in range(0, len(vals)):
        ogini += ((denom[i]/14)*(ginicalc[i]))
    print ogini

def wind_gini(wind):
    vals = ["true", "false"]
    calc = [[0,0] for i in range(0,2)]
    key = "wind"
    for i in range(0,len(vals)):
        for j in range(0,14):
            if ((outlook['label'][j] == "Yes") and (outlook[key][j] == vals[i])):
                calc[0][i] += 1
            elif ((outlook['label'][j] == "No") and (outlook[key][j] == vals[i])):
                calc[1][i] += 1
    print calc
    denom = [(calc[0][i] + calc[1][i]) for i in range(0, len(vals))]
    ginicalc = [1.0 for i in range(0,len(vals))]
    for i in range(0, len(vals)):
        for j in range(0, len(calc)):
            ginicalc[i] -= (calc[j][i]/denom[i])**(2)
    ogini = 0.0
    for i in range(0, len(vals)):
        ogini += ((denom[i]/14)*(ginicalc[i]))
    print ogini

def gini(ginidict):
    cgini = ginidict

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

outlook_gini(ddict)
