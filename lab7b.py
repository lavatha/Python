'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 5 Question 1 (lab7b.py)
'''

def print_meal_plan(meal_plan):
    width = 50
    print (f"{'MENU FOR TODAY' : ^{width}}")
    print("=" * width)
    print(f"{'Breakfast' : <25}{meal_plan ['breakfast'] : >25}")
    print(f"{'Lunch' : <25}{meal_plan ['lunch'] : >25}")
    print(f"{'Dinner' : <25}{meal_plan ['dinner'] : >25}")
meal_plan = {'breakfast' : 'oatmeal', 'lunch': 'sandwiches', 'dinner': 'broccoli'}
print_meal_plan(meal_plan)