# # Everything in python is stored as objects also called as instences.
# # like class int, class str etc.

# name ='Yashu'
# age ='29'
# print(name.upper())
# print(type(age))
# print(name)

# # the below class can be said as a objects in python.

# class Dog:
#       def bark(self):
#             print('Worf worf')

# dog1 = dog()
# dog1.bark()
# dog2 = dog()
# dog2.bark()

## -----------------------------------------------------

#Understanding self inside a init instence or method

# class Student:
#       #The init instence in python will exicute autromatically whenever you invoke a class irrespective of methods
#       def __init__(self,name,age):
#             self.name=name
#             self.age=age
#             print(f'Your name is {self.name} and age is:{self.age}')
# # So self is used to refer to the perticular object to which the created class(object) is initialized.
# #For here it will be refered to S1
# s1=Student("Yashwanth Gowda KS",20)
# #outPut
# #Your name is Yashwanth Gowda KS and age is:20

# #Also we can test for different student
# s2=Student("LalithRajR",19)
# # OP:
# # Your name is Yashwanth Gowda KS and age is:20
# # Your name is LalithRajR and age is:19

# #And also we can seperate the results like below.
# print(s2.name)
# #OP:
# #LalithRajR

##--------------------------------------------------------

# #And also we have another constructor of init that we call as default Constructor
# class Car:
#       #Only the self parameter is used ijn default and it will be executed whenever this class is called irrespective of methods
#       #And only isf the parameters are matching otherwise it will not
#       def __init__(self):
#             print('Class Car is called now.....')
#       #And also we can have another init constructor
#       def __init__(self,color,brand):
#             self.color=color
#             self.brand=brand
#             print(f'The color of the car {self} is {self.color} and it is of brand {self.brand}')
#             #the self inside print will print the memory address of c1.
# c1=Car("Blue","BMW")
# # OP:
# # Class Car is called now.....

## --------------------------------------------------------

# #Class Attributes and Method attributes
# # we have two different attributes in oop that is if a value will be same for all instences we will use it in class attribute (Global attribute) and it will be also used as the default value for certain instences attributes. 
# # The highest priority is given to the instence or tthe method attributes

# class Employee:
#       default_commision='NO_COMMISION'
#       def __init__(self,name,salary,commision=None):
#             self.name=name
#             self.salary=salary
#             self.commision=commision if commision is not None else Employee.default_commision
#             print(f'Employee {self.name} gets salary {self.salary} and commsion is: {self.commision}')
# #Default value for commision
# default=Employee.default_commision
# print(default)      
# e1=Employee('Pavan',12000,'1300')
# #Default of commision i sprinted if not passed in the object while initializing
# e2=Employee('Hithen',19000)
# #OP:
# # NO_COMMISION
# # Employee Pavan gets salary 12000 and commsion is: 1300
# # Employee Hithen gets salary 19000 and commsion is: NO_COMMISION

# #  -------------------------------------------------

# #Let us know about the methods in classes
# #functions inside a class is called as methods

# class Student:
#       Name = 'UnNymous'
#       def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks
#       #We will always pass self as a argument indide a parameter brackets of the method
#       def wellcome(self):
#             print('Wellcome student,',self.name)

#       #And also we can declare n number of methods inside a class
#       #note: Do not use same names for variable and methods
#       def get_marks(self):
#             print('Marks of', self.name ,'is,',self.marks)

## We create a object for a class as below
# s1=Student('Hasan',95)
# s1.wellcome()
# s1.get_marks()

# #OP:
# # Wellcome student, Hasan
# # Marks of Hasan is, 95

## --------------------------------------------

# #Practice Question
# #1.Create a student class that takes name and marks of 3 subjects as arguments in constructor.
# #Then create a method to print the average.


# #Always the name of the class should start with a capital letter
# class Student:
#       def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks
#       def print_average(self):
#             sum=0
#             for i in range(len(self.marks)):
#                   print('mark',i+1,'is',self.marks[i])
#                   sum+=self.marks[i]
#             avg=sum/len(self.marks)
#             print(f'Average marks of {self.name} is {avg}')

