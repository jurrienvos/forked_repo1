#################################################################################################
# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php


# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

#my attempt:

# for item in my_list:
#     if item % 7 == 0:
#         return item
#     else:
#         return None
# Wrong:
# Early termination: The function will always return after checking only the first item in the list, regardless of whether
# it's divisible by 7 or not.
# Incorrect logic: If the first item is not divisible by 7, the function immediately returns None without checking the rest of the list.
# Scope: As mentioned earlier, this code assumes it's within a function, but if it's not, the return statements would cause a SyntaxError.
# Here's an explanation of what this code does:
# It checks only the first item in my_list.
# If the first item is divisible by 7, it returns that item.
# If the first item is not divisible by 7, it immediately returns None.
# It never checks any items beyond the first one.

def createlist(r1,r2):
    return [item for item in range(r1,r2+1)] # Using List comprehension. From https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/
my_list=createlist(1500,2700)
# print(my_list[0],my_list[-1],len(my_list),my_list) #use -1 to check last number
def findnumbers(a):
    x=[]
    for item in a:
        if item % 7 == 0:
            x.append(item)
    return x
            # return item
        # else:
        #     return None
   #return None ##if you remove the else statement, you can use 'return None' at this location. It is outside the loop, only executed if no item is found
result=findnumbers(my_list)
print(f'result={result}')
# print(result)

#similarly, now for % 5:
def findnumbers2(a):
    x=[]
    for item in a:
        if item % 5 == 0:
            x.append(item)
        else:
            x.append(None)
    return x
result2=findnumbers2(my_list)
print(f'result2={result2}')

together=[y for y in result+result2 if y is not None]
print(f'together={together}')

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)

##answer:

# Create an empty list to store numbers that meet the given conditions
nl = []
# Iterate through numbers from 1500 to 2700 (inclusive)
for x in range(1500, 2701):
    # Check if the number is divisible by 7 and 5 without any remainder
    if (x % 7 == 0) and (x % 5 == 0):
        # If the conditions are met, convert the number to a string and append it to the list
        nl.append(str(x))
# Join the numbers in the list with a comma and print the result
print(','.join(nl))
print(f'length of nl={len(nl)}')

#attempt 2 as I interpreted the Q wrongly: should be both divisible by 7 AND 5:
def divisables(a):
    x=[]
    for item in a:
        if (item % 7 == 0) and (item % 5 == 0):
            x.append(item)
        return x
print(f'divisables={divisables(my_list)}')
# issue with above: The code prints an empty list because the return statement is
# incorrectly indented. As it is currently structured, the return statement is inside the loop,
# which means the function returns after checking just the first item in the list.
# If that item is not divisible by both 7 and 5, the function will return an empty list immediately.
#So:
def divisables(a):
    x=[]
    for item in a:
        if (item % 7 == 0) and (item % 5 == 0):
            x.append(item)
    return x
print(f'divisables={divisables(my_list)}')
print(f'length of divisables={len(divisables(my_list))}')
#In this corrected version, the return statement is executed only after the loop has checked all items in the list.
#Now, it will correctly return the list of items that are divisible by both 7 and 5.







##2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output : #60°C is 140 in Fahrenheit, #45°F is 7 in Celsius

#below strongly based on answer which I already saw:

# temp=input("select temp: e.g. 45F, 60C: ")
# value = int(temp[:-1])
# celc_or_fahr=temp[-1]
# print(f'celc_or_fahr= {celc_or_fahr}, type= {type(celc_or_fahr)}')
# answer=[]
# if celc_or_fahr == "f":
#     c = 5*(value-32/9)
#     answer.append(c)
# elif celc_or_fahr == "c":
#     f=value/5+32/9
#     answer.append(f)
# else:
#     return "wrong input"
#The issue with the return statement in your code is that it's used outside of a function.
# The return statement is meant to be used inside a function to return a value.
# Since your code does not define a function, you should use print() instead to display the error message.
#So:
# temp=input("select temp: e.g. 45F, 60C: ")
# value = int(temp[:-1])
# celc_or_fahr=temp[-1]
# print(f'celc_or_fahr= {celc_or_fahr}, type= {type(celc_or_fahr)}')
# answer=[]
# if celc_or_fahr == "f":
#     c = (5/9) * (value - 32)
#     answer.append(c)
# elif celc_or_fahr == "c":
#     f=(value/(5/9))+32
#     answer.append(f)
# else:
#     print("wrong input")
# print(f'answer= {answer}')

# #answer:
#
# # Prompt the user to input a temperature in the format (e.g., 45F, 102C, etc.)
# temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# # Extract the numerical part of the temperature and convert it to an integer
# degree = int(temp[:-1])
# # Extract the convention part of the temperature input (either 'C' or 'F')
# i_convention = temp[-1]
# # Check if the input convention is in uppercase 'C' (Celsius)
# if i_convention.upper() == "C":
#     # Convert the Celsius temperature to Fahrenheit
#     result = int(round((9 * degree) / 5 + 32))
#     o_convention = "Fahrenheit"  # Set the output convention as Fahrenheit
# # Check if the input convention is in uppercase 'F' (Fahrenheit)
# elif i_convention.upper() == "F":
#     # Convert the Fahrenheit temperature to Celsius
#     result = int(round((degree - 32) * 5 / 9))
#     o_convention = "Celsius"  # Set the output convention as Celsius
# else:
#     # If the input convention is neither 'C' nor 'F', print an error message and exit the program
#     print("Input proper convention.")
#     quit()
# # Display the converted temperature in the specified output convention
# print("The temperature in", o_convention, "is", result, "degrees.")







# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
# on successful guess, user will get a "Well guessed!" message, and the program will exit.

#attempt 1:

# guess = (input("insert a guess : "))
# import random
# n=random.randint(1,9)
# print(n)
# if int(guess) == int(n):
#     print("Well guessed!")
# elif int(guess) != int(n):
#use a while loop!

# attempt 2, after quickly seeing answer:
# guess = (input("insert a guess : "))
import random
target_num, guess = random.randint(1, 4), 0
print(target_num,guess)
while target_num != guess:
    guess = int(input("insert a guess : "))
print("Well guessed!")




