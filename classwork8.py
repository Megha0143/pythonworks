# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
#

class Circle:
    def __init__(self):
        self.radius = float(input("Enter the radius: "))

    def getarea(self):
        area = 3.14*(self.radius**2)
        print("Area of circle:", area)

    def getperimeter(self):
        perimeter = 2 *3.14* self.radius
        print("Perimeter of circle:", perimeter)


c = Circle()
c.getarea()
c.getperimeter()




# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

class Account:
    def __init__(self):
        self.acctnumber = input("Enter account number: ")
        self.acctname = input("Enter account name: ")
        self.balance = float(input("Enter balance: "))

    def withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.balance:
            self.balance = self.balance - amt
            print("Amount withdrawn:", amt)
        else:
            print("Insufficient balance")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def showbalance(self):
        print("Current balance:", self.balance)


a = Account()

a.showbalance()
a.withdraw()
a.showbalance()
a.deposit()
a.showbalance()