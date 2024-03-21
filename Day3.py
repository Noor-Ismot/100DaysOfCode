# For Loop: A for loop is a control structure in programming that allows you to execute a specific block of code repeatedly. It’s especially useful when you want to perform the same task multiple times without duplicating your code.
"""
userNumber = int(input("Enter your last number:"))
for i in range(1, userNumber+1):
    if i % 2 == 0 :
        print(i," is a even number")
    else:
        print(i," is odd number")
"""

"""
#set iteration withing range() function
userNumber = int(input("Enter your last number:"))
for i in range(1, userNumber+1,2):
    if i % 2 == 0 :
        print(i," is a even number")
    else:
        print(i," is odd number")
"""

#Nested Loop : This concept becomes incredibly useful when you’re working with multi-dimensional data structures like a 2-D Array or need to solve complex problems involving multiple iterations.
"""
userNumber = int(input("Enter your number:"))
for i in range(1, userNumber+1):
    for j in range(0, i):
        print("*",end="")
    print("\n")     
"""

#url: https://kinsta.com/blog/iterables-in-python/
        