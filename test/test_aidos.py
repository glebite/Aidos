"""
test_aidos.py 

"""
import sys
import pytest
sys.path.append('../src')
from aidos import Aidos

@pytest.mark.test_id(1)
def test_aidos_creation():
    aidos_obj = Aidos()
    assert aidos_obj is not None
