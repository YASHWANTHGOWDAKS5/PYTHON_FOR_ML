# #  Built-in Exception Types in Python

# # | Exception Type      | Description |
# # -------------------------------------------------------------------------
# # | SyntaxError         | Raised when Python encounters invalid syntax. | 
# # | IndentationError    | A subclass of SyntaxError, triggered by incorrect indentation. | 
# # | TypeError           | Occurs when an operation is performed on an incompatible type. | 
# # | ValueError          | Raised when a function receives the right type but inappropriate value. | 
# # | NameError           | Happens when a variable is not defined. | 
# # | IndexError          | Triggered when trying to access an index that’s out of range. | 
# # | KeyError            | Raised when accessing a non-existent key in a dictionary. | 
# # | AttributeError      | Occurs when an invalid attribute reference is made. | 
# # | ImportError         | Raised when an import fails. | 
# # | ModuleNotFoundError | Subclass of ImportError, specifically for missing modules. | 
# # | ZeroDivisionError   | Happens when dividing by zero. | 
# # | FileNotFoundError   | Raised when trying to access a file that doesn't exist. | 
# # | IOError             | Related to I/O operations failing. | 
# # | RuntimeError        | A generic error for unexpected runtime issues. | 
# # | AssertionError      | Triggered when an assert statement fails. | 
# # | StopIteration       | Raised by next() to indicate no further items. | 
# # | KeyboardInterrupt   | Triggered when user interrupts execution with Ctrl+C. | 
# # | MemoryError         | Raised when an operation runs out of memory. | 

# # Explore more in the official page - Python.org

# #Practice Questions regarding Try, Exception, else, finally
# #Safe Division calculation

# def safe_division():
#       try:
#             a=float(input('Enter the numerator: '))
#             b=float(input('Enter the denominator: '))
#             result=a/b
#       except ValueError:
#             print('Please Enter a number')
#       except ZeroDivisionError:
#             print('Cant divide with a zero ')
#       else:
#             print('Result of division is',result)
#       finally:
#             print('The dividon try block executed and this is finally block')

# safe_division()

##---------------------------------------------------------------

# #Reading a file that does not exists

# def Read_file():
#       try:
#             s=open('Practice1.txt', 'r')
#             data=s.read()
#       except FileNotFoundError:
#             print('There is not such file in the provided address')
#       else:
#             print(data)
#       finally:
#             print('The read file block executed and this is its finnaly block')

# Read_file()

##---------------------------------------------------------

# #User input: converting a string to integer

# def input_check():
#       a=str(input('Enter your name'))
#       print('Your name is: ',a)
#       try:
#             a=int(a)
#       except ValueError:
#             print('String can not be converted into Integer')
#       else:
#             print(a)
#             print(type(a))
#       finally:
#             print('The input try block executed and i am its finally block')

# input_check()

##-----------------------------------------------------

# #email validation
# #here we will explore how we can create our own exception

# def Email_Validation(email: str)-> str:
#       try:
#             if '@' not in email or '.' not in email:
#                   raise ValueError('Invalid email formate->correct formate:->example@gmail.com')
#       except ValueError as ve:
#             print(f'Error: {ve}')
#       else:
#             print(email)
#       finally:
#             print('The email validtaion try block exicuted and i am its finally block')

# email='yashwanthksgowda.gmail.com'
# Email_Validation(email)

##------------------------------------------------------------

# #Student marks calculator with log file
# #Revision of the file handling in python

# def Student_Marks():
#       try:
#             marks=[]
#             for i in range(1,6):
#                   m=int(input(f'Enter the marks for Subject-{i}->'))
#                   if m<0 or m>100:
#                         raise ValueError('Enter the marks that ranges between 0 to 100 only.')
#                   marks.append(m)
#       except ValueError as v:
#             print(f'Error:{v}')
#       except :
#             print('Enter a number not a string')
#       else:
#             average=sum(marks)/5
#             with open('Log.txt','w') as w:
#                   w.write(str(marks))
#                   w.write('\n')
#                   w.write(f'Average Marks is {average}')
#             with open('Log.txt','r') as r:
#                   data=r.read()
#                   print("data inside the Log.txt:\n",data)
#       finally:
#             print("the student marks try block executed and i am its finally block")

# Student_Marks()
# #OP:
# # Enter the marks for Subject-1->89
# # Enter the marks for Subject-2->97
# # Enter the marks for Subject-3->98
# # Enter the marks for Subject-4->96
# # Enter the marks for Subject-5->90
# # data inside the Log.txt:
# #  [89, 97, 98, 96, 90]
# # Average Marks is 94.0
# # the student marks try block executed and i am its finally block

##--------------------------------------------------------------

#Online payment simulation

def payment_simulation():
      try:
            m=int(input('Enter the amount: '))
            if m <0:
                  raise Exception(f'The amount should be a positive digit you entered {m}')
            if m>10000:
                  raise ValueError('Exceeded the limit can not process the transaction')
            card=str(input('Enter the 5 digit card number'))
            b=int(len(card))
            if b<5 or b>5:
                  raise RuntimeError('The card number is not valid')
      except ValueError as ve:
            print(f'Error:{ve}')
      except Exception as e:
            print(f'Error:{e}')
      except RuntimeError as re:
            print(f'R_Error:{re}')
      else:
            print(f'An amout of {m} as been transfered')
      finally:
            print('The transaction try block exicuted and i am its finally block')

payment_simulation()
