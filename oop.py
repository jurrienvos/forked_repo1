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
        return age
        # return f'{self.name} born in {self.country} has the age of {self.age}.'
#let op: statements als self.name gebruik je binnen de def, niet erbuiten.
#erbuiten gebruik je de instance en access je de attribute zoals hieronder.
my_person = person("Henk","NL",date(1990,12,1))
print(f'{my_person.name} born in {my_person.country} has dob {my_person.dob} and the age of {my_person.determine_age()}')
# ! when referencing the method without parentheses like doing my_person.determine_age,
# you are not actually calling the method to compute the age. Instead, you're simply referencing the method itself.
# my_person is an instance of the Person class.
# When you access my_person.name, you're accessing the 'name' attribute of that specific instance.