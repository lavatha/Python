'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 4 Question (challenge6.py)
'''


import sys

def find_last_letter(line):
    closest_to_z = None # Initialize variable to store the closest letter to 'z'
    for char in line.lower():  # Iterate through each character in the line
        if char.isalpha(): # Check if the character is an alphabet
            if closest_to_z is None or char > closest_to_z: # If closest_to_z is None or the current character is greater than the closest_to_z
                closest_to_z = char # Update closest_to_z with the current character
                
    return closest_to_z    # Return the closest letter to 'z'

if len(sys.argv) != 2: # Check if the number of command line arguments is not equal to 2
    print("Usage: python challenge6.py <filename>") # Print usage message
else:
    filename = sys.argv[1] # Get the filename
    try:
        with open(filename, 'r') as file:
            for line in file: # Iterate through each line in the file
                last_letter = find_last_letter(line) # Find the last letter in the line
                if last_letter:
                    print(last_letter) # If last_letter is not None, print it

    except FileNotFoundError:  # If the file is not found, catch the FileNotFoundError exception
        print(f"ERROR: File '{filename}' not found.")# Print an error message with the filename
