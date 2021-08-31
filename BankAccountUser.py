class User:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(interest_rate = 0.02, balance = 0)

    def makeDeposit(self, amount):
        self.account.makeDeposit(amount)
        print(f"Depositing {amount} dollars into account: {self.name}")
        return self
    
    def makeWithdrawal(self, amount):
        self.account.makeWithdrawal(amount)
        print(f"Withdrawing {amount} dollars from account: {self.name}")
        return self

    def displayBalance(self):
        self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
    
    def makeDeposit(self, amount):
        self.balance += amount
        return self
    
    def makeWithdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Your balance is: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

Jake = User("Jake")
Jake.makeDeposit(100)
Jake.makeWithdrawal(50)
Jake.displayBalance()