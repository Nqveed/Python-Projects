#  What is scope?- scope of a variable is the block of code in entire program where  the variable is declared ,used , and can be modified. a variable is only available from inside the region in which it is created and this is called scope
# Lifetime of a variable is the throughout time variable exists in memory.
# variable get automatically destroyed once we return from function.
glob="Hi I am GLOBALLY available"
def f1():
    local="Hi I am LOCALLy availabe"
    print(local)
    print(glob)
f1()
print(glob)
# print(local)
# def my_function():
#     x= 300
#     print(x)
# my_function()
# def my_function():
#     x=300 
#     def myinnerfuncion():
#        print(x)
#     myinnerfuncion()
# my_function()
# What is Global scope
# x=300 
# def my_function():
#     print(x)
# my_function()
# naming variable - python will treat the 2 variable as a seperate variables
x= 300
def my_function():
    x= 3000
    print(x)
my_function()
#  Global keyword - if you need to create a global variable locally than you should use global keyward.
x= 30000
def my_function():
    global x
    x=500
my_function()
print(x)
#  you can also use the global keyword if you want to make a change to a global variable inside the function,
x= 900
def my_function():
    global x
    x= 600
my_function()
print(x)




 
