'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 2 Question 5 (lab4a.py)
'''
import random #importing random library
secret_num = random.randint(1,10)  #secret number between 1-10
iscorrect = False

while(not iscorrect):
    user_input = input("Enter a number between 1 and 10: ") #Ask for input
    if (user_input.isdigit()): #check user input a digit
        if (int(user_input) > 1 and int(user_input) < 10): #check input is a digit between 1-10
            print("Correct! You win.") #print wining message
            iscorrect = True
        elif user_input == '1' or user_input == '10': #if the user input is exactly 1 and 10
            print("Sorry. Try again.") #print sorry 
        else:
            print("Error: not a number or out of bounds.")
    else:
        print("Error: not a number or out of bounds.")