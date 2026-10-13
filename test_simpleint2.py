from simpleint2 import simpInt

def test_simInt_positive():
    assert simpInt(20000, 8, 12) == 1920

def test_simInt_zero():
    assert simpInt(10000, 7, 0) == 0 