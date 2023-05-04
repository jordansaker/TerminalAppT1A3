import pytest
from file_handling import file_handler

# check pytest
def test_basic():
    assert 'hello' == 'hello'

# test function for no input arguments
def test_No_Arguments():
    with pytest.raises(Exception):
        file_handler()

# test function for when incorrect file name is provided on file read
# should fail the raises test as exception is caught in function
def test_Filename_Error_Raised():
    with pytest.raises(FileNotFoundError):
        file_handler('ErrorTest.txt', '.txt', '', 'r')
# should pass the assertion test
def test_Filename_Error_Assert():
    assert file_handler('ErrorTest.txt', '.txt', '', 'r') != type(FileNotFoundError)