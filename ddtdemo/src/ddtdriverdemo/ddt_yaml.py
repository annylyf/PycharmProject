import unittest
import ddt
from ddtdriverdemo.calculate import add

@ddt.ddt
class TestDDTDemo(unittest.TestCase):

    @ddt.file_data("test_data.yaml")
    def test_demo1(self,x,y,expect_result):
        self.assertEqual(add(x,y),expect_result)