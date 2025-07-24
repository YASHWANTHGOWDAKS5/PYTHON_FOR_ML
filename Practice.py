# let us know about functions
# it is a repeting reusable block of code in python and other programming language
# In python we have two types 1.Built in functions for example: print(),len() etc..

# let us make a user defined parameterize function for calculating the factorial of a number

def factorial(n):
      factorial=1
      for i in range(1,n+1):
            factorial*=i
      print('the factorial of', n,' numbers is:',factorial)

num = int(input("Entert the number:"))
if num >=0: #Remember that a input function in python by default returns string
      factorial(num)