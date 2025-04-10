# python conditions and if statement
#  equal a==b
# not equal a!=b
# less than a<b
# less than or equal to a<=b
# greater than a>b
# greater than or equal a>=b
# a = 33
# b = 200
# if b > a:
#     print("b is greater than a")
#  the Elif keyword is python way of saying if the previous condition is not true than please try the new condition
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are same")
# else catches anything which isn't cought by any preceeding  condition
# a = 200
# b= 33 
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are same")
# else:
#     print("a is greater than b")
# you can also have an else without the elif
# if b > a:
#     print("b is greater than a")
# else:
#     print("now b is not greater than a")
# short handif
# if a > b: print("a is greater than b")
# short hand if....else
# a=200
# b=200
# print(" no,it is not greater")
# one line if else statement with 3 conditions 
# print("A") if a > b else print("=") if a == b else print("B")
# a= 200
# b=45
# c= 600
# if a>b and c>a:
#     print("Both the conditions are true")
# # or is also logical operator and it is used to combine logical statement
# if a>b or a>c:
#     print("al least one of the 2 condition is true") 
# # nested if statement  you can have if statement inside if statement  
# x=41
# if x>10:
#     print("it is above 10, ")
#     if x > 20:
#         print("and it is also above 20,")
#     else:
#         print("but it is not above")
# the pass statement - if with any reason if statement has no content than you pass the pass statement for avoiding error in program
# a = 33
# b= 200
# if b>a:
#     pass
# age=int(input("enter your age "))
# if age>18:
#     print("you can apple for licence ")
# print("Speed thrills but kills ")

# age=int(input("enter your age "))
# if age>18:
#     print("you can apple for licence ")
# else:
#     print("Speed thrills but kills")
handsome ='true'
good_salary ='false'
if handsome =='true' and good_salary=='false':
    print("you will marry with a super model")
elif handsome == 'true' and good_salary == 'false':
    print("you will marry with beatiful girl")
elif handsome =='true'and good_salary == 'false':
    print("you will marry with a girl")
else:    
    print("Bhagwan Bharose!!")
# print("you will marry with a beatiful girl")


