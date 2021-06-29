# Test case/method  shoud start/end with keyword test
#If the file name is started with test keyword, while running in terminal use only py.test then under that package all the files with keyword starting from 'test' wil be executed
# if file name is not started with test, in terminal use pytest -v -s file.py.. -v indicates more output ....-s indicates print the output
#py.test -k basic -v   here -k indicates group of file i.e all file name with basic keyword will be excuted

import pytest

def test_m1():
    a=5
    b=20
    assert a*4==b

def test_m2():
    assert True

def test_m3():
    assert  False

def test_m4():
    assert 'uma'=='UMA'

def test_m5():
    a=10
    b=20
    assert a==b

def test_m6():
    assert 'python'.upper()=='PYTHON'
