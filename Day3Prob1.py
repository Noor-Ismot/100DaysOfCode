#Problem Statement
"""
Problem statement
The n-th term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -

    F(n) = F(n - 1) + F(n - 2), 
    Where, F(1) = 1, F(2) = 1

Provided 'n' you have to find out the n-th Fibonacci Number. Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like if else and return what's expected.

"Indexing is start from 1"

Example :
Input: 6

Output: 8

"""

userNumber = int(input())
fibList = list(1)
if userNumber == 1 :
    print("1")
else:
    for i in range(2, userNumber+1):
        newNumber = (i- 1) + (i-2)
        fibList.append(newNumber)
    print(fibList[userNumber])



