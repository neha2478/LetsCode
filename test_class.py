#Lecture -Test Class - 15 Lecture
# object constructor or a "blueprint" for creating objects
#object contains both data (variables, called attributes) and code (functions , called methods).

#Now lets write a Test 

#here self is not a keyword but  a instance of the class

class TestMyStuff():
    def test_type(self):
        assert type(1.3) == int


    #Let us create method for setting the strings
    def test_strs(self):
        assert str.upper('shruti') == 'SHRUTi'
        assert 'pytest'.capitalize() == 'pytest'