#Here we will learn about the static classmethod

# Create a class named Calculator 
'''
class Calculator
    add(a, b)   =>  a + b
    sub(a, b)   =>  a - b
    mul(a, b)   =>  a * b
    div(a, b)   =>  a / b
    
    all the above functions should perform the arithmetical operations
    
    it will have a static static method of each of them
    
'''

class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b
        
    @staticmethod   
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod   
    def div(a, b):
        return a / b

x = int(input("Enter 1st no : "))
y = int(input("Enter 2nd no : "))

# To call static method we need not to create an object
print(Calculator.add(x, y))
print(Calculator.mul(x, y))
print(Calculator.sub(x, y))
print(Calculator.div(x, y))