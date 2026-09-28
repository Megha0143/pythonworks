# #baking operations-menu driven (using class and list)
# from os import access
#
#
#
# # create a new account
# # withdraw
# # deposit
# # showbalance
# # exit
# class Account:
#     def __init__(self):
#         self.acctnumber = input("Enter account number: ")
#         self.acctname = input("Enter account name: ")
#         self.balance = float(input("Enter balance: "))
#     def withdraw(self):
#         amt = float(input("Enter amount to withdraw: "))
#         if amt <= self.balance:
#             self.balance = self.balance - amt
#             print("Amount withdrawn:", amt)
#         else:
#             print("Insufficient balance")
#
#     def deposit(self):
#         amount = float(input("Enter amount to deposit: "))
#         self.balance = self.balance + amount
#         print("Amount deposited:", amount)
#
#     def showbalance(self):
#         print("Current balance:", self.balance)
# l=[]
# while (1):
#     print('1.create an account')
#     print('2.withdraw')
#     print('3.deposit')
#     print('4.show balance')
#     print('5.exit')
#
#     ch=int(input("enter your choice:"))
#
#
#     if ch == 1:
#         a = Account()
#         l.append(a)
#         print("Account created successfully")
#
#     elif ch== 2:
#         number = int(input("enter account number:"))
#         for i in l:
#
#             if i.acctnumber==number:
#                 i.withdraw()
#                 break
#         else:
#             print("acc does not exist")
#         # if len(l) == 0:
#         #     print("No accounts available")
#         # else:
#         #     l[0].withdraw()
#
#     elif ch== 3:
#         number = int(input("enter account number:"))
#         for i in l:
#
#             if i.acctnumber == number:
#                 i.deposit()
#                 break
#         else:
#             print("acc does not exist")
#
#     #     if len(l) == 0:
#     #         print("No accounts available")
#     #     else:
#     #         l[0].deposit()
#
#     elif ch == 4:
#          number = int(input("enter account number:"))
#          for i in l:
#
#              if i.acctnumber == number:
#                  i.showbalance()
#                  break
#          else:
#              print("acc does not exist")
#     #     if len(l) == 0:
#     #         print("No accounts available")
#     #     else:
#     #         l[0].showbalance()
#     #
#     elif ch == 5:
#         print("Thank you")
#         break
#
#     else:
#         print("Invalid choice")
#


# --OOP PRINCIPLES--
#1 CLASS
#    --> definition of structure of its object. it contains properties and operation codes/fn
# 2 OBJECT
#   --> is a member/instance of a class. all the obj of same class have similar properties and operation
# 3 ENCAPSULATION
#  --> binding the properties and functions into a single unit class
# 4 INHERITANCE
# --> deriving attributes(properties/operations) from one class (parent/base/super)into another class(child,derived,sub)
# -->single,multiple,multilevel,hierarchical,hybrid inheritance
# 5 POLYMORPHISM
# --> an entity(method/operator)behaves in diff forms in diff context
# 6 ABSTRACTION
#  --> hiding implementation and show essential details only.

# COMPANY CLASS
#
# class company:
#     def __init__(self):
#         self.company_name=input("enter the company name:")
#         self.location=input("enter loc:")
#     def display_company(self):
#         print("company name:",self.company_name)
#         print("Location:",self.location)
# class employee(company):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("enter id:"))
#         self.empname=input("enter name:")
#         self.salary=int(input("enter salary:"))
#     def display_details(self):
#         super().display_company()
#         print("empid:",self.empid)
#         print("empname:",self.empname)
#         print("salary:",self.salary)
#     def update_salary(self):
#         self.salary=self.salary+(self.salary*0.1)
#         print("updated salary:",self.salary)
# e=employee()
# e.display_details()
# e.update_salary()


# HOSPITAL
# class hospital:
#     def __init__(self):
#         self.host_name=input("enter hostname:")
#         self.location=input("enter location:")
#         self.phone=int(input("enter phoneno:"))
#     def display_hospital(self):
#         print("hostname:",self.host_name)
#         print("Location:",self.location)
#         print("phone_no:",self.phone)
# class department:
#     def __init__(self):
#         self.dept_name=input("enter depname:")
#         self.doctor_name=input("enter docname:")
#     def display_department(self):
#         print("depname:",self.dept_name)
#         print("docname:",self.doctor_name)
# class patient(hospital,department):
#     def __init__(self):
#         hospital.__init__(self)
#         department.__init__(self)
#         self.patient_name=input("enter patient name:")
#         self.age=int(input("enter age:"))
#         self.gender=input("enter gender:")
#         self.phone=int(input("enter phoneno:"))
#         self.admission_date=input("enter admsndate:")
#         self.bed_no=input("enter bedno:")
#         self.discharge_date=" "
#     def set_discharge(self):
#         self.discharge_date=int(input("enter discharge date:"))
#     def full_summary(self):
#         print("\n-- patient summary --")
#         self.display_hospital()
#         self.display_department()
#
#         print("patiet name:",self.patient_name)
#         print("age:",self.age)
#         print("gender:",self.gender)
#         print("phone:",self.phone)
#         print("admsn date",self.admission_date)
#         print("bedno:",self.bed_no)
#         if(self.discharge_date==" "):
#             print("not yer discharged")
#         else:
#             print("discharge date:",self.discharge_date)
# p=patient()
# print("\nHospital Details")
# p.display_hospital()
# print("\ndepartment Details")
# p.display_department()
# print("\nFull Summary")
# p.full_summary()
# p.set_discharge()



class hospital:
    def __init__(self):
        self.host_name = input("Enter hospital name: ")
        self.location = input("Enter location: ")
        self.phone = int(input("Enter phone no: "))

    def display_hospital(self):
        print("Hospital name:", self.host_name)
        print("Location:", self.location)
        print("Phone no:", self.phone)


class department:
    def __init__(self):
        self.dept_name = input("Enter department name: ")
        self.doctor_name = input("Enter doctor name: ")

    def display_department(self):
        print("Department name:", self.dept_name)
        print("Doctor name:", self.doctor_name)


class patient(hospital, department):
    def __init__(self):
        hospital.__init__(self)
        department.__init__(self)

        self.patient_name = input("Enter patient name: ")
        self.age = int(input("Enter age: "))
        self.gender = input("Enter gender: ")
        self.phone = int(input("Enter phone no: "))
        self.admission_date = input("Enter admission date: ")
        self.bed_no = input("Enter bed no: ")
        self.discharge_date = ""

    def set_discharge(self):
        self.discharge_date = input("Enter discharge date: ")

    def full_summary(self):
        print("\n-- Patient Summary --")

        self.display_hospital()
        self.display_department()

        print("Patient name:", self.patient_name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Phone:", self.phone)
        print("Admission date:", self.admission_date)
        print("Bed no:", self.bed_no)

        if self.discharge_date == "":
            print("Not yet discharged")
        else:
            print("Discharge date:", self.discharge_date)


p = patient()

print("\nHospital Details")
p.display_hospital()

print("\nDepartment Details")
p.display_department()

print("\nFull Summary")
p.full_summary()

p.set_discharge()

print("\nUpdated Summary")
p.full_summary()














