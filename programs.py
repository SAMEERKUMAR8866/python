"""PROGRAM TO PRINT THE SUM OF TWO NUMBERS"""
def sum(a,b):
    return a+b

a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("sum of two numbers is:",sum(a,b))

"""from gzip import WRITE


WRITE A PYTHON CODE TO PRINT HELLO WORLD"""
print("hello world")
"""write a program to input two numbers and find their sum"""
a=int(input("enter the first number"))
b=int(input("enter a second number"))
c = a+b
print(c)

"""WRITE A PROGRAM TO FIND THE AREA OF A CIRCLE"""
r=int(input("enter the radius of circle"))
area=3.14*r*r
print(area)
"""WRITE A PROGRAM TO SWAP TWO NUMBERS"""
a=5
b=6
temp=a
a=b
print(temp,a)
"""write a program to check weather a number is even or odd"""
n=int(input("enter a number"))
if (n%2==0):
    print("n is even")
else:
    print("n is odd")
"""write a program to check whether a number is positive,negative or zero"""
n=int(input("enter a number"))
if n>0:
   print("n is positive")
elif n<0:
   print("n is negative")
else:
   print("n is zero") 
   """WRITE A PROGRAM TO FIND THE LARGEST OF TWO NUMBER"""
a=int(input("enter a number"))
b=int(input("enter sec no"))
if a>=b:
    print("a is greatest")
else :
    print("b is greatest")
"""WRITE A PYTHON PROGRAM TO FIND THE LARGEST OF THREE NUMBERS""" 
a=int(input("enter a number"))
b=int(input("enter sec no"))
c=int(input("enter a number"))
if a>=b and a>=c:
    print ("a is greatest")
elif b>=a and b>=c:
    print ("b is greatest")
else:
    print("c is greatest")
"""WRITE A PROGRAM TO CHECK WHTHER A YEAR IS LEAP YEAR OR NOT"""
N = input("enter the year")
if n%400==0:
    print ("N is leap year")
else:
    print("N is not leap year")
"""write a program to calcute simple interest"""
p=input("enter a p.i value")
r=input("enter the r value")
T=input("enter the time")
SI=(p*r*T)/100
print("SI")
