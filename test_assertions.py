def test_a1():
    assert 4 != 5 #To compare two numbers 

def test_a2():
    assert 234 #to assert some value

def test_a3():
    assert "abcd" == 'adcd' #We can compare the strings 

def test_a4():
    assert ((3-1)*4 /2) == 4.0

def test_a5():
    assert 1 in divmod(9, 5)
    assert 'put' not in 'this is pytest'
    # assert [1,2] in [1, 2, 3, 4] #we can't check the sub List 
    assert 2 in [1, 2, 3] #we can check elements in List
    assert [1, 2] < [1, 2, 4]

def test_a6():
    assert 1

#divmod() operator gives the couple of questiont and remainder
#Unlike Lists, tuples are immutable , we cannot add or delete the elements from the tuple

#It is always preferred to have single assert in pytest, unless something out-of-box


