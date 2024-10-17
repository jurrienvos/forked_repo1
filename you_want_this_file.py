def greet():
    print("Hello, world!")
greet()


def add(a,b):
    return a+b
result=add(2,3)
print("result =",result)


age=2
if age<0:
    raise ValueError("no possible")


age = -1
try:
    if age < 0:
        raise ValueError("no possible")
except ValueError as e:
    print(f"An error occurred: {e}")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution not completed.")


class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)



fruits = ["apple", "banana", "cherry"] #dit is een lijst

tuples = ("apple", "banana", "cherry")







def multiply(a,b,c):
    return a*b+2*c
print(multiply(4,4,3))


list=[x*y for x in range(0,3) for y in range(0,3)]
print(list)

def bark(self):
    return "Woof!"
print(bark(self=10))

#line
