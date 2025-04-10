# Inheritance
# allows one class(child) to resue the properties and methods of another class (parent).
#    #   creating a parent class
# class OOTSubscription:
#     def __init__(self,subcription_id,plan,total_payment):
#         self.id=subcription_id
#         self.plan=plan
#         self.payment=total_payment
#     def subscribe(self):
#         print(f"subcriber with {self.id}id unsubcribed to the {self.plan}plan")
#     def unsubscribe(self):
#         print(f"subcriber with {self.id}id unsubcribed to the {self.plan}plan")
# class premiunsubcription(OOTSubscription):
#     def __init__(self,subcription_id,plan,total_payment,screens):
#         super().__init__(subcription_id,plan,total_payment)
#         self.max_screens=screens
#     def set_max_screens(self,screens):
#         print(f" maximum screen to {self.set_max_screens} in premium plan")
# Netflex=premiunsubcription("123456","mouthly",1,1200)
# Netflex.subscribe()
# Netflex.set_max_screens(4)
      
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# x= person ("Naveed","Ashraf")
# x.printname()
# # #  creating child class
# class student(person):
#     pass
# #  testing the student class
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname =lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class student(person):
#     pass
# x= student("Naveed","Ashraf")  
# x.printname()
# # adding __init__() function
class person:

    def __init__(self,fname,lname): 
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self, fname, lname)
x= student("Naveed","Ashraf")
x.printname()
# # using  the super() function
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname( self):
#         print(self.firstname,self.lastname)
# class student(person):
#     def __init__(self,fname,lname):
#         super().__init__(fname, lname)
    
                
# x = student("Naveed","Ashraf")
# x.printname()

# how  to add the properties
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname( self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationyear= 2022
x=student("Naveed","Ashraf")
x.printname()
print(x.graduationyear)
# #   you can pass the object properties in student directly
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=lname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class student (person):
#     def __init__(self,fname,lname):
#         super().__init__(fname, lname)
#         self.graduationyear=2022
# x= student ("Naveed","Ashraf")
# x.printname()
# print(x.graduationyear)






    