# #Create a object foor the student class
# s1=Student('Shrungar',[29,30,35])
# s1.print_average()
# s2=Student('Mahadev TT',[30,36,23])
# s2.print_average()
# print('Done')

# # OP:
# # mark 1 is 29
# # mark 2 is 30
# # mark 3 is 35
# # Average marks of Shrungar is 31.333333333333332
# # mark 1 is 30
# # mark 2 is 36
# # mark 3 is 23
# # Average marks of Mahadev TT is 29.666666666666668

## ------------------------------------------------------

#Static Methods
#the methods that will not have any self parameter
#Work on Class Level
#We use decorator to convert a method into static method--(@staticmethod)
#A decorator allows us to wrap another function to extend the beheviour of the wrapper function without permanently modifying it

# class Student:
#       Name = 'UnNymous'
#       def __init__(self,name,marks):
#             self.name=name
#             self.marks=marks

#       #Static Method
#       @staticmethod
#       def intro():
#             print('This is AI Department')
#       #We will always pass self as a argument indide a parameter brackets of the method
#       def wellcome(self):
#             print('Wellcome student,',self.name)

#       #And also we can declare n number of methods inside a class
#       #note: Do not use same names for variable and methods
#       def get_marks(self):
#             print('Marks of', self.name ,'is,',self.marks)

# # We create a object for a class as below
# s1=Student('Hasan',95)
# s1.intro()
# s1.wellcome()
# s1.get_marks()

# #OP:
# # This is AI Department
# # Wellcome student, Hasan
# # Marks of Hasan is, 95

## -----------------------------------------

# Pillers of OOP
# 1.Abstractio
# 2.Encapsulation
# 3.Inheritence
# 4.Polymorphism

##-------------------------------------------

# #1. Abstraction in OOP
# # Hiding some working functionality from the user

# # Example:

# class Car:
#       def __init__(self):
#             self.on=False
#             self.clutch:False
#             self.Accelerator=False
#             #The above data will be hided for the user becaouse it is not needed for him
#       def start(self):
#             self.on=True
#             self.clutch=True
#             #The above data will be hided for the user becaouse it is not needed for him
#             print('Engine started you can move the car')

# user=Car()
# user.start()

# #OP:
# # Engine started you can move the car

#----------------------------------------------------

# 2.Encapsulation in OOP
# Wrapping Data and Functions into a single unit that is nothing but our class
# What ever we did above is Encapsulation

#---------------------------------------------------

# # Part-1 of OOP learning ends here and lets solve a Practice Question
# #Create a Account class with 2 attributes- Account number and balance. Create methods for debit, credit and printing the balance

# class Accounts():
#       def __init__(self,acc_no,balance):
#             self.acc_no=acc_no
#             self.balance=balance
#       def debit(self,amount=None):
#             self.amount=amount
#             if self.amount is not None:
#                  self.balance -= self.amount
#                  print(f'Amount of {self.amount} is deducted from balance {self.balance} as you withdrawed it.')
#       def credit(self,amount=None):
#             self.amount=amount
#             if self.amount is not None:
#                   self.balance += self.amount
#                   print(f'An amount of {self.amount} is added to your balance {self.balance} successfully')

#       def print_Bal(self):
#             print(f'Your account of acc_number: {self.acc_no} as current balance of {self.balance} rupees')  
      

# user1=Accounts(1234,20000)
# user1.debit(1000)
# user1.print_Bal()

# user2=Accounts(9875,1200)
# user2.credit(1800)
# user2.print_Bal()

# #OP:
# # Amount of 1000 is deducted from balance 19000 as you withdrawed it.
# # Your account of acc_number: 1234 as current balance of 19000 rupees
# # An amount of 1800 is added to your balance 3000 successfully
# # Your account of acc_number: 9875 as current balance of 3000 rupees

##-------------------- End of Part_1 of OOP in Python-------------------------------------
##------------ Refer the part_2 for completion of the course ------------------------------