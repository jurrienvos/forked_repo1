#######################################################
###################### OOP ############################

####1. What is a Class?
class Dog:
    def bark(self): #self is required for instance methods in Python. It allows the method to access the instance's attributes and other methods.
        return "Woof!"
####2. Creating an Object
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
#############################################################################################################
###################### https://www.w3resource.com/python-exercises/oop/index.php ############################
#1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter

#2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
# dob=float(input("dob is: "))

#1st attempt:

class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def age(self):
        return f'the person named {self.name} born in {self.country} has the age of {self.dob}.'
my_person = person("Buddy","NL",2024-1990)
print(my_person.age())
#print(my_person().age()) is wrong cause this statement attempts to
# call my_person as if it's a function (using the ())
# but my_person is an instance of the person class,
# not a callable function. So: call the age() method directly on the my_person instance.


#answer:

from datetime import date
#remember: date is not a method. It is a class from the datetime module.
#from datetime import date: you are importing the date class from the datetime module,
# allowing you to create instances of date and access its methods and attributes for handling date-related functionality.
mydate=date(2014,10,10)
print(mydate)
currentdate=date.today() #currentdate is the instance of the class date, and today() is a method.
print(currentdate)
print(currentdate.year)
# here, year is an attribute of the class date. Attributes in Python are typically accessed
# without parentheses, unlike methods, which require parentheses () to be called.

class Person:
    # Initialize the Person object with a name, country, and date of birth
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age = age - 1
        return age
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", date(1990, 7, 12))
print(f'Person 1: Name: {person1.name}, Country: {person1.country}, Date of Birth: {person1.date_of_birth}, Age: {person1.calculate_age()}')

#another try, after reading answer:

# dob=date(1990,12,1)
# print(dob)
# dob_year=dob.year
# print(dob_year)
# currentdate=date.today()
# print(currentdate)
# currentdate_year=currentdate.year
class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def determine_age(self):
        currentdate = date.today()
        age=currentdate.year - self.dob.year
        # if currentdate.month < self.dob.month: dit is goed maar je moet ook de dag meenemen
        if currentdate < date(currentdate.year, self.dob.month,self.dob.day):
            # return age - 1
            age = age - 1
        else:
            age = age
        return age

        # return f'{self.name} born in {self.country} has the age of {self.age}.'
#let op: statements als self.name gebruik je binnen de def, niet erbuiten.
#erbuiten gebruik je de instance en access je de attribute zoals hieronder.
my_person = person("jur","NL",date(1993,12,27))
print(f'{my_person.name} born in {my_person.country} has dob {my_person.dob} and the age of {my_person.determine_age()}')
# ! when referencing the method without parentheses like doing my_person.determine_age,
# you are not actually calling the method to compute the age. Instead, you're simply referencing the method itself.
# my_person is an instance of the Person class.
# When you access my_person.name, you're accessing the 'name' attribute of that specific instance.


# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

#my attempt:

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def substraction(self):
        if self.a < self.b:
            # print(f'only allow positive numbers') #with this line, I was still getting a 5th output: substraction None
            return "only allow positive numbers"
        else:
            return self.a-self.b
    def multipy(self):
        return self.a * self.b
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "no division by 0 is allowed"
myfunc=calculator(1,0)
print(f'addition: {myfunc.addition()}')
print(f'substraction: {myfunc.substraction()}')
print(f'multiply: {myfunc.multipy()}')
print(f'division: {myfunc.division()}')

#after reading answer, and now converting my code above to a version without def__init__:

class calculator:
    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b
    def addition(self,a,b):
        return a+b
    def substraction(self,a,b):
        if a < b:
            # print(f'only allow positive numbers') #with this line, I was still getting a 5th output: substraction None
            return "only allow positive numbers"
        else:
            return a-b
    def multipy(self,a,b):
        return a * b
    def division(self,a,b):
        if b != 0:
            return a / b
        else:
            return "no division by 0 is allowed"
