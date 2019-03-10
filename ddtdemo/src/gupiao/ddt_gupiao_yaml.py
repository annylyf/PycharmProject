#! /usr/bin/env python
#coding=utf-8

import unittest
import ddt
import requests

def get_gupiao_name(gupiao):
    responese = requests.get('http://hq.sinajs.cn/list='+gupiao)
    gupiao_text = responese.text
    print(gupiao_text)
    gupiao_name = gupiao_text[gupiao_text.find('"')+1,gupiao_text.find(',')]
    print("a=1")
    # gupiao_name = gupiao_text.find('"')
    print(gupiao_name)
    return gupiao_name



@ddt.ddt
class TestDDTDemo(unittest.TestCase):

    @ddt.file_data("test_data.yaml")
    def test_demo1(self,gupiao_name,expect_result):
        self.assertEqual(get_gupiao_name(gupiao_name),expect_result)