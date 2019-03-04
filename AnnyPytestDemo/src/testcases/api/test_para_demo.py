import pytest
from myapp import add

@pytest.mark.parametrize("x,y",[
    (2+4,6),
    (3+9,12),
    (1*2,7)
])
def test_add_by_paras(x,y):
    assert add.add_method(x,y)==x+y



# def test_add_1():
#     assert add.add_method(1,2)==7
