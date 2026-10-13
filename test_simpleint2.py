from simpleint2 import simpInt

def test_simpInt_positive():
    assert simpInt(20000, 8, 12) == 1920

def test_simpInt_zero():
    assert simpInt(10000, 7, 0) == 0 