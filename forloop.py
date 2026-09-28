# for i in range(100, 1001, 100):
#     print(i)
#
#
# for i in range(1, 6):
#     print(i**3)
#
#
# for i in range(100,1000):
#     if i % 3==0:
#         print(i)
#
#
# colors=['red' , 'green', 'blue' , 'yellow' , 'black']
# for color in colors:
#     print(color[::-1])

#print each digit in a number
# n=1234
# for i in str(n):
#     print(i)

#sum of digits a number

# n=1234
# sum=0
# for i in str(n):
#     sum=sum+int(i)
# print(sum)

# given a list
# l=[1,2,3,4]
# print sq of each number 1,4,9,16
#
# for i in l:
#     print(i**2)


#create a new list with sq of each number[1,4,9,16]
# l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**2)
#      print(i,"iteration",new)
# print(new)

#set

# l=[1,2,3,4]
# new=set()
# for i in l:
#     new.add(i**2)
# print(new)


#given a str
#s="hello world"
#create a new string with only vowels
# s="hello world"
# new=""
# vowels="aeiouAEIOU"
# for i in s:
#     if i in vowels:
#         new=new+i
# print(new)

#given a list l=[1,2,3,4]
#create a new dict where keys are numbers and values are sq of each nums
#new={1:1,2:4,3:9,4:16}
# l=[1,2,3,4]
# new={}
# for i in l:
#     new[i]=i**2
#     print(new)
# print(new)


#reverse of a string
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

#reverse of a num
# n=1234
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)


#loop control stmnts
#break
# s='hello'
# for i in s:
#     if(i=="l"):
#         break
#     print(i)


#continue-->
# s='hello'
# for i in s:
#     if(i=="l"):
#         continue
#     print(i)

#given a list of numbers
#l=[25,67,34,78,17,44,82]
#print all numbers
#skips all even numbers
#stops the loop when i>50



# l=[25,67,34,78,17,44,82]
# #print all numbers
# for i in l:
#     print(i,end=" ")
# print()
# #stops the loop when i >50
# for i in l:
#     if i>50:
#         break
#     print(i,end=" ")
# print()
# #skips all even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i,end=" ")
# print()



# #2.Given a list
# colors=['red','green','yellow','blue','orange','black']
# # print all colors
# for i in colors:
#     print(i,end=" ")
# print()
# # print those colors starting with 'b'
# for i in colors:
#     if i[0]=='b':
#         print(i,end=" ")
# print()
# # print first color starting with b
# for i in colors:
#     if i[0]=='b':
#         print(i,end=" ")
#         break
# print()
# # skip all colors starting with b
# for i in colors:
#     if i[0]=='b':
#         continue
#     print(i,end=" ")
# print()


#3.given s="python coding is easy and fun"

#print all charac upto a specific char(including that char)
#
# s="python coding is easy and fun"
# for ch in s:
#     print(ch,end="")
#     if ch=="i":
#         break



#Armstrong num

# n=int(input("enter a number:"))
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if sum==n:
#     print("armstrong number")
# else:
#     print("Not an armstrong number")


# n=int(input("enter a number:"))
# s=str(n)
# l=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**l
# if sum==n:
#     print("armstrong number")
# else:
#     print("Not an armstrong number")


#factor of a number
#6-->1,2,3,6
# num=int(input("enter a number:"))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)
#
# #pass
# for i in range(1,11):
#     pass
# print(i)
# #how to create null block in python-->pass
# for i in range(1,11):
#     if(i==3):
#         pass
#     else:
#         print(i)


# for i in range(1,6):
#     if i==3:
#         break
#     print(i)
# else: #it works only after execution
#     print("hello")
#

#check whether given number is prime or not
#
# num=int(input("enter a number:"))
# if(num>1):
#     for i in range(2,num):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:
#     print("number is neither prime nor composite")







