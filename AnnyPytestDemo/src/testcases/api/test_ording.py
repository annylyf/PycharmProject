import pytest
import time

value=0
@pytest.mark.run(order=2)
def test_add2():
    print("I am 2")
    time.sleep(2)

    assert value ==10


@pytest.mark.run(order=1)
def test_add1():
    print("I am 1")
    # global value
    value = 10
    assert value == 10