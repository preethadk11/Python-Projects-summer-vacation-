class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def showbalance(self):
        print(f'Current Blance:{self.balance}')
    def showdeposit(self,deposit):
        self.balance+=deposit
        print(f'Deposited:{deposit}')
        print(f'Total:{self.balance}')
    def showwithraw(self,withdraw):
        self.balance-=withdraw
        print(f'Withdrawn:{withdraw}')
        print(f'Total:{self.balance}')

a1=bankaccount("Preetha",1000)
a1.showbalance()
a1.showdeposit(500)
a1.showwithraw(200)
