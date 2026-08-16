import time 
timestamp = time.strftime('%H:%M:%S')
if timestamp < '12:00:00':
    print("good morning", timestamp)
elif timestamp <'18:00:00':
    print("good afternoon", timestamp)
elif timestamp <'21:00:00':
    print("good evevening", timestamp)
else:
    print("good night", timestamp)

"""MATCH CASE STATEMENT
the match statement is the type of statemnt eshtablished in puthon 3.10 i.e the latest version of python in this statement a specific value of any kind is given to match using cases method like there are made many different type of cases in which we have to find whether it matched the value  or pattern.
while the cases have a sequence order that the cases will be checked line by line if it matches the first case then it will give the output or not then also it will not terminate the rest of cases"""
x = 10 
match x:
if x