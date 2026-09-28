#sum of 2 numbers
# def add():
#     n1=int(input("enter a number:"))
#     n2= int(input("enter a number:"))
#     s=n1+n2
#     print("sum:",s)
#     return
# add()
#
# #define a function to display "hello your name"
# def display_name():
#     n1=input("enter your name:")
#     print("hello",n1)
#     return
# display_name()
#
# #define a function to find the factorial of a num
# def fact():
#      n1= int(input("enter a number:"))
#      f=1
#      for i in range(1,n1+1):
#         f=f*i
#      print("factorial:",f)
#      return
# fact()
#
# #define a fun to find the count of a specific characg in a given sytring
# def count_ch():
#     count=0
#     s=input("enter a string:")
#     c=input("enter the character:")
#     for i in s:
#         if(i==c):
#             count=count+1
#     print(count)
# count_ch()
#def a fun to check whether the num is prime or not
# def check_prime():
#     n = int(input("enter a number:"))
#
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#     else:
#         print("num is neither prime nor composite")
#
#     return
#
#
# check_prime()

# define a fn to find the factors of a num
# def factors():
#     n = int(input("enter a number:"))
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i)
#     return
#
# factors()


# #functio definition
# def functionname(parameters):
#     "function docstring"
#     function body
#
# parameters--> variables defined inside fn definition
# arguments--> values/variables passed to a fn when it is called
# return-->used to exit from the fn

#sum of 2 num
# def add():
#     n1=int(input("enter a number:"))
#     n2=int(input("enter a number:"))
#     s=n1+n2
#     print("sum",s)
#     return
# add()

# def add(n1,n2):
#     s=n1+n2
#     print("sum",s)
# # add(23,24)
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# add(a,b)

#define a fn that takes amt,year and rate as arg and find the simple interest value(dynamic input)

# def simintrst(p,n,r):
#     si=p*n*r/100
#     print("simple interst",si)
# p=int(input("enter amt:"))
# n=int(input("enter a years:"))
# r=int(input("enter a rate:"))
# simintrst(p,n,r)

#def a fn that takes 2 num as arguments and return sum as result
#call fn and print the result
#
# def add(n1,n2):
#     s=n1+n1n2

#define a function that takes a string as argument  and return a new dict where keys are words and
#values are lengh of each word .call the function
#
# def word_len(s):
#     new={}
#     #words=s.split()
#     for i in s.split():
#         new[i]=len(i)
#     return new
# s=input("enter a string:")
# word_len(s)
# print("result:",word_len(s))


# comprehension

#new={i:len(i) for i in s.split()

#define a fn that takes a number as argument and check whether that number is spy number or not

def spy(n):
    s=str(n)
    sum=0
    product=1
    for i in s:
        sum=sum+int(i)
        product=product*int(i)
    # while n>0:
    #     r=n%10
    #     s=s+r
    #     p=p*r
    #     n=n//10
    if sum==product:
        return "spy number"
    else:
        return "not a spy number"
n=int(input("enter a number:"))
spy(n)
print("result:",spy(n))


