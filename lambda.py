# #Lambda function is a simple function that can be used with advance functions like map(), sort(), filter(), reduce()
# #A shortcut to write small one-line functions.
# #Syntax: lambda<parameters or arguments>: expression
# # a lamda function will take n number of arguments and will always have only one expression 

# add = lambda a,b:a+b
# sub = lambda a,b:a-b
# mult = lambda a,b:a*b
# div = lambda a,b:a/b
# mod = lambda a,b:a%b
# a=int(input('Enter the value of a: '))
# b=int(input('Enter the value of b: '))
# print(add(a,b))
# print(sub(a,b))
# print(mult(a,b))
# print(div(a,b))
# print(mod(a,b))

# #we can also use lambda for advance use 
# #Example

# greater=lambda a,b:a if a>b else b
# check_greatest=lambda a,b:a>b
# print(check_greatest(a,b))
# print(greater(a,b))

# #OP:
# # Enter the value of a: 12
# # Enter the value of b: 3
# # 15
# # 9
# # 36
# # 4.0
# # 0
# # True
# # 12

##--------------------------------------------------

# #Map()----> applies a function operation into all the items in the collection
# #Takes a function and applies it to each item in a list.
# #Syntax: map(function, collection)
# #Let us see how to do using normal functions
# def add(t):
#       return (t*9/5)+32

# temp_deg=[0,20.0,30.0,30.0,40.0,50.0]
# celsius=list(map(add,temp_deg))
# print(celsius)

# #Now lets do the same using lambda function

# cel=list(map(lambda t:(t*9/5)+32, temp_deg))
# print(cel)
# #we can also use a for loop to print
# for temp in cel:
#       print(temp)
# #OP:
# # [32.0, 68.0, 86.0, 86.0, 104.0, 122.0]
# # [32.0, 68.0, 86.0, 86.0, 104.0, 122.0]

#----------------------------------------------------------------

# #filter: Takes a condition and returns only the items that match in the list.
# #First lets doo with a normal function
# age=[12,14,23,18,19,46]
# def eligible(age):
#       if age>=18:
#             return age
# e_age=filter(eligible,age)
# for i in e_age:
#       print(i)

# #let use lambda for the same
# eligible_age=filter(lambda a: a>=18,age)
# print(list(eligible_age))
# #OP:
# # 23
# # 18
# # 19
# # 46
# # [23, 18, 19, 46]

##-------------------------------------------

#reduce: it is a function used to reduce all th elements in a list to single resulted answer
#First let see how to use this using normal function
from functools import reduce
def add(a,b):
      return a+b
numbers=[12,3,4,6,8]
sum=reduce(add,numbers)
print(sum)

#Let us apply the same using lambda function
ex=['Y','A','S','H','U','G','O','W','D','A']
join=reduce(lambda a,b: a+b,ex)
print(join)
#OP:
# 33
# YASHUGOWDA