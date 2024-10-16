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


#extra lines
#extra lines2
#JA
#addition
#DEZE COMMIT