myfunc=calculator()
print(f'addition: {myfunc.addition(1,0)}')
print(f'substraction: {myfunc.substraction(1,0)}')
print(f'multiply: {myfunc.multipy(1,0)}')
print(f'division: {myfunc.division(1,0)}')
# in principe kun je nu dus 4 verschillende waarden gebruiken itt attempt 1 omdat je nu niet de attributes hebt ge-initialized met def__init__

#answer:

# Define a class called Calculator to perform basic arithmetic operations
class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")
# Example usage
# Create an instance of the Calculator class
calculator = Calculator()
result = calculator.add(7, 5)
print("7 + 5 =", result)
result = calculator.subtract(34, 21)
print("34 - 21 =", result)
result = calculator.multiply(54, 2)
print("54 * 2 =", result)
result = calculator.divide(144, 2)
print("144 / 2 =", result)
result = calculator.divide(45, 0)
print("45 / 0 =", result)

# ! in deze exercise een duidelijk verschil tussen gebruik van def__init__ en niet gebruik ervan.








# 4. Write a Python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

#my attempt

from sympy import pi
#circle area=pi*r^2, perimeter=2*pi*r
#triangle area=0.5*base*height, perimeter=a+b+c
#square area=l*l, perimeter=4*l
class shape:
    class circle:
        def area(self,r):
            return pi*r**2
        def perimeter(self,r):
            return 2*pi*r
    class triangle:
        def area(self,base,height):
            return 0.5*base*height
        def perimeter(self,a,b,c):
            return a+b+c
    class square:
        def area(self,l):
            return l**2
        def perimeter(self,l):
            return l*4
mycircle=shape().circle()
mytriangle=shape().triangle()
mysquare=shape().square()
print(f'area circle={mycircle.area(2)},perimeter circle={mycircle.perimeter(2)}')
print(f'area triangle={mytriangle.area(2,3)},perimeter triangle={mytriangle.perimeter(2,3,4)}')
print(f'area square={mysquare.area(2)},perimeter square={mysquare.perimeter(2)}')

#answer:

# import math
# # Define a base class called Shape to represent a generic shape with methods for calculating area and perimeter
# class Shape:
# # Shape is the base class (or parent class) that defines general methods (calculate_area and calculate_perimeter)
# # which are meant to be overridden by its derived classes (or child classes).
# # In this case, the base class doesn't provide actual implementations, but instead, it acts as a blueprint for the specific shapes (Circle, Rectangle, Triangle).
#     # Placeholder method for calculating area (to be implemented in derived classes)
#     def calculate_area(self):
#         pass
#     # Placeholder method for calculating perimeter (to be implemented in derived classes)
#     def calculate_perimeter(self):
#         pass
# # Define a derived class called Circle, which inherits from the Shape class
# class Circle(Shape):
# # Circle, Rectangle, and Triangle are derived classes that inherit from the Shape class.
#     # Initialize the Circle object with a given radius
#     def __init__(self, radius):
#         self.radius = radius
#     # Calculate and return the area of the circle using the formula: π * r^2
#     def calculate_area(self):
#         return math.pi * self.radius**2
#     # Calculate and return the perimeter of the circle using the formula: 2π * r
#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius
# class Rectangle(Shape):
#     # Initialize the Rectangle object with given length and width
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     # Calculate and return the area of the rectangle using the formula: length * width
#     def calculate_area(self):
#         return self.length * self.width
#     # Calculate and return the perimeter of the rectangle using the formula: 2 * (length + width)
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)
# class Triangle(Shape):
#     # Initialize the Triangle object with a base, height, and three side lengths
#     def __init__(self, base, height, side1, side2, side3):
#         self.base = base
#         self.height = height
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#     # Calculate and return the area of the triangle using the formula: 0.5 * base * height
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
#     # Calculate and return the perimeter of the triangle by adding the lengths of its three sides
#     def calculate_perimeter(self):
#         return self.side1 + self.side2 + self.side3
# # Purpose of Inheritance:
# # Code Reusability: You define general methods in the base class (Shape) and reuse these in all the derived classes
# # (Circle, Rectangle, Triangle). This prevents code duplication.
# # Polymorphism: You can write code that works with the Shape base class and its methods (calculate_area and calculate_perimeter),
# # and this same code will work for any shape (circle, rectangle, triangle), because each shape implements these methods in its own way.
# r = 7
# circle = Circle(r)
# circle_area = circle.calculate_area()
# circle_perimeter = circle.calculate_perimeter()
# # Print the results for the Circle
# print("Radius of the circle:", r)
# print("Circle Area:", circle_area)
# print("Circle Perimeter:", circle_perimeter)
# # Create a Rectangle object with given length and width and calculate its area and perimeter
# l = 5
# w = 7
# rectangle = Rectangle(l, w)
# rectangle_area = rectangle.calculate_area()
# rectangle_perimeter = rectangle.calculate_perimeter()
# # Print the results for the Rectangle
# print("\nRectangle: Length =", l, " Width =", w)
# print("Rectangle Area:", rectangle_area)
# print("Rectangle Perimeter:", rectangle_perimeter)
# # Create a Triangle object with a base, height, and three side lengths, and calculate its area and perimeter
# base = 5
# height = 4
# s1 = 4
# s2 = 3
# s3 = 5
# # Print the results for the Triangle
# print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
# triangle = Triangle(base, height, s1, s2, s3)
# triangle_area = triangle.calculate_area()
# triangle_perimeter = triangle.calculate_perimeter()
# print("Triangle Area:", triangle_area)
# print("Triangle Perimeter:", triangle_perimeter)

