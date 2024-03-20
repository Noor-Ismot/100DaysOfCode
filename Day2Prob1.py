#Problem Statement
"""
Problem statement
Data type refers to the type of value a variable has and the way the computer interprets it.
Each data type has a different size. You’ve studied 5 different data types and the sizes of the data types:

Integer: 4 bytes
Long: 8 bytes
Float: 4 bytes
Double: 8 bytes
Character: 1 byte

You’re given a data type. Print its size in bytes.
"""
#take user input
userInput = input()

#Match the data type and display text
match userInput:
    case 'Integer':
        print("4")
    case 'Long':
        print("8")
    case "Float":
        print("4")
    case "Double":
        print("8")
    case "Character":
        print("1") 
    case _:
        print("Enter a valid Data Type!")
    