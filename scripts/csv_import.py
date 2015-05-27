'''
Created on Nov 24, 2014

@author: sschubiger
'''
from scripting import *

import csv

# get a CityEngine instance
ce = CE()

states = {}
print "start"
if __name__ == '__main__':
    f = open('/Users/fs/Dropbox/fhwn/sync_S6/ivis_6id/ivis/CityEngine_2015/Vermoegensverteilung.csv', 'rU')
    try:
        reader = csv.reader(f,  delimiter=';')
        print "read csv"
        for row in reader:
            try:
                if (states.has_key(float(row[1])) != True):
                    states[float(row[1])] = {}
                if (states[float(row[1])].has_key(float(row[0])-2003) != True):
                    states[float(row[1])][float(row[0])-2003] = {}
                if (states[float(row[1])][float(row[0])-2003].has_key(row[3]) != True):
                    states[float(row[1])][float(row[0])-2003][float(row[3])] = {}
                states[float(row[1])][float(row[0])-2003][float(row[3])] = float(row[5])
                print "."
            except ValueError:
                pass
        
    finally:
        f.close()
            
    print states
    for shape in ce.getObjectsFrom(ce.getObjectsFrom(ce.scene, ce.withName('Gemeinden'))[0]):
        gemeindeNr = ce.getAttribute(shape, 'GMDNR')
        if states.has_key(gemeindeNr) == False:
            continue;
        fortuneInfo = states[gemeindeNr]
        pop = []
        for i in fortuneInfo:
            amount = 0
            if (fortuneInfo[i].has_key(1.0)):
                amount += fortuneInfo[i][1.0]
            if (fortuneInfo[i].has_key(2.0)):
                amount += fortuneInfo[i][2.0];
            pop.append(amount)
        ce.setAttribute(shape, "FORTUNE10M", pop)
        ce.setAttributeSource(shape, "FORTUNE10M", "OBJECT")


