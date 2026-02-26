class BankAccount:

    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Account is creadited . New Balance is : {self.balance}") 

    def withdraw(self,withdrawing_amount):
        self.balance -= withdrawing_amount
        print(f"Account is debited remenig balance : {self.balance}")

    def cheak_balance(self):
        print("The Account balance Rs :",self.balance) 

acc1 = BankAccount(5749,"dhanraj",22_000)
acc1.deposit(10_000)
acc1.cheak_balance()                 
acc1.withdraw(500)