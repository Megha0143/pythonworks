# PyDev console: starting.
# Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
# d={'name':'arun','age':23,'course':'python'}
# d.keys()
# dict_keys(['name', 'age', 'course'])
# d.get('name')
# 'arun'
# d.popitem()
# ('course', 'python')
# d.pop('age')
# 23
# d
# {'name': 'arun'}

# define a fn that takes anum as arg and return its sq

# def sqr(x):
#     s=x*x
#     return s
# x=int(input("enter a number:"))
# sqr(x)
# print(sqr(x))

# using lambda
# a=lambda x:x*x
# print(a(5))

# #sum of 2 numbers
#  lambda a,b:a+b
#
# #product of 2 num
# lambda a,b:a*b
#
# #cube of a num
# lambda a:a**3
#
# #first lettr of a string
# lambda s:s[0]
#
# # length of a string
# lambda s:len(s)
#
# # reverse of a string
# lambda s:s[::-1]
# # name value from a dict
# a=lambda d:d['name']
# print(a{'name':'arun','age':23})
#
#
# # second element from a list
# lambda l:l[1]
#
# # add 10 to a number
#
# lambda x:x+10


# create a new list of sqrs
# n=[1,2,3,4]
# print(map(lambda x:x**2,n))
# print(list(map(lambda x:x**2,n)))
# print(tuple(map(lambda x:x**2,n)))
# print(set(map(lambda x:x**2,n)))

# #create a new list of cubes
# l=[1,2,3,4]
# print(map(lambda x:x**3,l))
# print(list(map(lambda x:x**3,l)))
# # print(tuple(map(lambda x:x**3,l)))
# # print(set(map(lambda x:x**3,l)))
#
# #create a new list of square roots
# l=[25,36,81,100]
# print(map(lambda x:x**0.5,l))
# print(list(map(lambda x:x**0.5,l)))
# # print(tuple(map(lambda x:x**0.5,l)))
# # print(set(map(lambda x:x**0.5,l)))
#
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda x:len(x),colors)))
#
# #create a new list of first characters
# print(list(map(lambda x:x[0],colors)))
#
# #create a new list of last characters
#
# print(list(map(lambda x:x[-1],colors)))
#
# #create a new list of reverse of each elemnt
#
# print(list(map(lambda x:x[::-1],colors)))
#
# # Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))
#
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# email=list(map(lambda x:x['email'],l))
# print(email)

# -----> FILTER
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x%2==0,l)))
# print(list(filter(lambda x:x%2==0,l)))

l=[24,45,67,12,89,70]
# filter even values >50
print(list(filter(lambda x:x%2==0 and x>50,l)))

# filter the color whose len is greater than 5
colors=['red','green','blue','yellow','black','orange']
print(list(filter(lambda x:len(x)>5,colors)))

# filter the color containing letter 'n'
print(list(filter(lambda x:'n'in x,colors)))

# ------REDUCE()

l=[1,2,3,4]
# sum of list using reduce()
import functools
print(functools.reduce(lambda x,y:x+y,l,0))
# product of list using reduce()
import functools
print(functools.reduce(lambda x,y:x*y,l))