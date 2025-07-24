# #Part_2 of OOP in Python
# #DEL for deleting a attribute or method

# class Student:
#       def __init__(self,name,age):
#             self.name = name
#             self.age=age
#       def print_det(self):
#             print(f'Your name is {self.name} and age is {self.age}')
# s1=Student('Ramya',19)
# print(s1.name)
# # del s1.name
# s1.print_det()
# del s1.print_det

# s1.print_det()

# #OP:
# # Ramya
# # Your name is Ramya and age is 19
# # Traceback (most recent call last):
# #   File "C:\Users\ragha\OneDrive\Desktop\VS_any_code\Python_ML\OOP_2.py", line 14, in <module>
# #     del s1.print_det
# # AttributeError: print_det

# #--------------------------------------------------

# #Public and Private keys in OOP
# #Public Key-Accessed through out the program. The attributes or the keys that we used previously were Public Key
# # Private key-Accessed only that particular class or methods

# #Syntax starts with self.__VariableName etc..

# class Account:
#       def __init__(self,acc_no,acc_pass):
#             self.acc_no=acc_no
#             self.__acc_pass=acc_pass
#       def print_det(self):
#             print(f'Your password fopr acc number {self.acc_no} is {self.__acc_pass}')

# u1=Account(2468,'yashu@123')
# print(u1.acc_no)
# # print(u1.__acc_pass)
# #but we can use that private key in a methood of that class

# u1.print_det()


# #Exapmle 2
# class student:
#       __age=24

#       def __hello(self):
#             print('Hello this a private method')

#       def wellcome(self):
#             self.__hello()

# s1=student()
# # print(s1.age)
# #OP:
# # Traceback (most recent call last):
# #   File "C:\Users\ragha\OneDrive\Desktop\VS_any_code\Python_ML\OOP_2.py", line 60, in <module>
# #     print(s1.age)
# # AttributeError: 'student' object has no attribute 'age'
# #s1.hello()
# #OP:
# # Traceback (most recent call last):
# #   File "C:\Users\ragha\OneDrive\Desktop\VS_any_code\Python_ML\OOP_2.py", line 66, in <module>
# #     s1.hello()
# # AttributeError: 'student' object has no attribute 'hello'

# #But we can acces a privet method inside another method of same class
# s1.wellcome()
# #OP:
# # Hello this a private method

# #-----------------------------------

# #3.InHeritance
# #Here we will inherit the car properties in bmw
# class car:
#       @staticmethod
#       def start():
#             print('Car started')
#       @staticmethod
#       def stop():
#             print('car stoped....')

# class bmw(car):
#       def __init__(self,type):
#             self.type=type
#       def car_type(self):
#             print(f'Your car is of {self.type} type')

# user=bmw('disel')
# user.car_type()
# user.start()
# user.stop()

# #OP:
# # Your car is of disel type
# # Car started
# # car stoped....

##-----------------------------------------------------

# #We can use two class propertis in one 

# class a:
#       chara=print('This is class a')
# class b:
#       charb=print('This is class b')
# class c(a,b):
#       charc=print('This is class c')

#       #lets create a object for class c and check the inheritence\
# var=c()
# var.chara
# var.charb
# var.charc
      
# #OP:
# # This is class a
# # This is class b
# # This is class c

##------------------------------------------------

# #Super method

# class car:
#       def __init__(self,type):
#             self.type = type 
#       @staticmethod
#       def start():
#             print('Started')
#       @staticmethod
#       def stop():
#             print('Car stoped')
# class bmw(car):
#       def __init__(self,name,type):
#             self.name=name
#             super().__init__(type) #this refers to parent class
#             print(f'the name of the car is {self.name}')
#             super().start()
# user=bmw('cupris','disel')
# print(user.type)
# #OP:
# # the name of the car is cupris
# # Started
# # disel

##------------------------------------

# #class method

# # it is used to alter the properties or attributes of the class
# #Without using class method
# class student:
#       name='yashwanth'
#       def change_name(self,name):
#             student.name=name
#             return student.name
      
# s1=student()
# print(s1.change_name('pavan'))
# print(student.name)
# #OP:
# # pavan
# # pavan

##------------------------------------------------------------

# #Using class method

# class student:
#       name='yashwanth'
#       @classmethod
#       def change_name(cls,name):
#             cls.name=name
#             return cls.name

# s2=student()
# print(s2.change_name('Lalith'))
# print(student.name)
# #OP:
# # Lalith
# # Lalith

##---------------------------------------------------------

# # different methods in OOP
# # 1.Static method () //Decorator:@staticmethod
# # 2.class method (cls) //Decorator:@classmethod
# # instence method (self) //No decorator needed

##---------------------------------------------------------

# #Another decorator @property

# class Student:
#       def __init__(self,phy,chem,bio):
#             self.phy=phy
#             self.chem=chem
#             self.bio=bio
#             self.percentage=str((self.phy+self.chem+self.bio)/3)+'%'

