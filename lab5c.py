'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 3 (lab5c.py)
'''

import random

animals = ['snake', 'hamster', 'scorpion', 'beaver', 'mosquito', 'camel', 'vulture', 'horse', 'python', 'capybara' ]
secret = random.choice(animals) # randomly get animals out of the list


print("I'm thinking of an animal. Can you guess what it is? ") #print 
while True:
    guess = input("Enter a letter or a guess. Press enter to quit:") #user input
    if guess == "": #if user press enter qiut the game.
            print ("Game Over!")
            break
            
    elif len(guess)== 1: # guess only one letter
        if guess in secret: # if user guess correct letter, inside the secret list animal then give him another chance to guess
         print("Yes, my word contains that letter.") #user guessed the correct letter
        else:
         print ("Sorry, my word doesn't contain that letter.") #user guess was incorrect
    
    elif guess == secret: #user gussed the secrect animal 
        print("You win!")
        break
    
    else :
        print("Sorry, that's not it.") #incorrect guess of the word


