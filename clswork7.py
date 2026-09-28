# Q.Write Python Programs Using map(), filter(), or reduce()
#
# 1.Capitalize all names in a list
names = ['alin', 'arun', 'anu']
print(list(map(lambda s:s.capitalize(),names)))
#['Alin', 'Arun', 'Anu']

# 2.Append "@gmail.com" to a list of usernames
users = ['user1', 'user2']
print(list(map(lambda x:x+"@gmail.com",users)))
#['user1@gmail.com', 'user2@gmail.com']

# 3.Filter out all empty strings from a list
words = ['hello', ' ', 'world', ' ', 'python']
print(list(filter(lambda x:x!=' ',words)))
#['hello', 'world', 'python']

# 4.Filter names that start with the letter 'A'
names = ['Anu', 'Neenu', 'Arun', 'Ravi']
print(list(filter(lambda x:x[0]=='A',names)))
#['Anu', 'Arun']

# 5.Concatenate all strings in a list
words = ['Python', 'is', 'fun']
import functools
print(functools.reduce(lambda x,y:x+" "+y,words))
# Python is fun

# 6.Multiply all numbers in a list
nums = [2, 3, 4]
import functools
print(functools.reduce(lambda x,y:x*y,nums,1))
# 24

# 7.Extract First Character of Each Word
words = ["apple", "banana", "cherry"]
print(list(map(lambda x:x[0],words)))
# ['a', 'b', 'c']

# 8.Add 10 to Each Number
nums = [5, 10, 15]
print(list(map(lambda x:x+10,nums)))
# [15, 20, 25]

# 9.Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
    # #Sum of positive even numbers
a = sum(filter(lambda x: x > 0 and x % 2 == 0, l))
print("Sum of positive even numbers:", a)
# Sum of positive even numbers: 222

    # #Sum of Positive Odd numbers
b = sum(filter(lambda x: x > 0 and x % 2 != 0, l))
print("Sum of positive odd numbers:", b)
# Sum of positive odd numbers: 48

    # #Sum of Negative  odd numbers
c = sum(filter(lambda x: x < 0 and x % 2 != 0, l))
print("Sum of negative odd numbers:", c)
# Sum of negative odd numbers: -11


    # #Sum of Negatve Even numbers
d = sum(filter(lambda x: x < 0 and x % 2 == 0, l))
print("Sum of negative even numbers:", d)
# Sum of negative even numbers: -40

    # #Count of Positive numbers
e = len(list(filter(lambda x: x > 0, l)))
print("Count of positive numbers:", e)
# Count of positive numbers: 7

    # #Count of negative numbers
f = len(list(filter(lambda x: x < 0, l)))
print("Count of negative numbers:", f)
# Count of negative numbers: 4

# 10.Given a list
nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]
print(list(map(int,nums)))
# [1, 2, 3, 4]

# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase
print(list(map(lambda x:x['name'].upper(),p)))
# ['LAPTOP', 'PHONE', 'WATCH', 'TABLET']

#print products with price greater than 10000
print(list(filter(lambda x:x['price']>10000,p)))
# [{'name': 'laptop', 'price': 50000}, {'name': 'phone', 'price': 20000}, {'name': 'Tablet', 'price': 25000}]

#Find the total price of all products
import functools
print(functools.reduce(lambda x,y:x+y['price'],p,0))
# 98000