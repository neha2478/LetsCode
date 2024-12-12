#Here we will Learn to create a class 

#class Utilities :-
'''
Class is created with a name called class keyword
eg :-
class Car:

To keep a name for the class we always use Pascal Case.
Class is a blue print of an Object 

If we dont want to write something in class / function , want to keep it empty we 
just write 'pass keyword'

Types of Cases are...

PascalCase   camelCase  snake_case

PascalCase :- Is used for the Class name 
snake_case :- It is used for everything else
'''
'''
class User:
    #We can create an attribute using the __init__()
    #It is an constructor which is itself called 
    def __init__(self):
        print("New user being created!!")
        # self.id = id
        # self.username = username


#creating an Object 
user_1 = User()
user_1.id = "001"
user_1.username = "Sana"

print(user_1.username)
print(user_1.id)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Neha"
'''

"""
Constructor :- It is a part of Blue print which is used to initialize when an object is being initialized 
initialize :-To set values , counter , switches etc. to the variable.
__init__() :- It is the special function , It is used to initialize the attributes.
"""

#Another way to pass attributes to the parameter itself.
class User:

    def __init__(self, id, username):
        print("The new user created !!")
        self.id = id 
        self.username = username


#creating an object 
user_1 = User("001", "Sanjana") # here we can directly pass those to arguments 
print(f"The new user ID is :{user_1.id}, The User name : {user_1.username}")

user_2 = User("OO2", "Shorya")
print(f"The new user ID : {user_2.id}, The username : {user_2.username}")