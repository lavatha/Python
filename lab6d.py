'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 4 Question (lab6d.py)
'''
import sys

def remove_numbers(line):
    total = 0
    words = []
    for word in line.split(): # Iterate through each word in the line
        try:
            number = float(word) #convert the word to a float
            total += number #add the number to the total
        except ValueError:
            words.append(word) 
    return ' '.join(words), total #If conversion fails, add the word to the word list

def main():
    # Check for command-line argument
    if len(sys.argv) != 2:
        print("Usage: python lab6d.py <filename>") # Print usage message if incorrect number of arguments
        return
    
    filename = sys.argv[1] # Get the filename from command-line arguments

    try:
        with open(filename, 'r') as file:
            lines = file.readlines() # Read all lines from the file
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.") # Print error message if file not found
        return

    cleaned_lines = []
    for line in lines:
        cleaned_line, total = remove_numbers(line) # Omit numbers from each line and get the total sum
        print(total)
        cleaned_lines.append(cleaned_line.strip()) # Add cleaned line to the list of cleaned lines

    # Write back to the file
    with open(filename, 'w') as file:
        for line in cleaned_lines:
            file.write(line + '\n')  # Write each cleaned line back to the file

if __name__ == "__main__":
    main() # Call the main function if the script is executed directly
