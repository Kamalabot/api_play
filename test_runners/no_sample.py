#This is the sample testing file
from .simple_execution import *
import pytest

def test_cuber():
    print('testing cuber')
    assert cuber(3) == 27

def test_incrementor():
    print('testing incrementor')
    assert incrementor(5, 10) == 50

@pytest.mark.parametrize("x, y, z",[
    (5, 10, 50),
    (15, 30, 450),
    (25,86,2105)
    ])
def test_params(x,y,z):
    print(f'{x} and {y}')
    assert incrementor(x, y) == z

@pytest.fixture
def full_charge():
    return Smartphone(100,100) 

@pytest.fixture
def half_charge():
    return Smartphone(50,100)

@pytest.fixture
def half_bright():
    return Smartphone(50,50)

@pytest.mark.parametrize("chg,bright",[
    (100,100),
    (50,100),
    (50,50)
    ])
def test_phone(full_charge,chg,bright):
    assert full_charge.charge == chg
    assert full_charge.brightness == bright

@pytest.mark.parametrize("chg,bright",[
    (100,100),
    (50,100),
    (50,50)
    ])
def test_charge(half_charge,chg,bright):
    assert half_charge.charge == chg
    assert half_charge.brightness == bright

@pytest.mark.parametrize("chg,bright",[
    (100,100),
    (50,100),
    (50,50)
    ])
def test_bright(half_bright,chg,bright):
    assert half_bright.charge == chg
    assert half_bright.brightness == bright

