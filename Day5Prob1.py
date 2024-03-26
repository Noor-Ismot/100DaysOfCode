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