# s1=Student(40,34,39)
# print(s1.percentage)
# #if now i want to change the phy marks it will be changed but not the percentage
# s1.phy=89
# print(s1.phy)
# print(s1.percentage)
# #OP:
# # 37.666666666666664%
# # 89
# # 37.666666666666664%

# #So we can use @property

# class Student:
#       def __init__(self,phy,chem,bio):
#             self.phy=phy
#             self.chem=chem
#             self.bio=bio
#       @property
#       def percentage(self):
#             return str((self.phy+self.chem+self.bio)/3)+'%'

# s1=Student(40,34,39)
# print(s1.percentage)
# #if now i want to change the phy marks it will be changed but not the percentage
# s1.phy=89
# print(s1.phy)
# print(s1.percentage)

# #OP:
# # 37.666666666666664%
# # 89
# # 54.0%

##----------------------------------------------------------

# #polymorphism
# #One operator can perform different operation wrt the data that is dealing with

# print(1+2)
# print('Yashwanth'+'Gowda')
# print([1,3,5,8]+[2,3,6,9])
# #differnet meaning wrt context
# #This is implicite overloading

# #we can use the same inside class wrt methods
# #Complex number addition
# a=complex(1+3j)
# b=complex(5+7j)
# sum=a+b
# print(sum)
# #OP:
# # (6+10j)

# #Now lets create a class to do the above complex operation
# #using dunder functions

# class Complex:
#       def __init__(self,real,imaginary):
#             self.real=real
#             self.imaginary=imaginary
#       def print_comp(self):
#             print(f'{self.real}i + {self.imaginary}j')
#       def __add__(self,a):
#             newreal= self.real+a.real
#             newimg=self.imaginary+a.imaginary
#             return Complex(newreal,newimg)

#       def __sub__(self,a):
#             newreal= self.real-a.real
#             newimg=self.imaginary-a.imaginary
#             return Complex(newreal,newimg)
# c1=Complex(3,4)
# c1.print_comp()
# c2=Complex(7,6)
# c2.print_comp()

# c3=c1+c2
# c3.print_comp()

# c4=c1-c3
# c4.print_comp()

# #we are seeing operator overloading
# #This was all about Pillers of OOP in Python
# #there are more dunder functions please explore in https://www.geeksforgeeks.org/python/dunder-magic-methods-python/

# #-----------------------------------------------------------------

# # Practice Questions

# # 1.Define a circle class to create a circle with radius r using the constructor.  
# # Define an area method to caluculate the area of the circle.
# # Define a parimeter method to calculate the perimeter of the circle.

# class Circle:
#       def __init__(self,r):
#             self.r=r
#       def area(self):
#             a=3.14*self.r*self.r
#             print(f'Area of circle of radius {self.r} is {a}')
#       def perimeter(self):
#             p=2*3.14*self.r
#             print(f'the perimeter of circle of radius {self.r} is {p}')

# c=Circle(12)
# c.area()
# c.perimeter()
# #OP:
# Area of circle of radius 12 is 452.15999999999997
# the perimeter of circle of radius 12 is 75.36

##------------------------------------------------------------

# # 2.create a Employee class with attributes role, department & salary.
# # This class also as a showDetails() method to display the details
# # Create an Engineer class that inherits the properties of the Employee class
# # and has additional attributes: name and age.

# class Employee:
#       def __init__(self,role,dept,salary):
#             self.role=role
#             self.dept=dept
#             self.salary=salary
#       def showDetails(self):
#             print('Role:',self.role)
#             print('Department:',self.dept)
#             print('Salary:',self.salary)

# class Engineer(Employee):
#       def __init__(self,role,dept,salary,name,age):
#             super().__init__(role,dept,salary)
#             self.name=name
#             self.age=age
#             print('Name:',self.name)
#             print('Age:',self.age)
#             super().showDetails()

# e1=Employee('Developer','ML',25000)
# e1.showDetails()

# e2=Engineer('Developer','data scince',300000,'Yashwanth',20)

# #OP:
# # Role: Developer
# # Department: ML
# # Salary: 25000

# # Name: Yashwanth
# # Age: 20
# # Role: Developer
# # Department: data scince
# # Salary: 300000


# # 3.Create a class called order which stores item and it price.
# # use a dunder function __gt__() to convey that:
# # order1>order2 if price of order1>price of order2

# class Order:
#       def __init__(self,item,price):
#             self.item=item
#             self.price=price
#             #Dunder function to perform the greater than operation
#       def __gt__(self,a):
#             return self.price>a.price
# i1=Order('Biscutes',120)
# print(i1.item)
# print(i1.price)

# i2=Order('Chai ki patha',20)
# print(i2.item)
# print(i2.price)

# i3=Order.__gt__(i1,i2)
# print(i3)
# #OP:
# # Biscutes
# # 120
# # Chai ki patha
# # 20
# # True
# # -----------------End of The Course OOP in Python------------------------------
# # ----------Remember learning never ends and you can learn more advance oop in Python using open source data on internet, thankyou keep learning------------------------------