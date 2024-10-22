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
#     def bark(self):
#         return "Woof!"
# my_dog = Dog()
# print(my_dog.speak()) # Output: Animal speaks






#############################################################################################################
###################### https://www.w3resource.com/python-exercises/oop/index.php ############################