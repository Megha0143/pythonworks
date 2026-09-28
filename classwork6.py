
# # # Q1.Define a function that takes 2 numbers and returns their product
def mul(a,b):
    m=a*b
    return m

a=int(input("enter a number:"))
b=int(input("enter a number:"))
result=mul(a,b)
print("product",result)

#
# # Q2.Define a function that takes a string and returns number of vowels
#
def vowels(s):
    count=0
    for i in s:
        if i in "aeiouAEIOU":
            count=count+1
    return count


s=input("enter a string:")
result=vowels(s)
print("number of vowels", result)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
def area(l,b):
    a=l*b
    return a

l=int(input("enter length:"))
b=int(input("enter breadth:"))
result=area(l,b)
print("area of rectangle:",result)
#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
def even(l):
    new=[]
    for i in l:
        if i%2==0:
            new.append(i)
    return new

l=[45,78,90,12,35]
result=even(l)
print("even numbers",result)



# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

def digit_sum(l):
    new=[]
    for i in l:
        a=i//100
        b=(i//10)%10
        c=i%10
        s=a+b+c
        new.append(s)
    return new

l=[123,345,111,678,134,809]
result=digit_sum(l)
print("new list",result)

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]

def unique(l):
    new=[]
    for i in l:
        if i not in new:
            new.append(i)
    return new

l=[12,34,78,12,67,34,90,23]
result=unique(l)
print("unique elements",result)
#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]

def common(l1,l2):
    new=[]
    for i in l1:
        if i in l2:
            new.append(i)
    return new

l1=[12,34,56,78,90]
l2=[90,34,11,57,45]
result=common(l1,l2)
print("common elements",result)

