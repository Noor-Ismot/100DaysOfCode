#if else conditions : When there is one condition to check

print("Enter your age: ", end='')
age = int(input())
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")


#elif conditions : when there is more than one condition to check

print("Enter your age: ", end='')
age = int(input())
if age >= 18:
    print("You are an adult")
elif age >=12:
    print("You are a teenager")
else:
    print("You are a child")


# match case : when there is multiple pattern to match with a single value.a feature introduced in Python 3.10 as part of structural pattern matching. It's particularly useful when dealing with complex data structures or when you have multiple possible patterns to match against.

userInput = input("Which language are you learning? ")
match userInput:
    case 'Python':
        print("You can become a Data Scientist")
    case 'Java':
         print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
