# List in Python: The data type in list is an ordered sequence that is mutable and made up one or more elements.A list can have elements of different data types such as integer,float,string,tuple, or even another list.List is very useful to group together elements of mixed data types.Elements of a list are enclosd in square brackets are separated by a comma. List indices also start from 0.
# list1=[20,4.4,'Naveed']
# print(list1[0])
# print(list1[-1])
# print(list1[2-1])
# list1[1]='Faisabad'
# print(list1)
a= ["apple","banana","orange","apple"]
# b=["mango","grape","papaya"]
# print(a+b)
# slicing in list
# c= list(("apple","banana","orange","apple"))
# print(c[0])
# d= ["apple","banana","orange","apple","manago","cherry","guava"," wertermelon"]
# print(d[2:5])
# d=["apple","banana","orange","apple","manago","cherry","guava"," wertermelon"]
# print(d[-3])
# # leaving out the start  and end value
# print(d[:4])
# print(d[1:4])
# f=['Naveed','Varun','Ravander','Adnan','Ashraf','Amrit','Natin']
# print(f[2:4]) items start through stop-1
# print(f[:5]) # items start through rest of the array
# print(f[0:4:3])
# print(f[:]) # a copy of whole array 
# print(f[-1]) last item in the array
# print(f[-2:]) # last two items in array
# print(f[:-2])# everything except last items
# print(f[::-1]) #all items in the array reversed
# print(f[1::-1]) # first two items reversed
# print(f[:-3:-1]) # last two items reversed
# How to Check if the items exists in list using membership operator in  or  not in
if "apple" in a:
    print("yes,'apple' is in  the list")
elif "apple"  not in a:  
    print("no,'apple'  not is in  the list") 
# Repetition 
# h=["hello"]
# print(h*3)
# change the items value of list
# x[1] = "guava"   
# print(x)
# x[1:3] =["grapes","chiku"]
# print(x)
# x[1:2]="watermelon","Nuts"
# print(x)
# change of 2 values by replacing it with 1 value
# x[1:3]=["watermelon"]
# print(x)
# x.append("grape")
# print(x)
# x.insert (1,"cherry")
# print(x)
# x.extend(y)
# print(x)
# x.remove("banana")
# print(x)
# x.pop(1)
# print(x)
# x.pop() 
# print(x)
# del x[0]
# print(x)
# del x
# clear x
# z=["apple","banana","orange","apple"
# ,"mango","grape","papaya"]
# z.sort()
# print(z)
# s=[100,300,50,65,82,23,200,90,150,120]
# s.sort()
# print(s)
# z.sort(reverse=True)
# print(z)
# s.sort(reverse=True)
# print(s)
# def myfunc(n):
#     return abs(n-65)
# s=[100,300,50,65,82,23,200,90,150,120]  
# s.sort(key = myfunc)
# List comprehension
marks=[20,30,40,50,60]  
new_marks=[x+2 for x in marks]
print(new_marks)
cubes=[]
for x in range (10):
    if x % 2==0:
        cubes.append(x **3)
print("Using for loop:",cubes)
easy=[x ** 3 for x in range(10) if x %  2 == 0]
print("Using list comprehension:", easy)
# z.reverse()
# print(z)
# f=z.copy()
# print(f)
# a=list(z)
# print(a)
# x =z+s
# print(x)
# for i in s:
#     z.append(i)
#     print(z)
# z.extend(s)    
# print(z)










    
















 