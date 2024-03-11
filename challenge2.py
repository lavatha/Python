'''
Name: Lavatharini
Description: Lab 1 Question 1 (lab1a.py)
'''

decimal_number = float(input("Enter a number with decimals: ")) # user input a decimal number
rounded_integer = int(decimal_number + 0.5) if decimal_number >= 0 else int(decimal_number - 0.5)
print( rounded_integer)
