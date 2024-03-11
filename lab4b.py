'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 2 Question 6 (lab4b.py)
'''

def rtrn_area(length, width):  # definition of return of area
    '''
    function: rtrn_area
    Return area function
    parameter: length and width
    result: Area
    '''
    return length * width 


 
def print_all_caps(name, age):  # print Caps function
    '''
    function: print_all_caps
    parameter: name and age
    result : Print a statement in Upper case
    '''
    cap_name = name.upper() 
    print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age) + ' YEARS OLD!!!') 
    print_all_caps('eric', 41) 
    print_all_caps('melissa', 40) 

 
def get_rando():  # getting random numbers
     #importing random library
    '''
    function: ger_rando
    return: it returns random numbers between 1 to 101
    '''
    import random
    return random.randint(1, 101)

lucky_num = get_rando()  # getting a random number

 
def is_odd(num):  #checking odd or even number
    '''
    function: is_odd
    parameter: number
    returns: returns odd numbers
    '''
    if num % 2 == 1: 
        return True 
    else:  
        return False 
 
if __name__=="__main__":
    rect = rtrn_area(5,3)
    print(rect)
    print_all_caps('eric',41)
    print_all_caps('melissa', 40)
    lucky_num=get_rando()
    print(is_odd(13))
    print(is_odd(get_rando())) 

