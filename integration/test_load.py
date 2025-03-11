import pytest
from subprocess import check_output, CalledProcessError


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_load_call_function():
    """test command load"""
    out = check_output(
        ["dundie", "load", "tests/assets/names.csv"]
    ).decode("utf-8").split("\n")
    assert len(out) == 2


# Testing one possible unhappy path
@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command",["loady","carrega","salva","testa"])
def test_load_negative_call_load_with_wrong_params(wrong_command):
    """test command loady (wrong parameter)"""
    with pytest.raises(CalledProcessError) as error:
        check_output(
            ["dundie", wrong_command, "tests/assets/names.csv"]
        ).decode("utf-8").split("\n")
        assert "status 2" in str(error.getrepr()) 
