#EXCEPTION --
# -->is an event/error condition occurs during the execution of a pgm
# --if an exception occurs it will stop the execution of the current pgm and displays a message showing error


# Exception occurs due to various reasons
# --invalid input/data --value error
# --unable to access a file --FileNotFoundError
# --undefined variable --Name error
# --invalid type --type error
# --zero division error
# --unable to access a module --module not found error
# Key error --unable to access a key in dict
# attribute error --unable to access an attribute in a class
# index error  --unable to access a list index
# IOError--invalid file input/output
#
# n1=int(input("enter a number:"))
# n2=int(input("enter a number:"))
# s=n1+n2
# print("sum:",s)
#
# # op
#
# enter a number:6
# enter a number:r
# Traceback (most recent call last):
#   File "E:\python proj\exception.py", line 19, in <module>
#     n2=int(input("enter a number:"))
# ValueError: invalid literal for int() with base 10: 'r'


# "12"+34
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str


# l = 123
# for i in l:
#     print("hello")
#
# Traceback(most
# recent
# call
# last):
# File
# "<input>", line
# 1, in < module >
# TypeError: 'int'
# object is not iterable

# x
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'x' is not defined

# d={'a':10,'b':20}
# d['c']
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# KeyError: 'c'

# --EXCEPTION HANDLING--
# try:
# #     normal code to continue
# except:
# #     handling code if an exception occurs
# else:
# #     code to execute if no exception
# finally:
# #     code to execute whether or not exception occurs


# # # write a program that takes a number as input from user and finds the factorial of that number
# # # using math.factorial().use a try -except block to handle the value error if user inputs a
# # # number/character input
# import math
#
# try:
#     num = int(input("Enter a number: "))
# print("Factorial:", math.factorial(num))
#
# except ValueError:
#     print("Invalid input! Please enter a valid number.")

# import math
# try:
#     n = int(input("Enter a number: "))
#     print("Factorial:", math.factorial(n))
#
# except ValueError:
#     print("Please enter a valid number")


# #
# #
# # Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# # and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# #
# try:
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# print("\n1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
#
# choice = int(input("Enter your choice (1-4): "))
#
# if choice == 1:
# print("Result =", num1 + num2)
#
# elif choice == 2:
# print("Result =", num1 - num2)
#
# elif choice == 3:
# print("Result =", num1 * num2)
#
# elif choice == 4:
# print("Result =", num1 / num2)
#
# else:
# print("Invalid choice!")
#
# except ValueError:
# print("Invalid input! Please enter numbers only.")
#
# except ZeroDivisionError:
# print("Error! Cannot divide by zero.")
#
# # # write a program to open a file (text file) in read mode
# # # if the file does not exist catch the file exception print the error message file does not
# # # exist
# try:
# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()
#
# except FileNotFoundError:
# print("File does not exist.")
# #
# #
# # #Given a Dictionary
# # #
# # # d={"name':"arun","age":23,"place":"ekm"}
# # # Write a program to ask the user to enter a key and display its value.
# # # Handle KeyError if key does not exist
# d = {"name": "arun", "age": 23, "place": "ekm"}
#
# try:
# key = input("Enter a key: ")
# print("Value =", d[key])
#
# except KeyError:
# print("Key does not exist.")



# DATABASE--
#  container of data
#  is an organized collection of related data so that it can be easily stored accessed and updated
#  DBMS -- s/w used to create store and manage db
# mysql,mogodb,sqllite

# 2 types
# relational database(sql)
# --mysql,postgres,sqlite
# --data is organized in tabular

# non-relational db(no-sql)
# --MongoDB
# --data is organized in documents key value/graphssq




