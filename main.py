#Reece Fagg - 16/8/2022
#First functionality, read the data and output it into a table

#imports
import csv

trafficData=[]
#read the data
with open('trafficdata.csv') as f:
    csv_reader=csv.reader(f,delimiter=',')
    for row in csv_reader:
        trafficData.append(row)

#TODO: change to a dict maybe, using the offense code as our key