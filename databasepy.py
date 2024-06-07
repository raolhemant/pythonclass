#check blance 
#withdraw
#balance deposits
#exit


# class ATM():
#     def check_balance():
#         balance = 0

a = '''
1=check balane
2=cash deposits
3=cash withdraw
'''
print(a)
balance = 0
while True:
    choice = int(input("Enter a number"))
    if choice == 1:
        print(f'current balane {balance}')
    elif choice == 2:
        b = int(input("how much you  want to deposits"))
        if b < 0:
            print("Amount should be in positive")
            break
        balance = balance + b
    elif choice == 3:
        c = int(input("Enter the Amount you want withdraw"))
        if c > balance:
            print("insufficent balance")
            break
        balance = balance - c

class ATM():
    balance = 0
    def __init__(self,a,b) -> None:
        self.balance = 0
        self.a = '''
            1.check balane
            2.cash deposits
            3.cash withdraw
            '''
    def check_balance(self):
        if self.b == 0:
            return f'current balance {self.balance}'
    def deposits(self):
        self.b = int(input("how much you  want to deposits"))
        if self.b < 0:
            print("Amount should be in positive")
        balance = balance + self.b
    def withdraw(self):
        c = int(input("Enter the Amount you want withdraw"))
        if c > balance:
            print("insufficent balance")
        balance = balance - c

    def exit(self):


            

         


        
