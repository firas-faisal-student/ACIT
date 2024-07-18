wamt=0
damt=0
function=10
data=0
x="yes"

class Bankofmdv:
    def __init__(self, name, NaID):
        self.name = name
        self.NaID = NaID
    def basic_info(self):
        print("all of your basic information", "your name is: ", self.name, "your National ID is: ", self.NaID)
# this is the main class 

class emp(Bankofmdv):
    def __init__(self, name, NaID, empID, salary):
        super().__init__(name, NaID)
        self.salary = int(salary)
        self.empID = empID
# this is the subclass named "emp" short for employee, this has a super class from the parent class (Bankofmdv)
    def empcheck(self):
        print("Name=", self.name, "your employee ID is=", self.empID, "and your current monthly salary is:", self.salary)
#the function to check the employee information

class customer(Bankofmdv):
    def __init__(self, name, NaID, Cs_ID, Balance):
        super().__init__(name, NaID)
        self.Cs_ID = Cs_ID
        (self.Balance) = Balance
#this is the customer information which also has the superclass of the parent function (Bankofmdv),
#the extra information stored here is the C_ID and the balance of ther customer

    def balcheck(self):
        print("your currrent balance is: ", self.Balance)
    def deposit(self):
        damt = input("please enter the amount you wish to deposit ")
        self.Balance += int(damt)
        print("your current balance is:", self.Balance)
        damt=0
    def withdraw(self):
        wamt = input("please enter the amount you wish to withdraw ")
        if int(wamt)>= self.Balance:
            print("Insufficient Funds")
            wamt=0
        else:
            self.Balance-= wamt
            print("succsessfully withdrawn amount")
            print("your remaining balance is: ", self.Balance)
#above are the functions of the customer which is self explanatory from their respective names
emp1 = emp("jone","A897933","emp1", 20000)
emp2 = emp("Numair","A456215","emp2", 15000)

cus1 = customer("Tahufeeq","A546886","Cus1",50)
cus2 = customer("Ahlam","A465545","Cus2",150)

data = input("Welcome to Bank Of Maldives! Please enter your Bank ID ")
while function != 0:
    
    function = input(""" please enter what you would like to do!
    enter 0 to exit the program!
    enter 1 for employee status checking
    enter 2 for Customer balance checking
    enter 3 for customer depositing
    enter 4 for withdrawal from account! 
    """)
    if function == "1":
        if data == "emp1":
            emp1.empcheck()
        elif data == "emp2":
            emp2.empcheck()
    elif function == "2":
        if data =="cus1":
            cus1.balcheck()
        elif data =="cus2":
            cus2.balcheck()

    elif function == "3":
        if data =="cus1":
            cus1.deposit()
        elif data =="cus2":
            cus2.deposit()

    elif function == "4":
        if data =="cus1":
            cus1.withdraw()
        elif data =="cus2":
            cus2.withdraw()
    elif function == "0":
        print("goodbye")
    else:
        print("wrong function")




