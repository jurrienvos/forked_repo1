import pandas as pd
import matplotlib
import numpy as np


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


lijst=[x*y for x in range(0,3) for y in range(0,3)]
print(lijst)

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




#### 5. Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def bark(self):
        return "Woof!"
my_dog = Dog()
print('INHERITANCE',my_dog.speak()) # Output: Animal speaks





#################################### Day 17 Python Decorators ############################################

# #Example 1:  https://www.geeksforgeeks.org/function-wrappers-in-python/ - defining a decorator
# def hello_decorator(func):
#     def inner1(): # inner1 is a Wrapper function in which the argument is called. Also, inner function can access the outer local functions like in this case "func".
#         print("voor function execution")
#         func() #calling the actual function now, inside the wrapper function.
#         print("na function execution")
#     return inner1
# def function_to_be_used(): # defining a function, to be called inside wrapper
#     print("binnen de function!")
# function_to_be_used = hello_decorator(function_to_be_used) # passing 'function_to_be_used' inside the decorator to control its behavior
# function_to_be_used() # calling the function

#### Basic decorator
# def my_decorator(func):
#     def wrapper():
#         # func()
#         print("before function is called - basic decorator.")
#         func()
#         print("after function is called - basic decorator.")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello! - basic decorator")
# say_hello()



#### 2. Decorators with Arguments
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("before function is called - Decorators with Arguments.")
#         result = func(*args, **kwargs)
#         print("after function is called - Decorators with Arguments.")
#         return result
#     return wrapper
# @my_decorator
# def greet(name):
#     print(f"Hello, {name} ! - Decorators with Arguments")
# #greet("Alice")
# @my_decorator
# def say_goodbye(name):
#     print(f"Goodbye, {name}!")
# greet("Alice")
# say_goodbye("Alice")




#### 3. Using Built-in Decorators - Python has some built-in decorators, such as @staticmethod, @classmethod, and @property.
# class MyClass:
#     @classmethod
#     def classs_method(cls):
#         print("This is a class method.")
# MyClass.classs_method() # Output: This is a class method.
#


#### 4. Chaining Decorators - You can apply multiple decorators to a single function.
def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper
def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper
@decorator_one
@decorator_two
def say_hello():
    print("Hello!")
say_hello()






###################################################
############ Day 18: Python Generators ############
##van mij:
def count_up_to(n):
    count = 1
    while count <= n:
        count = count + 1
        return count
counter0 = count_up_to(4)
print(f'counter0={counter0}') #outputs counter0=2. Waarom geen lijst met [1, 2, 3, 4]?
#The reason your current code doesn't produce a list of numbers [1, 2, 3, 4]
#is because you are using return inside the loop, which immediately exits the function
#after the first iteration and returns the value 2. To generate a sequence of numbers,
#you need to use yield instead of return and allow the loop to continue until the count reaches the desired number.

#### 1. Creating a Generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count = count + 1
# counter = list(count_up_to(4))
counter = count_up_to(4)
print((counter))#output: <generator object count_up_to at 0x0000029D04386400>.
#Code outputs <generator object count_up_to at 0x0000021722326400> instead of a list with numbers is because
#the yield statement creates a generator object, and when you print the generator object directly, it doesn't automatically run through the values it generates.
#A generator is an iterable that generates values on the fly, which means the values are produced one by one when requested, instead of all at once like a list.
# To see the numbers generated by the count_up_to function, you can:
# 1. Iterate over the generator using a loop,
# 2. or Convert the generator into a list.
# 2=
# counter = count_up_to(4)
# print(list(counter))
# 1=
x=[]
for value in counter:
    x.append(value)
print(f'list with values={x}')
print(f'empty={list(counter)}') #outputs empty: as counter is a generator, it can only be iterated over once.
#After it is exhausted, subsequent attempts to iterate over it will yield an empty result.
#so if you try to print or use counter again after that, it won’t produce any values, because generators in Python don’t "reset" after iteration.

#### 2. Using Generators in a Loop
y=[]
for number in count_up_to(4):
    y.append(number)
print(f'list with values{y}')

#### 4. Generator Expressions
squares = (x**2 for x in range(5))
print(type(squares)) #outputs <class 'generator'>
x=[]
for num in squares:
    x.append(num)
print(f'{x} squares')




############ Day 19: Python Context Managers ############
# 2. Creating Your Own Context Manage
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self # You can return any object you want to use inside the context.
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")
with MyContextManager():
    print("Inside the context.")


from contextlib import contextmanager
@contextmanager
def my_context():
    print("Entering the context.")
    yield # This is where the code inside the 'with' block runs.
    print("Exiting the context.")
with my_context():
    print("Inside the context.")




############ Day 20: Python Testing ############
#### 2. Unit Testing
import unittest
def add(a, b):
    return a + b
def subtract(c,d):
    return c-d
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        message = "+ Test failed!"
        self.assertEqual(add(2, 3),5,message)
        self.assertEqual(add(-1, 1),0,message)
    def test_subtract(self):
        message = "- Test failed!"
        self.assertEqual(subtract(5,3),2,message)
        self.assertEqual(subtract(6, 3), 3, message)
if __name__ == '__main__':
#This line checks if the script is being run directly (as opposed to being imported as a module in another script).
#When you run a Python script, the special variable __name__ is automatically set to "__main__" if the script is the entry point of execution.
#If the script is imported into another file, __name__ will be set to the name of the module, and the block of code inside this if statement won’t run.
    unittest.main()

#It looks for methods that start with test_ and executes them.
#In general: Yes, you generally need those two lines when running the script directly to ensure the unit tests run.
#If you're running the tests in a test suite or using an external test runner like pytest or some IDE’s built-in test runner,
# you may not need these lines because those test runners handle test discovery and execution automatically...

def test_add():
 assert add(2, 3) == 5

###




###

