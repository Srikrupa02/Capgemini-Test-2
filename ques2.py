class BankAccount:
    def __init__(self,bankholder_name,balance):
        self.bankholder_name=bankholder_name
        self.balance=balance
    def deposit(self,amount):
        if amount >0:
            self.balance+=amount
            print(f"The balance amount is :{self.balance}")
    def withdraw(self,amount):
        if amount> self.balance:
            print("There is insufficient balance to withdraw.") 
        elif amount>0 :
            self.balance-=amount
        else:
           print("Invalid withdrawal amount.")
    def show(self):
        print(f"The bank_holder name is:{self.bankholder_name}\n The bank balance is :{self.balance}")
bank_acc=BankAccount("Srii",5000)
bank_acc.deposit(2000)
bank_acc.withdraw(8000)
bank_acc.withdraw(4000)

bank_acc.show()
        
