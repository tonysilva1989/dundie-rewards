
from dundie.core import load

def test_load():
    """ Test load function."""
    assert len(load("test/assets/names.csv")) == 2