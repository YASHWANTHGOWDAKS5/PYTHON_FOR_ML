# #Notes in P_6 written Notes
# #Lets Gpo with the problems 
# #Problem 1:
# def length(v):
#       return len(v)
# v='Yashhwanth'
# l=[1,2,3,4,5,6]
# s={'yashu','Gowda',19,'Male',True}
# result=length(v)
# result1=length(l)
# result2=length(s)
# print(f'Length of {v} is: {result}')
# print(f'Length of {l} is: {result1}')
# print(f'Length of {s} is: {result2}')
# #OP:
# # Length of Yashwanth is: 9
# # Length of [1, 2, 3, 4, 5, 6] is: 6
# # Length of {True, 19, 'Gowda', 'yashu', 'Male'} is: 5

# #------------------------------------------------

# #Problem 2:
# #Printing of all list elements in a single line

# def elements(l):
#       for i in range(len(l)):
#             print(l[i],end="")

# l=[1,5,',',7,3,4,5,' ','Rupees']
# elements(l)
# #OP:
# # 15,7345 

##-------------------------------------------

# #Problem 3:
# #Factorial of n
# def factorial(n=1):
#       f=1
#       for i in range(1,n+1):
#             f*=i
#       return f

# n=int(input('Enter the number to calculate the factorial: '))
# result=factorial(n)
# print(f'Factorial of {n} is: {result}')
# #OP:
# # Enter the number to calculate the factorial: 5
# # Factorial of 5 is: 120

##------------------------------------------

# #Problem:4
# #Conversion of USD to INR
# def Convert(d):
#       return d*86
# d=int(input('Enter doalrs to convert into ruppes: '))
# result=Convert(d)
# print(f'In India {d}$ is {result}','Rupees')
# #OP:
# # Enter doalrs to convert into ruppes: 5
# # In India 5$ is 430 Rupees

##------------------------------------------------------

# #problem 5:
# #To check if a given number is EVEN or ODD
# def Check(n):
#       return 'Even' if n%2==0 else 'Odd'
# print(Check(3))
# #OP:
# #Odd

# #--------------------------

# #Recursion
# #Problem 1:
# def display(n):
#       if n==0:
#             return
#       print(n)
#       display(n-1)
#       print('Class Stacking example')
# display(3)
# #OP:
# # 3
# # 2
# # 1
# # Class Stacking example
# # Class Stacking example
# # Class Stacking example

##-----------------------------------------------------

# #Problem 2:
# #Factorial:

# def factorial(n):
#       if n==0 or n==1:
#             return 1
#       else:
#             return n*factorial(n-1)
      
# print(factorial(5))
# #OP: 120

# #-------------------------------------------

# #Problem 3:
# def cal_sum(n):
#       if n==0:
#             return 0
#       return cal_sum(n-1)+n

# sum= cal_sum(5)
# print(sum)
# #OP:15

# #----------------------------------------------

# #Problem 4:

# def printlist(l,n):
#       if n==0:
#             return
#       print(l[n-1])
#       printlist(l,n-1)
# l=[1,2,3,4,5]

# printlist(l,len(l))

# #For Forward printing:
# def printlist(l,n):
#       if n==len(l):
#             return
#       print(l[n])
#       printlist(l,n+1)
# l=[1,2,3,4,5]

# printlist(l,0)

##OP1:
## 5
## 4
## 3
##2
## 1

##OP2:
##1
##2
##3
##4
##5

##------------------------- End of functions and Recursions ----------------------------

