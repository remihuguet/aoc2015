import pytest
import not_quite_lisp

@pytest.fixture(params=[
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3)
])
def case(request):
    return request.param

def test_compute_floor(case):
    assert not_quite_lisp.compute_floor(case[0]) == case[1]

def test_compute_basement():
    assert not_quite_lisp.compute_basement(")") == 1
    assert not_quite_lisp.compute_basement("()())") == 5