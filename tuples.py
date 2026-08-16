"""Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation."""
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
"""Tuple Indexes
Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on."""
"""Accessing tuple items:
I. Positive Indexing:
As we have seen that tuple items have index, as such we can access items using these indexes.
II. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on."""
"""Check for item:
We can check if a given item is present in the tuple. This is done using the in keyword.

Example 1:"""
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
"""Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

Syntax:
Tuple[start : end : jumpIndex]"""
"""Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

Example:"""
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
"""Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.
However, we can directly concatenate two tuples without converting them to list.
Example:"""
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
"""Tuple methods
As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

count() Method
The count() method of Tuple returns the number of times the given element appears in the tuple."""
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
"""index() method
The Index() method returns the first occurrence of the given element from the tuple."""
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
"""Note: This method raises a ValueError if the element is not found in the tuple."""

