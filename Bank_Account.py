class BankAccount:
    def __init__(self, curr_balance):
        self.curr_balance = curr_balance

    def deposit(self, other):
        self.curr_balance += other

    def withdraw(self,other):
        self.curr_balance -= other

    def balance_inquiry(self):
        print('Your current balance is:', self.curr_balance)

bank_account = BankAccount(1000)

bank_account.deposit(200)
bank_account.withdraw(300)
bank_account.balance_inquiry()