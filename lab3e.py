'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 2 Question 1 (lab3e.py)
'''

import random #import random numbers
score = 0
count = 0

answer = ""

iscorrect2 = False
while (not iscorrect2): #Declare answer with sentinal
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    iscorrect = False
    while (not iscorrect):
        answer=input("Enter the answer1 to %s + %s, press 's' to skip or 'q' to quit:" %(num1,num2))

        if (answer == "q"): #if answer 'q' pressed
            iscorrect = True
            iscorrect2 = True
        elif (answer == "s"): # if answer 's' pressed
            count += 1 #if question is skipped then increasing question count by 1
            print("Question skipped. 0 points awarded.")
            iscorrect = True
        else:
            count += 1
            total = num1 + num2
            if (total == int(answer)): # if correct answer entered
                print("Correct! You have been awarded 1 point!") #giving 1 point for correct answer
                score += 1
                iscorrect = True
            else:
                print("Incorrect. Try again")

score_percentage = round((float((score/count)*100)),2) #calculating score percentage 

#printing summary
print("Total Questions: %s" %(count))
print("Total Score %s" %(score))
print("You received a grade of " + str(score_percentage) + "%")

