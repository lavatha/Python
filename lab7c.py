'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 5 Question 1 (lab7c.py)
'''

from lab7b import print_meal_plan


menu = [] #creating empty list
template = {'breakfast': None, 'lunch': None, 'dinner': None} # declaring no value template

while True:
    day = input("Would you like to add a day? (y/n): ") #input
    if day == 'n': # when input is n
        break
    elif day == 'y': #when input is y
        new_day = template.copy() # creating a new day template
        for i in new_day: # adding items to new template
            new_day[i] = input(f"Please enter your meal preference for {i}: ")
        menu.append(new_day)
    else: 
        print("Invalid input. Please enter 'y' or 'n': ")

day_num = int(input("Please enter a day number for the menu you would like to print (1-{}): ".format(len(menu))))
print_meal_plan(menu[day_num -1])

