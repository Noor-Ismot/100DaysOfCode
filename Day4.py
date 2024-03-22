#Day 4 :
# While Loop
# break
# continue

#While loop: Used to iterate over code when the condition is true. This loop type is typically used when the number of times you’ll need to repeat is unknown.By checking the condition at the beginning of the loop, you can control whether the loop body is executed or not.

'''
num = int(input())
factorial = 1
while(num>0):
    factorial *= num 
    num-=1
print(factorial)
'''


# break:  It allows you to exit the loop prematurely, even before the termination condition is met. For example, if you’re searching for a value in a list, once you find it, you can break out of the loop instead of continuing to search through the remaining elements.
'''
userList = list(map(int,input("Enter the list items:").split()))
i = 0
while i < len(userList):
    if userList[i] >= 20:
        break
    print(i+1, "th value of the list is: ",userList[i])
    i+=1
'''       

#Continue: It skips the current iteration of the loop and moves to the next one. This can be useful when you want to skip certain elements or avoid executing some code under specific conditions.
    
userList = list(map(int,input("Enter the list items:").split()))
i = 0
while i < len(userList):
    if userList[i] == 20:
        i+=1
        continue
    print(i+1, "th value of the list is: ",userList[i])
    i+=1
