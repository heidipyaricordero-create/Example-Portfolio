#test_sample add
from sample import add

def test_add():
    assert  add (3,3) == 6
    assert add (2,4) != 3
    
def test_string():
    assert "Pytest" in "Hello Pytest!"

def test_boolean():
    assert True is True