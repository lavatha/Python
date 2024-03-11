'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 3 Question 1 (lab5e.py)
'''

import sys
print(sys.argv) 

def calculate_average(numbers):
    
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers) #average calculation

def main():
   
    args = sys.argv[1:] #arguments

    if not args: #No argument
        print("Usage: Enter one or more command line arguments.")
        sys.exit(1) #Calculation stops if there is no argument

    numbers = [] #number list 

    for arg in args:
        try:
            number = int(arg) #argument in integer
            print(f"Number found: {number}.")
            numbers.append(number) #adding to the list
        except ValueError:
            print(f"Error: '{arg}' is not a number. ") #if input is not numerical value then print error

    average = calculate_average(numbers)

    
    if numbers:
        print(f"Average for {len(numbers)} numbers: {average:.1f}")

if __name__ == "__main__":
    main()

