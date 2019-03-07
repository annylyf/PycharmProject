from myapp import paixu
import pytest

@pytest.mark.parametrize("before, bubble", [
    ([2, 3, 4, 5, 6], [2, 3, 4, 5, 6]),

    ([2, 3, 4, 5, 6],None),

    ([2, 3, 4, 5, 6],10)


])
def test_practice(before, bubble):
    assert paixu.bubble_sort(before) == bubble



