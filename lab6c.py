'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 4 Question (lab6c.py)
'''


import sys

if len(sys.argv) < 3: #Checking whether there are fewer than three command-line options.
    print(f"Usage: {sys.argv[0]} keyword filename") 

else:
    key_word = sys.argv[1] #gettingthe keyword from the command-line arguments
    file_name = sys.argv[2] #getting the filename from the command-line arguments

    print(f"{file_name}") #Printing the filename for confirmation
    print(f"{key_word}") #Printing the keyword for confirmation
    try:
        f = open(file_name, 'r') 
    except FileNotFoundError: #if the FileNotFoundError does not exist
        print(f"ERROR: {file_name} was not found.") 
        sys.exit(1) #Exiting the program with exit code 1


    lines = f.readlines() # Reading all lines from the file into a content list

    for line in lines: # Iterating through each line in the list of lines
        if key_word in line: # Checking if the keyword is present in the line
            index = lines.index(line)+1 # Determining the index 
            print(f"{index}: {line.strip()}")  # Print the line number and the line content

        else:
            exit # Exiting the loop if the keyword is not found
    
    f.close() 
    sys.exit() 
