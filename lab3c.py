'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 2 Question 3 (lab3c.py)
'''

sum = 0
print("SUMMING CALCULATOR") 
while True: 
    print("The sum so far: " + str(sum)) 
    user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") 
    if user_input == "": 
        break 
    else:  
        sum += int(user_input) 
print("Thank you for using summing calculator. The final sum was " + str(sum) 
+ ".")  