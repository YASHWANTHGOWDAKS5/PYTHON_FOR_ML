# # list comparision is way to create list using specific syntax
# # Syntax: ["expression" an "iterable" for the list and a "if" condition if needed]

# a=[2,21,3,4,6]
# res = [val ** 2 for val in a if val%2 ==0]
# print(res)
# #OP:
# # [4, 16, 36]
# #the above is an example of comperhension of list 
# #if we have a list of integers and we want to create a new list by using the existing by applying some operations ont the list

##----------------------------------------------------

# #Now et us see the difference between the general method and the comprehension.
# #Problem 1
# #Given a list and x print the new list having the list elements less than the x value
# l1=[12,3,2,4,53,45,56,76,45,32]
# new_list=[]
# def smaller(l1,x):
#       for num in l1:
#             if num<x:
#                   new_list.append(num)

#       return new_list
# print('New list',smaller(l1,30))
# #OP:
# # New list [12, 3, 2, 4]

##----------------------------------------------------------------------

# #Now lets do the same using comprehensions
# l1=[12,3,2,4,53,45,56,76,45,32]
# a=30
# new_list=[x for x in l1 if x<a]
# print(new_list)
# #OP:
# # [12, 3, 2, 4]

##-------------------------------------------

# #Problem 2
# #Given a list create two new list using that one with all even numbers and one with all odd numbers form the input list

# def eo(l1):
#       even=[x for x in l1 if x%2==0]
#       odd=[y for y in l1 if y%2!=0]
#       return even,odd
# l1=[1,2,3,4,5,6,7,8,9]
# print(eo(l1))

# #OP:
# # ([2, 4, 6, 8], [1, 3, 5, 7, 9])

##----------------------------------------

# #Problem 3:
# #Find the ovel used in a string

# def ovel(s):
#       o=[a for a in s if a in 'aeiou']
#       return o
# s='yashwanthgowdaks'
# print(f"Ovel used in {s} are: ",ovel(s))

# #OP:
# # Ovel used in yashwanthgowdaks are:  ['a', 'a', 'o', 'a']

##----------------------------------------

# #Problem 3
# #Get all the words that start with y and print the word in upper case
# def upper(s):
#       u=[w.upper() for w in s if w.startswith('y')]
#       return u
# s=['yashu','lalith','yes','yup','hithen']
# print(f'The words that starts with u=y in list {s} are: ',upper(s))

# #OP:
# # The words that starts with u=y in list ['yashu', 'lalith', 'yes', 'yup', 'hithen'] are:  ['YASHU', 'YES', 'YUP']

##-----------------------------------------------------

# #We can also see "set comprehensions" it is just as "list comprehension" but we will use "curly braces "{}"."

# def eo(l1):
#       even={x for x in l1 if x%2==0}
#       odd={y for y in l1 if y%2!=0}
#       return even,odd
# l1=[1,2,3,4,5,6,7,8,9]
# print(eo(l1))

# #OP:
## as we are using set it should have disticnt values only
# # ({8, 2, 4, 6}, {1, 3, 5, 7, 9})

#-----------------------------------------------------------

# #Now let us see what is dictionary comprehension
# #Lets understand the working and syntax through three examples
# #Example-1

# l1=[12,3,4,5,6,7]
# d1={x:x*2 for x in l1 if x!=0}

# print(d1)
# #OP:
# # {12: 24, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14}

##-------------------------------------------------

# #Example-2:
# d2={i:f'4MH23CA00{i}' for i in range(1,6)}
# print(d2)
# #OP:
# # {1: '4MH23CA001', 2: '4MH23CA002',
# #  3: '4MH23CA003', 4: '4MH23CA004',
# #  5: '4MH23CA005'}

##------------------------------------------------

# #Example-3
# l1=[1,2,3,4,5,6,7]
# s1=['yashuGowda','Pavan','Hithesh','Lalith','seena','Gunda','Reddy']

# d1={f"{l1[i]}:Name:{s1[i]}" for i in range(len(l1))}
# print(d1)
# #OP:
# # {'1:Name:yashuGowda', '2:Name:Pavan', '4:Name:Lalith',
# #  '5:Name:seena', '7:Name:Reddy',
# #  '6:Name:Gunda', '3:Name:Hithesh'}

##--------------------------------------------------

# #A better way to do the example 3 is osing constraint "dict" and "zip"
# l1=[1,2,3,4,5,6,7]
# s1=['yashuGowda','Pavan','Hithesh','Lalith','seena','Gunda','Reddy']

# d1=dict(zip(l1,s1))
# print(d1)
# #OP:
# # {1: 'yashuGowda', 2: 'Pavan',
# #  3: 'Hithesh', 4: 'Lalith',
# #  5: 'seena', 6: 'Gunda',
# #  7: 'Reddy'}

##----------------------------------------------------------

# #Reversing the dictionary comprehension
# d1={1:'yashu',2:'Hithesh',3:'Varsha',4:'Pavan'}
# d2={v:k for (k,v) in d1.items()} #This shuld reverse the keys with value and value with key
# l1=[z for z in d1.items()] #This creates a list of key value pair in the dict
# print(d2)
# print(l1)
# #OP:
# # {'yashu': 1, 'Hithesh': 2, 'Varsha': 3, 'Pavan': 4}
# # [(1, 'yashu'), (2, 'Hithesh'), (3, 'Varsha'), (4, 'Pavan')]

##------------------ End of Comprehensions in Python -------------------------------
##--------- Get more details in geeksforgeeks.org ------------------------------