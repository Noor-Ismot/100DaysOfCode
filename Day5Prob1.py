'''
Problem statement
Functions - Take this coding challenge to test your coding skills to

-define a function

-pass arguments by value to a function

-pass arguments by reference to a function

This coding challenge is organized in the following way:

First line of input reads an integer to select the coding challenge:

-Reading value '1' selects the coding-challenge 1 ( tests the ability to define a function and pass arguments by value.)

-Reading value '2' selects the coding challenge 2 (tests the ability to pass arguments by reference to a function)

Coding Challenge -1
Define a function named "Maximum" that accepts two integers (pass by value) as arguments and returns the greatest of the two arguments.

Coding Challenge -2
Define a function named "Swap" that accepts two integers (pass by reference) as arguments and swaps their value.
'''

#My solution
'''
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
    
def swap(x,y):
    tempVal = x
    x=y
    y=tempVal
    return x,y

challenge = int(input())
x, y= input().split()
x = int(x)
y= int(y)

if challenge ==1 :
    print(maximum(x,y))

else:
    x, y = swap(x,y)
    print(x,y)
'''

'''
In Python, you can't directly pass arguments by reference. However, you can achieve a similar effect by passing mutable objects like lists. Here's how you can implement the swap function
'''

def maximum(a,b):
    return max(a,b)
    
def swap(aList):
 aList[0], aList[1] = aList[1], aList[0]
 return aList[0], aList[1]

challenge = int(input())
x, y= input().split()
x = int(x)
y= int(y)

if challenge ==1 :
    print(maximum(x,y))

else:
    numList = [x,y]
    swap(numList)
    print(numList[0], numList[1])

