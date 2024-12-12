#Create a Class Name Account
'''
class Account
    name
    account_number
    balance
    
    deposite()
    withdraw()
    show_details()
    
    AccNumber
    
    After withdrawl the minimum balance shouldn't fall 
    below 1000 , 
    if it fall's below 1000 than it shows error
    
    MinimumBalanceError
    
    AccNumber is automatically assigned by this class Account , for that we need to maintain a static/cclass
    variable to do that.
'''

#code

#this class is inheriting Exception class
class MinimumBalanceError(Exception):
    pass

#Account class
class Account:
    
    AccountNo = 1001

    #constructor
    def __init__(self, name, balance =1000):
        
        if(balance < 1000):
            raise MinimumBalanceError('Account cannot be Created!!')
        
        self.name = name
        self.balance = balance
        #the account_number should be assigned by account account_number
        self.acc_number = self.AccountNo
        self.AccountNo += 1
        
    def deposite(self, amount):
        self.balance += amount
        
        
    def withdrwal(self, amount):
        if self.balance - amount < 1000:
            raise MinimumBalanceError('Amount cannot be withdrawl!!')
        else:
            self.balance = self.balance - amount
            
    def show_detailes(self):
        print(f'Account Number is {self.acc_number}')
        print(f'Name is {self.name}')
        print(f'Balance is {self.balance}')


#creating an Object

a1 = Account('Shruti', 2000)
a1.show_detailes()
print(a1.deposite(200))
print(a1.withdrwal(300))

print('')

a2 = Account('Shruti', 2000)
a2.withdrwal(1500)
a2.show_detailes()
