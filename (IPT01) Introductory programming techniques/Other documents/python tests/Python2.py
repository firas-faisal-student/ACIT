class user:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    def Call_user(self, name):
        print(f"user name is {self.name}")

student1 = user("bob", "001", 25)

print(student1.name)

print(student1.Call_user("bob"))

class bankacc(user):
    def __init__(self, name, id, age, amount):
        super().__init__(name, id, age)
        self.amount = amount
    def deposit(amount):
        print(f"{amount},amount deposited")
bobaccount = bankacc("bob","002",25,0)
print(bobaccount.deposit())

        