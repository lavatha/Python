'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 3 Question 1 (lab5a.py)
'''
def my_sum(numbers): #definition of my sum
    total=0
    for num in numbers:
        total += num
    return total #reruning argument

if __name__ == "__main__": 
    user_numbers = [] #empty list
    print("AVERAGE CALCULATOR") 
    while True: 
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ") #Print statement for user input
        if user_input == "": #if user enter the enter then it will end the program
            break 
        else:  
            user_numbers.append(int(user_input)) #Appends the integer value of user_input to the end of the list user_numbers
    num_sum = my_sum(user_numbers) #summing the number
    num_length = len(user_numbers) #length of the list 
    average = num_sum / num_length #average calculation
    print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this list is: {average}.") 
    print("Thank you for using average calculator")