#here we will write a code 

# import pytest 
from src.is_alphabet import is_alphabet

def test_is_alphabet():
    """
        Test the function "is_alphabet" taking alphabet and returning True.
    """
    #arrange
    text = "ffiH"
    expected_result = True

    #act
    actual_result = is_alphabet
    #assert
    assert actual_result == expected_result

# pytest.mark.parameter("test", ["&&", " ", "fdk f8","llj.", ""])
def test_is_not_alphabet(text):
    """
        Test the function "is_alphabet" taking non-alphabet characters 
        and returning False.

        Args:
            text (string): non-alphabet string
    """

    #arrange
    expected_result = False
    #act
    actual_result = is_alphabet(text)
    #assert
    assert actual_result == expected_result

# def test_is_alphabet_input_integer():
#     """
#         Function "is_alphabet" should gracefully handle an integer as input
#     """

#     #arrange





