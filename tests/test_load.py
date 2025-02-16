
import pytest
from dundie.core import load
from .constants import PEOPLE_CSV


def setup_module():
    print()
    print("Run before the tests from this module",end="\n")

def teardown_module():
    print()
    print("Run after the tests from this module",end="\n")

@pytest.fixture(scope="function",autouse=True)
def create_new_file(tmpdir):
    tmpdir.join("new_file.txt").write("This is just garbage text...")

@pytest.mark.unit
@pytest.mark.high
def test_load(create_new_file):
    """ Test load function."""
    assert len(load(PEOPLE_CSV)) == 2
    assert load(PEOPLE_CSV)[0][0] =='T'


@pytest.mark.unit
@pytest.mark.medium
def test_load():
    """ Test load function."""
    assert len(load(PEOPLE_CSV)) == 2
    assert load(PEOPLE_CSV)[0][0] =='T'