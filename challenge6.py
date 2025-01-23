'''
Name: Lavatharini
Description: Lab 4 Question
'''


import sys

def find_last_letter(line):
    closest_to_z = None # Initialize variable to store the closest letter to 'z'
    for char in line.lower(): 
        if char.isalpha(): # Check if the character is an alphabet
            if closest_to_z is None or char > closest_to_z: # If closest_to_z is None or the current character is greater than the closest_to_z
                closest_to_z = char 
                
    return closest_to_z    

if len(sys.argv) != 2: # Check if the number of command line arguments is not equal to 2
    print("Usage: python challenge6.py <filename>") 
else:
    filename = sys.argv[1] # Get the filename
    try:
        with open(filename, 'r') as file:
            for line in file: 
                last_letter = find_last_letter(line) 
                if last_letter:
                    print(last_letter) # If last_letter is not None, print it

    except FileNotFoundError:  # If the file is not found, catch the FileNotFoundError exception
        print(f"ERROR: File '{filename}' not found.")# Print an error message with the filename
