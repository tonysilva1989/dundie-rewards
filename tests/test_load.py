
from dundie.core import load
from .constants import PEOPLE_CSV


def test_load():
    """ Test load function."""
    assert len(load(PEOPLE_CSV)) == 2