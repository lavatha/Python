'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 5 Question 1 (lab7a.py)
'''

student1 = {'first_name': 'eric', 'last_name': 'smith', 'addr1': '217 Au Large Blvd', 'city': 'Toronto', 'prov': 'Ontario', 'pcode': 'M4A 1P3'}

def shipping_label(a_dict):
    "takes a dictionary, generates a string"
    a_str = f"{a_dict['first_name'].capitalize()} {a_dict['last_name'].capitalize()}\n"
    a_str += f"{a_dict['addr1']}\n"
    a_str += f"{a_dict['city']}, {a_dict['prov']}\n"
    a_str += f"{a_dict['pcode']}"
    return a_str

print(shipping_label(student1))
