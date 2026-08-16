"""loops are the term used in programming language to repeat some specific command multiple times.
The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries"""
name = 'satakshi'
for i in name:
    print(i, end=", ")
"""range(): it is the command given in the code when we accurately know how many time we want to repeat the code."""
#for k in range(5):
 #   print(k)
for k in range(1,10,5):
    print(k)
"""while Loop - is the loop which works only when the condition is true and when the condition becomes false the loop will terminate."""
count = 10
while (count > 0):
  print(count)
  count = count - 1
  """Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed."""
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
    """do..while is a loop in which a set of instructions will execute at least once and then the repetition of loops body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop."""
    #while True:
     #   number = int(input("Enter a positive number: "))
      #  print(number)
       # if not number > 0:
        #    break
"""break statement
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within."""
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("cutiepie")
print("Thank you")
"""Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur."""
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)
    