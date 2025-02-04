
import pytest
from dundie.core import load
from .constants import PEOPLE_CSV

@pytest.mark.unit
@pytest.mark.high
def test_load():
    """ Test load function."""
    assert len(load(PEOPLE_CSV)) == 2
    assert load(PEOPLE_CSV)[0][0] =='T'