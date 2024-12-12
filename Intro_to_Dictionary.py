#Here we will learn about the Dictionaries...

student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Physics", "Chemistry"],
    "grades": {"Math": 90, "Physics": 85, "Chemistry": 95}
}

#Another way to print keys and values using for Loop
'''
for index in student:
    print(student[index])
'''

# for keys, values in student.items():
#     print(keys)
#     print(values)

# print("-------------------Another way----------------------------")
'''
for keys, values in student.items():
    # print(f"The key - {keys} : The value - {values}")
    print(f"The key is {keys}")
    print(f"The value is {values}")
'''

# To add values to the dictionary
'''
student["school_name"] = "K.V.Panagarh"
student["name_of_student"] = "Rohan"
# print(student)

#Editing the values in dictionary :-
student["name_of_student"] = "Shyam"
print(student)
'''
# print("----------------------------Another keys and values of Dict way---------------------------")
'''
for things in student:
    print(things) #This only printing keys 
'''
'''
for keys in student:
    print(keys) #This will print the keys
    print(student[keys]) #This will print values of respective keys 
'''

'''
programming_dictionary = {"Apple": "Red", "Banana": "Yellow", "Guava": "Green", "Chikoo": "Brown"}
#printing Keys using keys()
print(list(programming_dictionary.keys()))
#printing Values using value()
print(list(programming_dictionary.values()))
print(programming_dictionary["Apple"])
print(programming_dictionary["Banana"])
print(programming_dictionary["Chikoo"])
print(programming_dictionary["Guava"])
'''


#To create an empty dictionary 

# empty_dictionary = {}

# dict = {}
# print(dict)


#-----------------------Creating a list inside a Dictionaries--------------------------------
#Lecture - 69 ----------------------NESTING LIST INSIDE DICTIONARY-----------------------------------

#Normal Dictionary
"""
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
"""

#Nested List in Dictionary
'''
travel_blog = {
    "France": ["paris", "Little", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_blog)
'''

# Example of Nested List :-
'''
nested_List = ["A", "B", ["C", "D", "E", ["F", " G", "H"], "I", ["J", "K"]], "L", "M"]
print(nested_List[1])
print(nested_List[2])
print(nested_List[2][3])
print(nested_List[2][2])
print(nested_List[3])
print(nested_List[2][4])
print(nested_List[2][5][1])
print(nested_List[2][5])
'''

#Here merging the Lists and Dictionary
#---------------Nested Dictionary--------------------

travel_log = {
    "France":{
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5
    },
    "India": {
        "cities_visited": ["Mumbai", "Candigarh", "Bengeluru", "Kerala", "Kolkata", "Delhi"],
        "total_visits" : 7
    }
}

print(travel_log)
print(list(travel_log.keys()))
print(travel_log["India"]["cities_visited"])

for i in range(0, len(travel_log["India"]["cities_visited"])):
    print(travel_log["India"]["cities_visited"][i])

print("The total visited places in India : {}".format(travel_log["India"]["total_visits"]))

