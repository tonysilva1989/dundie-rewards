
from dundie.core import load

def test_load():
    """ Test load function."""
    assert len(load("tests/assets/names.csv")) == 2