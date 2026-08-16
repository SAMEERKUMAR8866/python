"""The conversion of one data type into the other data type is known as type casting in python or type conversion in python."""
"""Two Types of Typecasting:
Explicit Conversion (Explicit type casting in python)
Implicit Conversion (Implicit type casting in python)."""
"""Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion."""
string = "33"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
"""Implicit type casting:
The conversion of one data type into another data type, done automatically by the Python interpreter, is known as implicit type conversion."""
a = 7
print(type(a))
b = 3.0
print(type(b))
c = a + b
print(c)
print(type(c))