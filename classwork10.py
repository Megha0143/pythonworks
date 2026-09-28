# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()
class Movie:
    def __init__(self):
        self.moviename=input("Enter Movie Name:")
        self.year=int(input("Enter Year:"))
        self.language=input("Enter Language:")
        self.director=input("Enter Director:")
        self.rating=input("Enter Rating:")
    def display_details(self):
        print(self.moviename,self.year,self.language,self.director,self.rating)
    def update_rating(self):
        self.rating=int(input("Enter updated Rating:"))

m=Movie()
m.display_details()
m.update_rating()


# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.
class Vehicle:
    def __init__(self):
        self.brand=input("Enter Brand:")
        self.model=input("Enter Model:")
        self.color=input("Enter Color:")
        self.year=int(input("Enter Year:"))
    def display(self):
        print(self.brand,self.model,self.color,self.year)

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.mileage=input("Enter Mileage:")
    def display(self):
        super().display()
        print(self.mileage)

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc=input("Enter CC:")
    def display(self):
        super().display()
        print(self.cc)

c=Car()
c.display()
b=Bike()
b.display()