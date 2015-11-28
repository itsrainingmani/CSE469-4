from __future__ import division
from copy import deepcopy
import csv

inp = []

def gini_calc(outlook, key, vals):
    #vals = ["Rainy", "Sunny", "Overcast"]
    if (len(vals) == 3):
        calc = [[0,0,0] for i in range(0,2)]
    elif (len(vals) == 2):
        calc = [[0,0] for i in range(0,2)]
    print calc
    for i in range(0,len(vals)):
        for j in range(0,14):
            if ((outlook['label'][j] == "Yes") and (outlook[key][j] == vals[i])):
                calc[0][i] += 1
            elif ((outlook['label'][j] == "No") and (outlook[key][j] == vals[i])):
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

def gini(ginidict, attributes, attrnames):
    cgini = ginidict
    cattr = attributes
    cnames = attrnames

    newattr = {}
    for key in cnames:
        newattr[key] = gini_calc(cgini, key, cattr[key])
    minkey = ""
    minval == 0
    for key in newattr:
        if newattr[key] < minval:
            minval = newattr[key]
            minkey = key

    print "the minimum GINI value is " + minkey + " so we split on it"

    arr = []

    for i in range(0, len(cnames)):
        arr.append(cgini[cnames[i]])
    arr.append(cgini['label'])

    recurdict = {}
    for i in cattr[minkey]:
        recurdict = deepcopy(cgini)
        recurattr = deepcopy(cattr)
        recurnname = deepcopy(cnames)
        removelist = []
        for j in range(0, len(recurdict[minkey])):
            if (recurdict[minkey][j] == i):
                removelist.append(j)
        for key in recurdict:
            recurdict[key] = [v for l, v in enumerate(recurdict[key]) if l not in removelist]
        del recurdict[minkey]
        del recurattr[minkey]
        recurnname.remove(minkey)
        gini(recurdict, recurattr, recurnname)


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

attr = {}
attr["humid"] = ["High", "Normal"]
attr["outlook"] = ["Rainy", "Sunny", "Overcast"]
attr["temp"] = ["Hot", "Mild", "Cool"]
attr["windy"] = ["True", "False"]
attr["label"] = ["Yes", "No"]

attrnames = ["outlook", "humid", "temp", "windy"]
