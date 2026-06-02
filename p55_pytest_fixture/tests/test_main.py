from app.main import add, divide
import pytest


# fixture used to set dynamic data
@pytest.fixture()
def setup_data():
    return {"a":10, "b":5}

def test_add_with_fixture(setup_data):
    assert add(setup_data['a'], setup_data['b']) == 15


#here ("a,b,expected",[(2,3,5)]) it means 2 assign on a, 3 assign on b, expected value is 5
@pytest.mark.parametrize("a,b,expected",[(2,3,5), (-1,1,0), (0,0,0)])
def test_add_parameters(a, b, expected):
    assert add(a, b) == expected


# if you want to skip some test or write test case after some time later
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass