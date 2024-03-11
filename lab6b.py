'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 4 Question (lab6b.py)
'''

import sys
 
def reverse(filename):
    try:
        with open(filename, 'r') as file: #open the file 
            lines = file.readlines() #read all lines 
            reversed_lines = reversed(lines) #reverse the order of contents
            for line in reversed_lines: 
                print(line.rstrip())  #Print each line without trailing whitespace
    except FileNotFoundError: #if specified file is not found
        print(f"Error: File '{filename}' is not found.")
 
if __name__ == "__main__":
    
    if len(sys.argv) > 1: #Check if command line arguments are provided
        filename = sys.argv[1] # If provided, use the first argument as the filename
    else:
        filename = 'readme.txt' # If no arguments provided, use 'readme.txt' as the default filename
        
    reverse(filename) # Call the reverse_read function with the default filename