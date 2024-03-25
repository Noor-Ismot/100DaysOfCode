#Problem Statement
"""
The n-th term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -

    F(n) = F(n - 1) + F(n - 2), 
    Where, F(1) = 1, F(2) = 1

Provided 'n' you have to find out the n-th Fibonacci Number. Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like if else and return what's expected.

"Indexing is start from 1"

Example :
Input: 6
Output: 8

"""

'''
#Series:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233...
'''
def fibonacci(n):
    if n <= 0:
        return "Incorrect Input"
    elif n == 1 or n == 2:
        return 1
    else:
        fib_sequence = [0, 1, 1]
        for i in range(3, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[n]

print(fibonacci(int(input())))





