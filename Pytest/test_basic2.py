#py.test -m dem here -m indicates that the marked tests(@pytest.mark.dem) only will be executed


import pytest

@pytest.mark.dem
def test_m1():
    a=5
    b=20
    assert a*4==b

def test_m2():
    assert True

@pytest.mark.dem
def test_m3():
    assert  False

@pytest.mark.dem
def test_m4():
    assert 'uma'=='UMA'

def test_m5():
    a=10
    b=20
    assert a==b

def test_m6():
    assert 'python'.upper()=='UPPER'
