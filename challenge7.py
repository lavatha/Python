'''
Name: Lavatharini
Description: Lab 5 challenge Question 1
'''

import csv
import sys

def readcsv(filename):
    list_of_dicts = [] 
    f = open(filename, 'r')
    reader = csv.DictReader(f)
    for row in reader: 
        list_of_dicts.append(row)
    f.close() 
    return list_of_dicts

def writecsv(filename, listofdicts):
    f = open(filename, 'w')
    fieldnames = listofdicts[0].keys()
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in listofdicts:
        try:
            if (row["First Name"] == "Christopher"):
                row["First Name"] = "Chris"
            if (row["Last Name"] == "Patal"):
                row["Last Name"] = "Patel"
            elif (row["Last Name"] == "Smith"):
                row["Last Name"] = "Nichols"
            elif (row["Last Name"] == "Geary"):
                row["Address"] = "455 Bloor"
            if (row["Address"] == "81 Vanier"):
                row["Address"] = "72 Princeton"
            if (row["City"] == "North York"):
                row["City"] = "Toronto"
            if (row["Country"] == "Canada"):
                row["Country"] = "CA"
        except KeyError as e:
            print ("Handling key error" + str(e))
        w.writerow(row)
    f.close()
    
def print_modified_table(listofdicts):
    if listofdicts:
        fieldnames = listofdicts[0].keys()
        header = " | ".join(fieldnames)
        print(header)
        print("-" * (len(header) + len(fieldnames) - 1))

        for row in listofdicts:
            print(f"{row['First Name']: <10} | {row['Last Name']: <10} | {row['GPA']: <4}")

if len(sys.argv) == 1:
    print("Usage: lab7d.py filename")
else:
    filename = sys.argv[1] # Get filename
    outfile = "out_" + filename
    try:
        data = readcsv(filename)
        writecsv(outfile, data)
        print_modified_table(data)
    except FileNotFoundError:
        print("ERROR: %s not found." % filename)
