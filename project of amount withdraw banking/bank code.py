class BankAccount:
    def __init__(self, owner, balance=5000): 
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs {amount} withdrawn successfully.")
            print(f"Remaining Balance: Rs {self.balance}")
        else:
            print("Insufficient balance!")

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: Rs {self.balance}"



account = BankAccount("Ali")


print(account)


try:
    amount = float(input("Enter the amount you want to withdraw: Rs "))
    account.withdraw(amount)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
