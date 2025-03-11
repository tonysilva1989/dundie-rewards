import pytest


MARKER= """\
unit: Mark unit tests
integration: Mark integration tests
high: High priority
medium: Medium priority
low: Low priority
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers',line)


# fixed data to populate the tests
# all tests will use this fixture
@pytest.fixture(autouse=True)
def go_to_tmpdir(request): #dependecy injection
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield # Generator protocol
    
