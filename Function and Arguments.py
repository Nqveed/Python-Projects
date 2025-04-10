# creating and calling a function
def my_function():
    print("hello ,this is Naveed")
my_function()
# Definition of arugments-arugment are specified after the function name and inside the parentheses
# def my_function(fname ):
#     print(fname + " Ashraf")
# my_function("Naveed")
# my_function("Adnan")
# my_function("Arsalan")
# # number of arguments-args-2
# def my_function(fname,lname):
#     print(fname+" "+lname)
# my_function("Naveed","Ashraf") 
# arbitrary arguments,args
def my_function(*kids):
    print("The youngest child is "  +  kids[0])
my_function("chintu", "mintu", "pinku")
# # keyword arguments key= values
# def my_function(child1,child2,child3):
#     print("The youngest child is "  + child3)
# my_function(child1="chintu", child2="mintu",child3 = "pinku")
# Arbitrary keyword argumemts **kwardgs
# def my_function(**kids):
#     print("His last name is " +kids["lname"])
# my_function(fname= "Naveed",lname="Ashraf")
# # Default parameter Value
# def my_function(country ="Pakistan"):
#     print("I am from " + country)
# my_function("India")
# my_function("Australia")
# my_function("UK")
# # my_function()
# passing a list as an argument
# def my_function(food):
#     for i in food:
#         print(i)
# fruits =["apple","banana","cherry"]
# my_function(fruits)
# use  return statement
# def my_function(x):
#     return 5*x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# #  the pass statement
# def my_function():
#     pass
# Lambda function syntex lambda argument : expression
# x = lambda a:a+10
# print(x(5))
# lambda function can even take multiple arguments and return result:
# x = lambda a, b:a*b
# print(x(6,5))
# y= lambda a,b,c:a+b+c
# print(y(6,7,8))
# numbers=[11,20,31,40,51,60,71,80,91,100]
# def even(x):
#     return x%2==0
# evens=list(filter(even,numbers))
# print("Even numbers:",evens)
# numbers=[11,20,31,40,51,60,71,80,91,100]
# evens1=list(filter(lambda x: x%2==0,numbers))
# print("Even numbers:",evens1)
# city=['Faisalabad','Lahore','Jaipur','Kota','Chandigarh','Delhi','Muzaffarpur']
# def length (city):
#     return len(city)
# sort= sorted(city,key=length)
# print("sorted words by length:",sort)
# city=['Faisalabad','Lahore','Jaipur','Kota','Chandigarh','Delhi','Muzaffarpur']
# sort1=sorted(city,key=lambda i : len(i),reverse=True)
# print("sorted words by length:",sort1)
# # why we use lambda function
# def y_function(n):
#     return lambda a: a*n
# my_double =my_function(3)
# print(my_double(11))
# new function for double and triple
# def my_function(n):
#     return lambda a:a*n
# my_double=my_function(2)
# my_triple=my_function(3)
# print(my_double(11))
# print(my_triple(11))
# marks=[77,97,64,85,55]
# def grade(marks):
#     if marks>=90:
#         return 'A'
#     elif 80 <=marks <90:
#         return 'B'
#     elif 70 <= marks < 80:
#         return 'C'
#     elif 60 <= marks <70:
#         return 'D'
#     elif 45 <= marks < 60:
#         return 'E'
#     else:
#         return 'F'
# grades = list( map(grade,marks))
# print("Exam Scores",marks)
# print("Grades:",(grades))
# marks=[77,97,64,50,55,45]
# def failing(score):
#     return score < 60
# result= filter (failing,marks)
# print("Failing Scores:" ,list (result))
# # Decorator is a function that takes another function as argumemt and return function.
# def decorator(func):
#     def wrapper():
#         print('Transaction initiated')
#         func()
#         print('Transaction Completed')
#     return wrapper
# @decorator
# def hello():
#     print('....Executing all steps of Transaction...')
# # hello1=decorator(hello)
# # hello1()
# hello()
def my_function(*workers):
    print("worker name is " + workers[0])
my_function("A","B","C")
def my_func(*Books):
    print("The book name  is " + Books[1])
my_func("Eng","Urdu","Physics","Math","Islamic study")
def my_func(Book , marks):
    print(Book, marks)
my_func("Eng",87)























