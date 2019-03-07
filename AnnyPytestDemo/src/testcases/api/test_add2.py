import pytest
import time
import allure

from testcases.testapp import add2
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


@allure.feature("测试成功的用例")
def test_add1():
    assert add2.add_method2(2, 3) == 5

@allure.feature("测试失败的用例")
def test_add2():
    print("I am 2")
    time.sleep(3)
    pytest.assume(add2.add_method2(1.2,3.1) == 5.3)
    print("I want to go")
    pytest.assume(add2.add_method2(1, 2) == 3)

#多个asset
# assert  add2.add_method2(1.2,-0.9)==0.3
# assert  add2.add_method2(1,2)==3

    # assert add2.add_method2[(1, 2),(1.2,-0.9)] == [3,0.3]

# assert add2.add_method2(1.2,3.1)==5.3