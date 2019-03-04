import pytest
from myapp import add

@pytest.mark.parametrize("x,y",[
    (6,6),
    (9,12),
    (10,7)
])
def test_add_by_paras(x,y):
    assert add.add_method(x,y)==x+y



# def test_add_1():
#     assert add.add_method(1,2)==7
