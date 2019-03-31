#! /usr/bin/env python
#coding=utf-8
import logging
from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_cfg

class DeptManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department management API")
        self.create_dep_url = sys_cfg.get('contact_para','create_dep_url')
        self.dep_secure = sys_cfg.get('contact_para','secure')


    def create_dept(self):
        new_part={
       "name": "Anny+20190331",
       "parentid": 1,
       "order": 1
        }

        param = {'access_token':self.get_token(self.dep_secure)}
        logging.debug("url:"+str(self.create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_dep_url,new_part,params=param)

    def get_create_dept_res(self):
        return self.get_response()
