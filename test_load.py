
from dundie.core import load

def test_load():
    """ Test load function."""
    assert len(load("names.csv")) == 2