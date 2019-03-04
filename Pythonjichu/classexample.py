#coding=utf-8
class Person:

        def __init__(self):
            print("Init the class")
            self.age=''
            self.province=''
            self.name=''

        def set_profile(self,age,province,name):
            self.age = age
            self.province = province
            self.name = name

        def get_profile(self,name):
            return self.age,self.province


if __name__=="__main__":
    jiguang = Person()
    jiguang.set_profile(18,'深圳','anny')
    print(jiguang.get_profile('anny'))




