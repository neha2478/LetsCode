#---------------------Understanding Random Numbers and Lists--------------------------------------

#Random module is a python module
'''
import random 

#randint() - It provides random integer value , takes two parameters a: and b" (start and end point)
rand_integer = random.randint(1, 100)
print(rand_integer)
'''

'''
    Module - A Python module is a file containing Python definitions and statements.
            A module can define functions, classes, and variables. A module can also include runnable code.

            Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.
'''

#Task
# import random
# import my_module

# print(my_module.my_favorite_number)

#To print the floating number


import random
random_number_0_to_1 = random.random() 
print(random_number_0_to_1)


#here first random - module , random() - is function of random
# To round the floating no 

# we can use the round() - To give a round off value

'''
a = round(random_number_0_to_1)
print(a)
'''

#No parameters
'''
The random.random () function generates random floating numbers in the range of 0.1, and 1.0. 
It takes no parameters and returns values uniformly distributed between 0 and 1.
'''
'''
import random
random_random_0_to_1 = random.random() * 10
print(random_random_0_to_1)
'''

#Uniform() will return a random floating no 
# random.uniform(a, b)
'''
import random
random_float = random.uniform(1, 10)
print(random_float)
'''

#Print heads or Tails ...
#Task
'''
print(Heads)
print(Tails)
'''

#Solution
'''
import random 
random_heads_or_tails = random.randint(0,1)
print(f"The number is {random_heads_or_tails}")
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
'''

#-------------------Understanding the Offset and Appending Items to Lists-------------------

# -----------LISTS--------------------

#Creating a List Data Structure
import random
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Las Vegas", "New York", "Orlando", "Denver", "Washington D.C", "Phoenix", "Cambridge"]
# print(states_of_america[0])
# print(states_of_america[7])
# print(states_of_america[5])
# print(states_of_america)

'''
#Use of For Loop
for e in states_of_america:
    print(e , end = " , ")

for i in range(len(states_of_america)):
    print(i)

for i in range(0, len(states_of_america)):
    val = states_of_america[i]
    print(i, val)

#Another way to do this using the  enumerate 

for i, val in enumerate(states_of_america, start = 1):
    print(i, val)
'''

#We can change the value of List
'''
states_of_america[1] = "Pecilvania"
print(states_of_america)
'''
#Appending a new value to the List
'''
states_of_america.append("Angelaland")
print(states_of_america)
'''

# states_of_america.extend("India")
# print(states_of_america)

#Wrong method
# for i in range(0, len(states_of_america)-1):
#     if i == len(states_of_america)-1:
#         states_of_america.remove(len(states_of_america)-1)

#     # if  i == len(states_of_america)-2:
#     #     states_of_america.remove(len(states_of_america)-2)
# print(states_of_america)

#Using of remove :-
'''
states_of_america.remove("New Jersey")
print(states_of_america)
'''
#Using sort() in Lists :-
'''
states_of_america.sort()
print(states_of_america)

#Using the Arguments of List 
states_of_america.sort(reverse=True)
print(states_of_america)

#Creating  a new List
# Sort the list by the length of the values:
def myFun(e):
    return len(e)

a = ["Cat", "dog", "duck", "bird", "squirrel"]

a.sort(reverse= True, key=myFun)

print(a)

#Another Example:-
def myFun(e):
    return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFun)

print(cars)
'''


#TASK 33 - 3rd video of Day 4
# ---------------WHO WILL PAY BILL?---------------------------
'''
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1 Option to do so...
print(random.choices(friends))
#   random.choices(List_name) - Hence it will help to chose a random element from List 

#2nd Option :-
#random.randint() - We have used this to fetch random integer no of List
random_index = random.randint(0, len(friends)-1)
print(friends[random_index])
'''

#Lesion 5 - Index Error and working with Nested Lists:-
'''
states_of_america = ["Alabama","Alaska","Arizona","Arkansas","California", "Colorado","Connecticut","Delaware"]
length_of_list = len(states_of_america)
print(f'The Length of the List : {length_of_list}') #Using theFormat Specifier

#here getting the last element of the List
print(f'The Last Element of List : {states_of_america[length_of_list - 1]}')
print(f'The Last Element of List : {states_of_america[length_of_list - 3]}')
print(f'The Last Element of List : {states_of_america[length_of_list - 4]}')

#Here contacting Two List in one List 
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = fruits + vegetables

print(dirty_dozen) # Ans - ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

#Here List inside a List
dirty_dozen_two = [fruits, vegetables]
print(dirty_dozen_two)
# Output :- [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']] 
print(dirty_dozen_two[1][3]) #O/P :- Celery
print(dirty_dozen_two[0][4]) #O/P :- Peaches
'''