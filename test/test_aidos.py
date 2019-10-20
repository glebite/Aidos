"""
test_aidos.py 

"""
import sys
import pytest
sys.path.append('../src')
from aidos import Aidos

@pytest.mark.test_id(1)
def test_aidos_creation():
    aidos_obj = Aidos("test")
    assert aidos_obj is not None

@pytest.mark.test_id(2)
def test_aidos_logging_creation():
    aidos_obj = Aidos("test")
    assert aidos_obj.log is not None

@pytest.mark.test_id(3)
def test_aidos_no_run_name():
    try:
        aidos_obj = Aidos()
        assert False
    except TypeError as raised_exception:
        assert True
        
