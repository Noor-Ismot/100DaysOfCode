#Problem statement: 
'''
Write a program to input an integer 'n' and print the sum of all its even digits and the sum of all its odd digits separately.

Digits mean numbers, not places! That is, if the given integer is "132456", even digits are 2, 4, and 6, and odd digits are 1, 3, and 5.

Constraints
0<= 'n' <=10000

Example :
Input: 'n' = 132456
Output: 12 9

Explanation:
The sum of even digits = 2 + 4 + 6 = 12
The sum of odd digits = 1 + 3 + 5 = 9
'''

userNumber = input()
evenDigitsSum = 0
oddDigitsSum = 0
for i in range(0, len(userNumber)):
    if int(userNumber[i]) % 2 == 0:
        evenDigitsSum += int(userNumber[i])
    else:
        oddDigitsSum += int(userNumber[i])
print(evenDigitsSum, oddDigitsSum)