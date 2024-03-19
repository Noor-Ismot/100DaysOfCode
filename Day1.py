#Table of Content
#---------------------
"""
- How to take input in python
- How to display output in python default way
- How to display output in python custom way
- Type conversion
- Take input for List and display a list
- import library
- map() function 
"""

# Input Output in Python
# --------------------------
"""
age = input("What is your age:")
print(age)
print(type(age))
"""

#Type conversion in Python
#-------------------------------
"""
age = int(input("What is your age:"))
print(age)
print(type(age))
"""

#Take list element as Input
#-------------------------------

#Solution 1: Take list elements one by one, and append them to the list, size is necessary
"""
months = int(input("Number of months you have worked:"))
salaryList = list()
print("Enter each month salary")
for i in range(0,months):
    salaryList.append(int(input()))
print(salaryList)
"""

#Solution 2: map() and list() function
"""
print("Enter your each month's salary:")
salaryList = list(map(int,input().split()))
print("Your salary list:" , salaryList)
"""

#Output in Python
#---------------------

#Default: print(object(s), sep=’ ‘ ,end = ‘\n’, file = file, flush = flush) 
"""
print("I am Originally From Bangladesh.")
print("And","living","in","Sweden")
"""

#Print with Custom Separator and end
"""
print("I am Originally From Bangladesh ",end='+')
print("living","in","Sweden", sep=",")
"""

#Import in Python : By Importing the math Module, we are importing all the attributes, and functions into our program.
"""
import math
print("factorial of 5 is: ", end="")
print(math.factorial(5))
"""

#Importing specific attributes and functions, using from keyword
"""
from math import factorial
print("factorial of 5 is: ", end="")
print(factorial(5))
"""


#Sometimes module name could be large so then import it with a new name
"""
import math as m
print("factorial of 5 is: ", end="")
print(m.factorial(5))
"""
