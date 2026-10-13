from simpleint2 import simInt

def test_simInt_positive():
    assert simInt(20000, 8, 12) == 1920

def test_simInt_zero():
    assert simInt(10000, 7, 0) == 0 