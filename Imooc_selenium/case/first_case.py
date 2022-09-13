
#import sys  
#sys.path.append(’需要引用模块的地址')
# sys.path.append("..")   # 这代表添加当前路径的上一级目录

#coding = utf-8

import code
import email
import sys
from unicodedata import name
import unittest
from unittest import suite
sys.path.append('F:/selenium_python/Imooc_selenium')
from selenium import webdriver
from business.register_business import RegisterBusiness
import HTMLTestRunner
import os
import unittest
import time
from log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        print('所有case执行之后的后置')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info("this is chrome")
        self.register = RegisterBusiness(self.driver)
        

    def tearDown(self):
        time.sleep(3)
        for method_name,error in self._outcome.errors:                        # TearDown 中捕获错误信息：for method_name,error in self._outcome.errors （self._outcome.errors返回list）
            if error:
                case_name = self._testMethodName                              # 根据当前动态的类名和方法名来获取
                self.driver.save_screenshot(os.path.join(os.getcwd(),"report",case_name+".png"))
        self.driver.close()
        
        

    def test_register_emali_error(self):
        email_error = self.register.register_email_error('1111qq.com','111name','111',code)
        # 通过if判断
        # if email_error == True:
        #     print("注册成功了，此条case失败")

        #通过assert判断是否为error
        self.assertTrue(email_error,"邮箱错误，case执行register_email_error用例")

    def test_register_username_error(self):
        username_error = self.register.register_name_error('2222qq.com','222name','111','testcode')
        self.assertFalse(username_error,"case执行")

    def test_register_password_error(self):
        password_error = self.register.register_password_error('3@qq.com','333name','111','testcode')
        self.assertFalse(password_error)
        

    def test_register_code_error(self):
        code_error = self.register.register_code_error('4@qq.com','444name','111','testcode')
        self.assertFalse(code_error)
    

    def test_register_success(self):
        success = self.register.user_base(email,name,'password',code)
        self.assertFalse(success)




if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(),"report","first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_register_emali_error'))
    suite.addTest(FirstCase('test_register_username_error'))
    #suite.addTest(FirstCase('test_register_success'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report",description=u"这个是第一次测试报告",verbosity=2)
    runner.run(suite)