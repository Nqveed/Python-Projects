# Arrays are used to store miltiple values in one single variable
# In numpy,an array is fundamenent object.
# Arrays are used to store homogeneous data in cuntinuous block of memory. such as[1,2,3,3],[100,101,102]
# Arrays vs List
# all elements of an array are of same data type *List can have elements of different data type
# Elements of array are stored in continuous memory locations
# *List elements are not stored continuously in memory
# Arrays are  static and can not be resized once they are created 
# *List can be resized and modified easily
# Arrays support element wise operations
# *Lists do not support element wise operations
# Numpy array take up less space in memory
# More space in memory

cars = ["Ford","Valvo","Bmw"]
print(cars)
cars=["Ford","Valvo","Bmw"]
a=cars[1]
print(a)
cars=["Ford","Valvo","Bmw"] 
cars[0]="Toyota"
print(cars)
cars=["Ford","Valvo","Bmw"]
b= len(cars)
print(b)
cars=["Ford","Valvo","Bmw"]
for i in cars:
    print(i)    
#   adding Arrays elements  
cars=["Ford","Value","Bmw"] 
cars.append("Honda")
print(cars)
#  removing function pop 
cars=["Ford","Valvo","Bmw"]
cars.pop(1)
print(cars)
cars.append("Honda")
print(cars)
print(cars)
# cars.count()
# print(cars)
#  removing functions remove
# cars=["Ford","Value","Bmw"]
#  append()
# copy()
# count()
# extend()
# index()
# pop()
# remove()

    