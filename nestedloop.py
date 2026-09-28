##given a list
# l=[10,20,30]
# for i in l:
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()


# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()
#
# op-->
#
# * * * *
# * * * *
# * * * *
# * * * *


# l=[["lion","tiger"],["cat","elephant"]]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)

#given a list
# names=["kelly","alan","jeny"]
# for i in names:
#     for j in range(3):
#         print(i,end=" ")
#     print()
#
# op-->
#
# kelly kelly kelly
# alan alan alan
# jeny jeny jeny


#given 2 lists
# n=[1,2,3]
# q=['what','when','why']
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=" ")
#     print()
#
# op-->
# 1
# what when why
# 2
# what when why
# 3
# what when why

#given a list
# d=[{'id':101,'name':'arun','age':23},
#    {'id':102,'name':'amal','age':24},
#    {'id':103,'name':'anu','age':25}]
# print("id\t","name\t","age\t")
# for i in d:
#     print(i["id"],"\t",i["name"],"\t",i["age"])
#
# op-->
#
# id	 name	 age
# 101 	 arun 	 23
# 102 	 amal 	 24
# 103 	 anu 	 25

# or

# d=[{'id':101,'name':'arun','age':23},
#    {'id':102,'name':'amal','age':24},
#    {'id':103,'name':'anu','age':25}]
# print("id\t","name\t","age\t")
# for i in d:
#     for j in i.values():
#         print(j,"\t",end=" ")
#     print()

# to use key and values in an iteration we can use .items()
# d={'id':101,'name':'arun','age':23}
# for i,j in d.items():
#     print(i,j,end=" ")

#*
# **
# ***

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#
# op-->
# *
# * *
# * * *
# * * * *

# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# op-->
# *
# * * *
# * * * * *
# * * * * * * *

# for i in range(1,5):
#     for j in range(i):
#         print(i,end=" ")
#     print()
#
# op-->
# 1
# 2 2
# 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# op-->
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# op-->
# * * * *
# * * *
# * *
# *

#given a list
#l=[23,45,78,90,12,13,91]
# for i in l:
#     if i%2==0:
#         print(i)

#print all prime num
# for i in l:
#     for j in range(2, i // 2):
#         if i%j==0:
#             #print("not prime")
#             break
#     else:
#         print(i)
#
# op-->
# 23
# 13

#find odd prime num in range (1,100)
for i in range(1,100):
    for j in range(2,i):
        if(i%2!=0):
            print(i)
            break

#find armstrong num in range(100,1000)