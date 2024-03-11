'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 3 Question 1 (lab5d.py)
'''

import sys 
 
print(sys.argv) 
print(f"The name of the file you are running is: {sys.argv[0]}.") 
 
if len(sys.argv) == 1: 
    print("No arguments found.") 
else: 
    for arg in sys.argv[1:]:  # start from the second item in the list 
        print(f"Argument found: {arg}.") 
print("Complete.") 

