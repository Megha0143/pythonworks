
# #Write a program to check whether two entered numbers are equal or not

n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
if n1==n2:
    print("equal")
else:
    print("not equal")

# #Write a program to check whether two entered words are equal or not

n1=input("enter a word:")
n2=input("enter a word:")
if n1==n2:
    print("equal")
else:
    print("not equal")

# #Write a program to find the maximum of two numbers

n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
if n1>n2:
    print(n1,"is greatest")
else:
    print(n2,"is greatest")






# #write a program to check whether the entered character is vowel or not

ch=input("enter your character:")
vowel="aeiouAEIOU"
if ch in vowel:
    print("entered character is a vowel")
else:
    print("not a vowel")

# #Write a program to check whether the entered country name contains word 'land'

loc=input("enter a  location:")
if 'land' in loc:
    print("location is:", loc)
else:
    print("invalid")
# #write a program to check whether the entered number is 3 digit or not

n1=int(input("enter a number:"))
if n1>=100 and n1<=999:
    print("entered number is 3 digit")
else:
    print("Not a 3 digit number")




#write a program to check whether the entered string is  palindromde or not

ch=input("enter a word:")
c1=ch[::-1]
if ch==c1:
    print("entered word is palindrome")
else:
    print("not a palindrome")



#Write a program to check whether a number is present in given list

l=[23,67,12,90]
n=int(input("enter a number:"))
if n in l:
    print("present")
else:
    print("not present")
#Write a program to check whether a key is prsent in a dictionary or not

d={101:'Arun',102:'Amal',103:'Anu'}
n=int(input("enter the key:"))
if n in d:
    print("present")
else:
    print("not present")



#Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)
n=input("enter your password:")
if len(n)<8:
    print("entered password is weak")
else:
    print("entered password is strong")
