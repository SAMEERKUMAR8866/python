"""In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable"""
#a=input("Enter the name: ")
#print(a)

"""STRINGS"""
""" A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters."""
#name = "satakshi"
#print("Hello, " + name)
"""it does not matter whether we use single or double quotes in strings."""
"""Multiline Strings
If our string has multiple lines, we can create them like this:"""
a="my name is satakshi and i am a btech student\n i am in second semester"
print(a)
"""Accessing Characters of a String
we use indexing method to access a character in a string because string has array like format and accepts indexing."""
print(a[0])
print(a[1])
"""Looping through the string
We can loop through strings using a for loop like this:"""

for character in a:
    print(character)