#answer, with added piece from gtp:

import math
class Shape:
# Shape is the base class (or parent class) that defines general methods (calculate_area and calculate_perimeter)
# which are meant to be overridden by its derived classes (or child classes).
# In this case, the base class doesn't provide actual implementations, but instead, it acts as a blueprint for the specific shapes (Circle, Rectangle, Triangle).
    # Placeholder method for calculating area (to be implemented in derived classes)
    def calculate_area(self):
        pass
    # Placeholder method for calculating perimeter (to be implemented in derived classes)
    def calculate_perimeter(self):
        pass
# Define a derived class called Circle, which inherits from the Shape class
class Circle(Shape):
# Circle, Rectangle, and Triangle are derived classes that inherit from the Shape class.
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius
    # Calculate and return the area of the circle using the formula: π * r^2
    def calculate_area(self):
        return math.pi * self.radius**2
    # Calculate and return the perimeter of the circle using the formula: 2π * r
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    # Initialize the Rectangle object with given length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # Calculate and return the area of the rectangle using the formula: length * width
    def calculate_area(self):
        return self.length * self.width
    # Calculate and return the perimeter of the rectangle using the formula: 2 * (length + width)
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
class Triangle(Shape):
    # Initialize the Triangle object with a base, height, and three side lengths
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    # Calculate and return the area of the triangle using the formula: 0.5 * base * height
    def calculate_area(self):
        return 0.5 * self.base * self.height
    # Calculate and return the perimeter of the triangle by adding the lengths of its three sides
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
def print_area(area: Shape, perimeter: Shape):
    print(f'The area is: {area.calculate_area()} and the perimeter is: {perimeter.calculate_perimeter()}')
circle_area = Circle(5)
circle_perimeter = Circle(7)
rectangle_area = Rectangle(4, 6)
rectangle_perimeter = Rectangle(4, 6)
triangle_area = Triangle(30, 4, 3, 4, 5)
triangle_perimeter = Triangle(6, 4, 80, 40, 50)
print_area(circle_area,circle_perimeter)       # Works with Circle
print_area(rectangle_area,rectangle_perimeter)    # Works with Rectangle
print_area(triangle_area,triangle_perimeter)     # Works with Triangle


