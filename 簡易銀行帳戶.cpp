class account:
    def __init__ (self,number,name):
        self.number=number
        self.name=name
        self.balance=0
    def deposit(self,amount):
        if amount<=0:
            raise ValueError('must be positive')
        self.balance+=amount
    def withdraw(self,amount):
        if(amount>=self.balance):
            raise RuntimeError('balance not enough')
        self.balance-=amount
