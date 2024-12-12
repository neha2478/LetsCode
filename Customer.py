'''
Learning Access modifiers :- 

Task :- Create a class Named Customer
    name , phoneno    => Instance variables 
    
    get_name() , get_phoneno() , set_phoneno  => Method names 
'''

class Customer:
    
    #creating an constructor
    def __init__(self, name , phoneno):
        self.name = name
        self.phoneno = phoneno
    
    #Accessor function - getter   
    def get_name(self):
        return self.name
        
    #Accessor function - getter 
    def get_phoneno(self):
        return self.phoneno
        
    #Accessors function - mutators
    def set_phoneno(self, ph):
        self.phoneno = ph
        
#Create an object of Customer class
c1 = Customer('Shruti',5678902340)

print(f'Customer Name is {c1.get_name()} and phone no is {c1.get_phoneno()}')

#who to use mutator fuction - (setter)
c1.set_phoneno(7890123456)

print(f'Customer Name is {c1.get_name()} and phone no is {c1.get_phoneno()}')

    