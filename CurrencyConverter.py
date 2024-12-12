#Create a class named Currency Converter
'''
class CurrencyConverter
        currency
        rate
        set_currency()
        get_currency()
        set_rate()
        get_rate()
        convert( amount )

formula :-

    amt = 100 
    
    USD          INR
        
        rate = 70      
        
    cc = CurrencyConverter('USD', 70)
    cc.set_currency('AUD') 
    cc.set_rate(50)     
'''

class CurrencyConverter:
    
    def __init__(self, currency , rate):
        self.currency = currency
        self.rate = rate
        
    def get_currency(self):
        return self.currency
    
    def set_currency(self, name):
        self.currency = name
    
    def get_rat(self):
        return self.rate
    
    def set_rate(self, rate):
        self.rate = rate

    def convert(self , amt):
        #formula
        return self.currency + ' conversion is ' + str(self.rate * amt)
    
#creating an object of Class to access the func, mutators and Accessor
cc = CurrencyConverter('USD' , 70)
print(cc.convert(200))
print(cc.get_currency())
print(cc.get_rat())
print(id(cc))

cc.set_currency('AUD')
cc.set_rate(80)
print(f'The Currency conversion is {cc.convert(60000)}')