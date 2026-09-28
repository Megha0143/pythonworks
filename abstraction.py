# --ABSTRACTION--
#  -->hiding implementation and showing essential details to the user
# eg:
# -->ATM,INSTAGRAM
# -->can be implemented using abstract class
# --abstract class--->it is a class that contains abstract method
# --abstract method--> method does not have any implementation/code

# --eg:
# class Editor:
#     def create_file():
#         pass
#     def write():
#         pass
#     def run():
#         pass
#     def close():
#         pass
#
# class pycharm(Editor):
#     def create_file():
# #         code
#     def write():
# #         code
#     def run():
# #         code
#     def close():
# #         code
# class vscode(Editor):
#
#     def create_file():
#         #         code
#     def write():
#
#         # code
#     def run():
#
#         # code
#     def close():
# #         code


# FEATURES OF ABSTRACT CLASS:
# -->it act as a template/blueprint for all the classes that we inherited from abstract class
# -->it contains at least one abstract method
# -->it cannot be instantiated/cannot create objects
# -->all the subclasses must implement the abstract methods declared inside the abstract class
# -->otherwise subclasses cannot create objects and call its operations
# -->ABC--abstract base class
# syntax
# from abc import ABC,abstractmethod
# class abstractclass(ABC):
#     @abstarctmethod
#     def abstarctmethod(self):
#         pass

#create an abstract clss shape with abstract methods get_area() and get_perimeter()
# create 2 subclasses rectangle and sq each class should calc area and peri differently

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class rectangle(Shape):
#     def __init__(self):
#         self.length=float(input("enter length:"))
#         self.width=float(input("enter width:"))
#     def get_area(self):
#
#         return self.length*self.width
#     def get_perimeter(self):
#         return 2*(self.length +self.width)
# class square(Shape):
#     def __init__(self):
#         self.side=float(input("enter side:"))
#     def get_area(self):
#         return self.side*self.side
#     def get_perimeter(self):
#         return 4*self.side
# r=rectangle()
# print("rectangle area:",r.get_area())
# print("rectangle perimeter:",r.get_perimeter())
#
# s = square()
# print("Square Area:", s.get_area())
# print("Square Perimeter:", s.get_perimeter())


# create an abstract class employee with an abstrct method calculate_salary()
# create 2 subclass
# full time employee
# part time employee
# each class should  calculate salary differently
# each employee-- common properties-empid,name,age
# fulltime employee-- additional property--monthly salary
# part time employee -- additional property--hours rate

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self):
        self.empid = int(input("Enter employee id: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self):
        super().__init__()
        self.monthly_salary = float(input("Enter monthly salary: "))

    def calculate_salary(self):
        print("Salary:", self.monthly_salary)

class PartTimeEmployee(Employee):

    def __init__(self):
        super().__init__()
        self.hours = float(input("Enter working hours: "))
        self.hour_rate = float(input("Enter hourly rate: "))

    def calculate_salary(self):
        salary = self.hours * self.hour_rate
        print("Salary:", salary)


# Full Time Employee
f = FullTimeEmployee()
f.calculate_salary()

# Part Time Employee
p = PartTimeEmployee()
p.calculate_salary()


