#######################################################
###################### OOP ############################

####1. What is a Class?
class Dog:
    def bark(self): #self is required for instance methods in Python. It allows the method to access the instance's attributes and other methods.
        return "Woof!"
#2. Creating an Object
my_dog = Dog()
print(my_dog.bark()) # Output: Woof!
#if you'd remove self > TypeError: Dog.bark() takes 0 positional arguments but 1 was given.
# Why? when you call my_dog.bark(), Python automatically passes the instance my_dog to the bark method as the first argument.
#But since you've removed self from the method definition, Python expects bark() to take no arguments, hence the error.

############### my code
def bark():
    return "Woof!"
print(f'code written by me {bark()}')

class horse:
    def legs(self):
        return "4 legs"
    def nose(self):
        return "wet nose"
    def tail(self):
        return "long tail"
my_horse=horse()
print(f'legs: {my_horse.legs()}')
print(f'nose: {my_horse.nose()}')
print(f'tail: {my_horse.tail()}')


####3. Attributes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
my_dog = Dog("Buddy", 5)
print(my_dog.name) # Output: Buddy

############### my code
class mens:
    def __init__(self, name, age):
        self.name = name
        self.age = age
my_mens = mens("Buddy", 5)
print(f'mens: {my_mens.name} is {my_mens.age}')


####4. Methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says Woof!"
my_dog = Dog("Buddy", 5)
print(my_dog.bark()) # Output: Buddy says Woof!

############### my code
class mens:
    def __init__(self, name, age, length):
        self.name = name
        self.age = age
        self.length=length
    def human_traits(self):
        return f"{self.name} is {self.age} yrs old and has length {self.length} cm"
my_mens = mens("Buddy",5,160)
print(my_mens.human_traits())



# #5. Inheritance
# class Animal:
#     def speak(self):
#         return "Animal speaks"
# class Dog(Animal):
# you can have parentheses () after the class name in the class definition.
# These parentheses are used to specify inheritance, meaning they define the parent class or classes that the new class inherits from.
#     def bark(self):
#         return "Woof!"
# my_dog = Dog()
# print(my_dog.speak()) # Output: Animal speaks






#############################################################################################################
###################### https://www.w3resource.com/python-exercises/oop/index.php ############################
#1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math
print(math.pi)


class circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
my_circle=circle(2)
print(f'area={my_circle.area()}')
print(f'perimeter={my_circle.perimeter()}')

#answer:
import math
class Circle:
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius
    # Calculate and return the area of the circle using the formula: π * r^2
    def calculate_circle_area(self):
        return math.pi * self.radius ** 2
    # Calculate and return the perimeter (circumference) of the circle using the formula: 2π * r
    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius
# Example usage
# Prompt the user to input the radius of the circle and convert it to a floating-point number
radius = float(input("Input the radius of the circle: "))
# Create a Circle object with the provided radius
circle = Circle(radius)
# Calculate the area of the circle using the calculate_circle_area method
area = circle.calculate_circle_area()
# Calculate the perimeter of the circle using the calculate_circle_perimeter method
perimeter = circle.calculate_circle_perimeter()
# Display the calculated area and perimeter of the circle
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)

