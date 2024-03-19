#Problem Statement
"""
Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.
1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.
"""

#Solution - 1
"""
#Take user input and get the ASCII value with ord() function
charValue = ord(input())

#Conditions to check ASCII value and Display output accordingly
if charValue >= 65 and charValue <=90:
    print("1")
elif charValue >= 97 and charValue <=122:
    print("0")
else:
    print("-1")
"""

##Solution - 2
charValue = input()

#Conditions to check value and Display output accordingly
if charValue >= 'A' and charValue <='Z':
    print("1")
elif charValue >= 'a' and charValue <= 'z':
    print("0")
else:
    print("-1")