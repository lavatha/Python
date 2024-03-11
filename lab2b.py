'''
Name: Lavatharini
Description: Lab 1 Question 1 (lab1a.py)
'''

STANDARD_DEDUCTION = 10000.00 #Standard deduction is $10000 and its constant
DEPENDENT_DEDUCTION = 2000.00 #Per Dependent deduction is $2000 and its constant

TAXRATE_1 = 0.10 #tax rate for <= $32000 is 10% hence 0.10
TAXRATE_2 = 0.15 #tax rate for > $32000 and <= 64000 is 15% hence 0.15
TAXRATE_3 = 0.25 # tax rate for > 64000 is 25% hence o.25
TAXRATE = 0.00 # empty tax rate

TAX = 0.00 # empty tax to use later

grossincome = float(input("Enter your gross income: "))
dependents = int(input("Enter the number of dependents: "))

taxable_income = (grossincome - (STANDARD_DEDUCTION + (dependents * DEPENDENT_DEDUCTION)))

#based on taxable income and tax rate calculating TAX

if (grossincome <= 32000.00): 
    TAX_RATE = TAXRATE_1
    TAX = TAX_RATE * taxable_income
elif (grossincome > 32000.00 and grossincome <= 64000.00):
    TAX_RATE = TAXRATE_2
    TAX = TAX_RATE * taxable_income
else:
    TAX_RATE = TAXRATE_3
    TAX = TAX_RATE * taxable_income
#If tax is 0 or negative then tax is $0
if (TAX <= 0):
    TAX = 0.00

#Print the tax
print("The income tax is $%0.2f" %(TAX))
