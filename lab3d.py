'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 2 Question 4 (lab3d.py)
'''
import random #importing random library
secret_num = random.randint(1,10)  #secret number between 1-10
while True:
    guess = int(input("Guess a number between 1 and 10: ")) #Ask for guess
    if guess == secret_num: #check for correct match
         print("Correct! You win") #If the guess is correct declare the victory
         break
    else:
        print("Sorry, that's not it.") #if guess is wrong declare loss

