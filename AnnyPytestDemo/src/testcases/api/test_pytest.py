#coding=utf-8

from myapp import add
import time
import random

def test_add():
    time.sleep(random.randint(2, 7))
    assert add.add_method(10,2)==12

def test_add2():
    time.sleep(random.randint(1,7))
    assert add.add_method(10,2) ==13