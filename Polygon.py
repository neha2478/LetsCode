#here we will learn Inheritance, 
'''
Create a class Name Polygon and Triangle
Takes ns - integer type
sides = [5,7,9,19,67] take either tuple/list as input for sides 

class Polygon
    no_of_sides
    sides = [5,7,8,19] /or (5,7,8,19) - generally we may take tuple as it will not change its size
    
class Triangle:
    area()


how constructors work in this...
class Polygon:
    def __init__(self, ns, *sides):

class Triangle:
    def __init__(self, ns, *sides):
        Polygon __init__(ns, *sides)
        
    def area()
    
Formula :  a=10, b=15, c=9
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        
a, b, c will be getting values from *sides - list/tuple
'''

#Code
import math

class Polygon:
    def __init__(self, ns, *sides):
        self.ns = ns
        self.sides = sides
        
#Inheriting the Polygon class
class Triangle(Polygon):
    def __init__(self, ns, *sides):
        #base class's constructor is called class_name.__init__(...)
        #we need to pass self also...instance variable
        Polygon.__init__(self, ns, *sides)
        
    def area(self): 
        x, y, z = self.sides #destructuring the List
        s = (x + y + z) / 2
        area = math.sqrt(s * (s - x) * (s - y) * (s - z))
        
        return area

# class Square(Polygon):
#     def __init__(self, ns, *sides):
#         Polygon.__init__(self, ns, *sides)
        
#     def area(self):
#         a = self.sides
#         area =math.pow(a , 2)
        
#creating the object ,*sides  ca take multiple input as to no_of_sides - ns
a = Triangle(3, 6, 4, 5)
print(f'The area of Triangle is {a.area()}') #calling the area() of Triangle

# a2 = Square(4,3,3,3,3)
# print(a2.area())