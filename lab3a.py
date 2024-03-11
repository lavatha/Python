'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 2 Question 1 (lab3a.py)
'''

num_1 = 0 
num_2 = 0
num_3 = 0
num_4 = 0
score1 = 0
score2 = 0
score3 = 0
score4 = 0
while num_1 != 26: 
    user_input = input("Enter the answer to 12 + 14, or, or press 's' to skip : ")
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    else:
        num_1 = int(user_input) 
    if num_1 != 26:
        print ("Incorrect. Try again.")
    else:
        print("Correct! You have been awarded 1 point!")
        print('Next question...')
        score1 = 25
    
while num_2 != 31: 
    user_input = input("Enter the answer to 23 + 8, or, or press 's' to skip : ")
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    else:
        num_2 = int(user_input) 
    if num_2 != 31:
        print ("Incorrect. Try again.")
    else:
        print("Correct! You have been awarded 1 point!")
        print('Next question...')
        score2 = 25

while num_3 != 43: 
    user_input = input("Enter the answer to 30 + 13, or, or press 's' to skip : ")
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    else:
        num_3 = int(user_input) 
    if num_3 != 43:
        print ("Incorrect. Try again.")
    else:
        print("Correct! You have been awarded 1 point!")
        print('Next question...')
        score3 = 25

while num_4 != 44: 
    user_input = input("Enter the answer to 17 + 27, or, or press 's' to skip : ")
    if user_input == 's':
        print("Question skipped. 0 points awarded.")
        break
    else:
        num_4 = int(user_input) 
    if num_4 != 44:
        print ("Incorrect. Try again.")
    else:
        print("Correct! You have been awarded 1 point!")
        score4= 25
result = int( score1 + score2 + score3 + score4 )
print("You received a grade of %.2f%%" % result)
   