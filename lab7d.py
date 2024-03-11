'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 5 Question 1 (lab7c.py)
'''


import csv 
import sys

def readcsv(filename):

    list_of_dicts = [] 
    f = open('sample.csv', 'r') 
    reader = csv.DictReader(f) 
    for row in reader: 
       list_of_dicts.append(row) 
    f.close()
    return list_of_dicts

def writecsv(filename, listofdicts):
    f=open(filename, 'w')
    fieldnames=listofdicts[0].keys()
    w=csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in listofdicts:
        try:
            if (row["First Name"] == "Christopher"):
                row["First Name"] = "Chris"
            if (row["Last Name"] == "Patal"):
                row["Last Name"]= "Patel"
            elif(row["Last Name"]=="Smith"):
                row["Last Name"] = "Nichols"
            elif (row["Last Name"] == "Geary"):
                row["Address"]= "455 Bloor"
            if(row["Address"]=="81 Vanier"):
                row["Address"] = "72 Princeton"
            if(row["City"]=="North York"):
                row["Address"] = "Toronto"
            if(row["Country"]=="Canada"):
                row["Country"] = "CA"
        except KeyError as e:
            print("Handling key error" + str(e))
        w.writerow(row)
    f.close

if len(sys.argv) == 1: #when no enough arguments
    print("Usage: lab7d.py filename")
else:
    filename=sys.argv[1]
    outfile = "out_" + filename
    try:
        writecsv(outfile, readcsv(filename))
    except:
        print(f"ERROR: {filename} not found.") #file not found error