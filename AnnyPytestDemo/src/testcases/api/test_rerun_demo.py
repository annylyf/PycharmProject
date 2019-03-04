from myapp import add
import random
import time

def test_rerun_add():
    time.sleep(1)
    assert add.add_method(2,3)==random.randint(2,7)