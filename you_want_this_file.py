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


name='henk'
print(f'hoi {name}')
print("hoi",name)

###################### OOP #############################
#2. Creating an Object
class Dog:
    def bark(self):
        return "Woof!"
my_dog = Dog()
print(my_dog.bark()) # Output: Woof!





# 3. Attributes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 5)
print(my_dog.name) # Output: Buddy
#4. Methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} who is {self.age} years old says Woof!"

my_dog = Dog("Buddy",3)
print(my_dog.bark()) # Output: Buddy says Woof!







#5. Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Woof!"
my_dog = Dog()
print('INHERITANCE',my_dog.speak()) # Output: Animal speaks


#################################### Day 17 Python Decorators ############################################
#Example 1:  https://www.geeksforgeeks.org/function-wrappers-in-python/
# defining a decorator
def hello_decorator(func):
    def inner1(): # inner1 is a Wrapper function in which the argument is called. Also, inner function can access the outer local functions like in this case "func".
        print("voor function execution")
        func() #calling the actual function now, inside the wrapper function.
        print("na function execution")
    return inner1
def function_to_be_used(): # defining a function, to be called inside wrapper
    print("binnen de function!")
function_to_be_used = hello_decorator(function_to_be_used) # passing 'function_to_be_used' inside the decorator to control its behavior
function_to_be_used() # calling the function

#### basic decorator
def my_decorator(func):
    def wrapper():
        print("before function is called - no arguments.")
        func()
        print("after function is called - no arguments.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello! - no arguments")
say_hello()

#### Decorators with Arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before function is called - arguments.")
        result = func(*args, **kwargs)
        print("after function is called - arguments.")
        return result
    return wrapper
@my_decorator
def greet(name):
    print(f"Hello, {name}! - arguments")
greet("Alice")

#### 3. Using Built-in Decorators


