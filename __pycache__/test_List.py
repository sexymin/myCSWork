import unittest
import Target01 as t01

def test_L1():
    result = t01.returnList((11),(12),13)
    assert type(result) == list
def test_L2():
    result = t01.returnList(11,12,13)
    assert type(result) == list
def test_L3():   
    result = t01.returnList([11],12,13)
    assert type(result) == list
def test_L4():
    result = t01.returnList([11,12,13])
    assert type(result) == list
def test_L5():
    result = t01.returnList([11],(12),13)
    assert type(result) == list
def test_L6():
    result = t01.returnList((11),(12),13)
    assert type(result) == list
