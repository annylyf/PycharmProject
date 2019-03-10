import unittest
import ddt
from ddtdriverdemo.calculate import add

@ddt.ddt
class TestDDTDemo(unittest.TestCase):

    @ddt.data((2,2))
    @ddt.unpack
    def test_demo1(self, x,y):
        self.assertEqual(add(x,y), 4)

#使用字典方式传数据
        @ddt.data({"x":20,"y":10})
        @ddt.unpack
        def test_demo2(self, x, y):
            self.assertEqual(add(x, y), 30)