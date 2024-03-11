'''
Name: Lavatharini
Student ID: 153494232
Description: Lab 4 Question 1 (lab6a.py)
'''

data_to_write = ['First Line!', 'Second Line!!', 'Third Line!!!', '...and so on!']
f = open('testing.txt', 'w') #open file
for i in data_to_write:
    f.write(i + "\n") #write each element of list and followed by a new line
f.close() #close the file