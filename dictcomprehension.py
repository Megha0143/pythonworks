#dictionary comprehension
#new_dict={key:value for item in iterable if condition}
#eg:
# l=[1,2,3,4]
#create a new dict where keys are numbers and values are sqrs of each number
#normal code
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

#comprehenion
# new={i:i**2 for i in l}
# print(new)
#
# new={i:i**3 for i in l}
# print(new)

#given a list
# l=[10,20,30,40]
# #create a new dict where keys and values are numbers
# new={i:l[i] for i in range(0,len(l))}
# print(new)

# s="hello world"
# for i in s.split():
#     print(i)

#given a string
#create a new dict where keys are words and values are length of each word

# s="python coding is easy and fun"
# new={i:len(i) for i in s.split()}
# print(new)

