

# 第一步：导入unittest包

import unittest

def add(x,y):
    return x+y


# 第二步：类名继承testcase
class Demo(unittest.TestCase):

#测试用例执行之前先执行setUp
    def setUp(self):
        print("I am set up")


#测试方法以"test_"开头

    def test_demo(self):
        print("my first unit test demo")
        self.assertEqual(add(19,1),11,"asser equal")

    def test_demo2(self):
        print("my first unit test demo")
        self.assertEqual(add(10,1),11,"asser equal in demo2")

#测试用例执行之后执行tearDown
    def tearDown(self):
        print("I am tear down")


