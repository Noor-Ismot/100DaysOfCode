#Space Complexity
'''
The term space complexity generally refers to the memory space that a code uses while being executed. Again space complexity is also dependent on the machine and so we are going to represent the space complexity using the Big O notation instead of using the standard units of memory like MB, GB, etc.
i.e
input(a) -> 1 input space
input(b)-> 1 input space
c = a+b -> 1 input space

So, space complexity O(3)
Similarly, if we use an array of size n, the space complexity will be O(N).

'''

#"Pass by value" and "pass by reference" are two different mechanisms used to pass arguments to functions in programming languages. They affect how changes made to the parameters inside the function affect the original variables passed as arguments.
'''
Key Differences:
Effect on Original Variables:

Pass by value does not affect the original variables passed as arguments.
Pass by reference allows changes made to parameters inside the function to affect the original variables.
Supporting Languages:

Pass by value is common in languages like C, Java, and Python (for immutable types).
Pass by reference is supported in languages like C++ (with references), Python (for mutable types like lists), and others.
Efficiency:

Pass by value might involve copying large data structures, which could be inefficient.
Pass by reference is more efficient for large data structures since it avoids unnecessary copying.

'''

'''
i.e
#Pass by Value

def func(x):
    x = x + 1

num = 5
func(num)
print(num)  # Output will be 5, as num remains unchanged.

#Pass by Reference

def func(lst):
    lst[0] = lst[0] + 1

my_list = [5]
func(my_list)
print(my_list)  # Output will be [6], as the value of my_list has been modified inside the function.
'''