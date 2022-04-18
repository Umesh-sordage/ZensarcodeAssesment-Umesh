class Account:
    def __init__(self, balance=0.0, name=''):
        self.balance = balance
        self.name = name
        self.nominee = None

    def Deposit(self, balance=0.0):
        self.balance = self.balance + balance
        print("Deposite is succesfull and the balance in account is %f" % self.balance)

    def Withdrawal(self, balance=0.0):
        if (self.balance >= balance):

            self.balance = self.balance - balance
            print("The withdraw is successfull and balance is %f" % self.balance)

        else:
            print("Insufficient balance")

    def AddNominee(self, name=''):
        self.nominee = name
        print(self.nominee)
