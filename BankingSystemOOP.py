# Parent Class
class User():
    def __init__(self,name,age,gender,address) :
      self.name = name
      self.age = age
      self.gender = gender
      self.address = address

    def show_details(self):
        print("Personal details of User:")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)
        print("Address ", self.address)

# Child Class
class Bank(User):
    def __init__(self,name,age,gender,address):
        super().__init__(name,age,gender,address)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $ ", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund | Balance available: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated: $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance has been updated: $", self.balance)

obj=Bank('Sayantika', 22, 'female', 'suri')
obj.show_details()
obj.deposit(10000)
obj.deposit(100)
obj.withdraw(5000)
obj.show_details()
obj.view_balance()
