#Time Complexity
#To represent the time complexity, we generally use the Big O notation.
#How to calculate?
#we are going to follow while calculating the time complexity:
'''
We will always calculate the time complexity for the worst-case scenario.
We will avoid including the constant terms.
We will also avoid the lower values.
Note: A point to remember is that we can actually ignore the constant coefficients as well
'''
#Why worst case?
'''
As we always want that our system serves the maximum number of clients, we need to calculate the time complexity for the worst-case scenario. With this, we can actually judge the robustness of any code or any system.
'''
#We will avoid including the constant terms.why?
'''
Let’s understand this rule considering the time complexity: O(4N3 + 3N2 + 8). Now, if we consider the value of N as 105 the time complexity will be like this:  O(4*1015 + 3*1010 + 8). In this case, the constant term 8 is very less significant in terms of changing the time complexity with different values of N. That is why we should avoid the constant terms while calculating the time complexity.
'''