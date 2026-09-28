#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

w=float(input("enter weight:"))
h=float(input("enter height:"))
height=h/100
BMI=w/height**2
if BMI>=40.0:
    print("obese")
elif BMI>=25.0 and BMI<40:
    print("overweight")
elif BMI>=18.5 and BMI<25.0:
    print("normal")
elif BMI<=18.4:
    print("underweight")

#2.# A toy vendor supplies three types of toys:



# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.


# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

code=int(input("code: "))
amt=float(input("amount: "))
if code==1:
    if amt >=1000:
        d=amt-(amt*0.010)
        print(d)
    else:
        print("no discount")
elif code==2:
    if amt>=100:
        d=amt-(amt*(5/100))
        print(d)
    else:
        print("no discount")
elif code==3:
    if amt>=500:
        d=amt-(amt*(10/100))
        print(d)
    else:
        print("no discount")
else:
    print("invalid code")

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

n=int(input("number: "))
if n%3==0:
    if n%5==0:
        print("fizzbuzz")
    else:
        print("fizz")
else:
    if n%5==0:
        print("buzz")
    else:
        print(n)