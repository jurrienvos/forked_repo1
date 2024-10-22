
x="awesome" #this variable is created outside the function: it is a global variable.
def myfunc():
    print(f'Python is {x}')
myfunc()



x="awesome" #this variable is created outside the function: it is a global variable.
def myfunc():
    x = "fantastic" #local variable
    print(f'Python is {x}')
myfunc()
print(f'Python is {x}')

###
