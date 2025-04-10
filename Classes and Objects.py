# # create a class and object
# Object are real world enttities. such as pen,watch, it has two parts data or properties such as pen'color, and method or function such as writing with pen is method
# Classes are group of these enttities.
# python is an object oriented
# class computer:
#     def config(self):
#         print("i5,16gb,1TB") 
# # # a='8'
# coml=computer()
# coml.config()
# computer.config(coml)
# print(type(coml))
class computer1:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is ", self.cpu,self.ram)
comp1 = computer1('i5',16)
comp2 = computer1('Ryzen3',6)
comp1.config()
comp2.config()
# class student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
# stud=student("Naveed",99)
# print(stud.name,stud.grade)
# stud.grade=100
# print(stud.grade)
# class student1:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def student_details(self):
#         print(f"{self.name} is in class with gp {self.grade} ")
# stud1=student1("Naveed",98)
# stud1.student_details()
# class student2:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
# stud2=student2("Naveed","A")
# print(stud2.__dict__)
# 

# class faculty:
#     def putdata(self):
#         self.id=int(input("Enter faculty id "))
#         self.name=input("Enter faculty name ")
#         self.salary =float(input("Enter faculty salary "))
#         self.address=(input("Enter faculty address "))
#     def display(self):
#         print("facultyid: ",self.id)
#         print("faculty name: ",self.name)
#         print("faculty salary: ",self.salary)
#         print("faculty address: ",self.address)
# a=faculty()
# a.putdata ()
# a.display()
# class animals:
#     def name(self):
#         print("Cornivoir:","lion",",","Bear")
#         print("Mamals: ","buffalo","Cow")
#         print("Birds: ","eagle","Falcan")
# ani=animals()
# ani.name()
# ani1=animals()
# ani1.name()
#
# class animals:
#     def name(self,lion,buffalo,eagle):
#         self.lion=lion
#         self.buffalo=buffalo
#         self.eagle=eagle
#     def data(self):
#         print("Lion:","lion")
#         print("Buffalo: ","buffalo")
#         print("Eagle: ","eagle")
# ani=animals()
# ani.name("lion","buffalo","eagle")
# ani.data ()
# class animals:
#     def __init__(self,a,b,c):
#         self.lion=a
#         self.buffalo=b
#         self.eagle=c
#     def data(self):
#         print("Lion:",self.lion)
#         print("Buffalo: ",self.buffalo)
#         print("Eagle: ",self.eagle)
# ani=animals("lion","buffalo","eagle")
# ani.data()
# class animals:
#     def __init__(self,a,b,c):
#         self.con=a
#         self.mam=b
#         self.bird=c
#     def data(self):
#         print("Corni:",self.con)
#         print("mam: ",self.mam)
#         print("Bird: ",self.bird)
# ani=animals("lion","buffalo","eagle")
# ani.data()
# class myclass:
#     x=5
# print(myclass)
# create object
# class myclass:
#     x=5
# pl = myclass()
# print(pl.x)
# Constructors: It is a special method within a class that gets automaticaly called when an object is created
# It is used to initialize the attributes of  the object
# It is written with _init __() 
# class faculty:
#     def __init__(self):
#         self.id=int(input("Enter faculty id "))
#         self.name=input("Enter faculty name ")
#         self.salary =float(input("Enter faculty salary "))
#         self.address=(input("Enter faculty address "))
#     def display(self):
#         print("facultyid: ",self.id)
#         print("faculty name: ",self.name)
#         print("faculty salary: ",self.salary)
#         print("faculty address: ",self.address)
# a=faculty()
# b=faculty()
# a.display()
# b.display()
# class faculty:
#     def __init__(self,a,b,c,d):
#         self.id=a
#         self.name=b
#         self.salary =c
#         self.address=d
#     def display(self):
#         print("facultyid: ",self.id)
#         print("faculty name: ",self.name)
#         print("faculty salary: ",self.salary)
#         print("faculty address: ",self.address)
# a=faculty(1,"Naveed",10000,"Lahore")
# a.display()
# class person:
 #     def __init__(self,name,age):
 #         self.name=name
 #         self.age=age  
 # pl = person ("Naveed",36)
 # print(pl.name)
 # print(pl.age)
# class student:
#     def __init__(self,my_roll,my_name,my_marks):
#         self.rollno=my_roll
#         self.name=my_name
#         self.marks=my_marks
#     def average(self):
#         return sum(self.marks)/len(self.marks)
# first_student=student(1,'Naveed',[50,60,70,80,90])
# print(first_student.rollno)
# print(first_student.name)
# print(first_student.average())
# # #  object method
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def my_function(self):
#         print("Hello everyone my name is "+self.name)
# pl = person("Naveed",36)
# pl.my_function()
#  The self parameter 
# class person:
#     def __init__(Naveedobject ,name,age):
#         Naveedobject.name=name
#         Naveedobject.age=age
#     def my_function(abc):
#         print("Hello everyone my name is "+abc.name)
# pl= person("Naveed",36)  
# pl.my_function()
# #How to modify object properties
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.name=age
#     def my_function(self):
#         print("Hello everyone my name is" + self)
# pl = person("Naveed",36)
# pl.age =30
# print(pl.age)
# # Delete Object properties
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def my_function(self):
#         print("Hello everyone my name is" + self.name)
# pl = person ("Naveed",36)
# del pl.age
# print(pl.name)
# # how to delete object
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def my_function(self):
#         print("Hello everyone my name is" + self.name)
# pl = person ("Naveed",36)
# del pl
# The pass statement
# class person:
#     pass





        


















