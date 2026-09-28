#WAP to check the following
# a num is divisible by 2 and 3
# num is div by 2 and not div by 3
# num is div by 3 and not div by 2
#num is not div by 2 and 3

# n=int(input("enter a num:"))
# if n%2==0:
#     print("entered num is divisible by 2")
#     if n%3==0:
#         print("entered num is divisible by 3")
#     else:
#         print("entered number is not divisible by 3 ")
# else:
#     print("entered num is not divisible by 2")
#     if n%3==0:
#         print("entered num is divisible by 3")
#     else:
#         print("entered num is not divisible by 3 ")

#wap to check the given num is positive even or odd
#neg even or neg odd

n=int(input("enter a num:"))
if n>0:
    print("num is positive")
    if n%2==0:
        print("num is even")
    else:
        print("num is odd")
else:
    print("num is negative")
    if n%2==0:
        print("num is negative even")
    else:
        print("num is negative odd")
