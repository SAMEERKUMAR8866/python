"""An if……else statement evaluates like this:
if the expression evaluates True:
Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

if the expression evaluates False:
Execute the block of code inside else statement. After execution return to the code out of the if……else block."""
book1_price = 1000
budget = 700
if book1_price <= budget:
    print("the book is in budget")
else:
    print("the book is out of budget")
"""elif Statements
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
the elif stamtement refers to the combination iof else and if condition which means when we have a third condition which does not follows the first condition instead have an another route before the execution of else statement."""
if book1_price<0:
    print ("the book price has fault")
elif book1_price==0:
    print ("the book is free")
else:
    print ("price is correct")
"""Nested if statements
We can use if, if-else, elif statements inside other if statements as well."""
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime  

