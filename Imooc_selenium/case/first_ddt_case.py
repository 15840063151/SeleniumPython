


# coding = utf-8
import unittest
import sys
from unittest import suite
sys.path.append('F:/selenium_python/Imooc_selenium')
from util.excel_util import ExcelUtil
import ddt
from selenium import webdriver
from business.register_business import RegisterBusiness
import os
import time
import HTMLTestRunner
import code

ex = ExcelUtil()
data = ex.get_data()   # data数据即返回的excel列表
#[[1.0, 'username1', 'password1', 'code', 'user_email_error', '请输入有效的电子邮件地址'], ['2@163.com', 'username2', 'password2', 'code', 'user_email_error', '请输入有效的电子邮件地址']]



# 邮箱、用户名、密码、验证码、错误信息定位元素、错误信息提示
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.register = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(1)
        for method_name,error in self._outcome.errors:                         # TearDown 中捕获错误信息：for method_name,error in self._outcome.errors （self._outcome.errors返回list）
            if error:
                case_name = self._testMethodName                              # 根据当前动态的类名和方法名来获取
                self.driver.save_screenshot(os.path.join(os.getcwd(),"report",case_name+".png"))
        self.driver.close()

    # @ddt.data(
    #     ['1','username1','password1','code','user_email_error','请输入有效的电子邮件地址'],
    #     ['2@163.com','username2','password2','code','user_email_error','请输入有效的电子邮件地址']
    #     )
    # @ddt.unpack
    # def test_register_case(self,email,username,password,code,assertCode,assertText):
    #     email_error = self.register.register_function(email,username,password,code,assertCode,assertText)
    #     self.assertTrue(email_error,"邮箱错误，case执行register_email_error用例")


    @ddt.data(*data)  #输入data数据
    def test_register_case(self,data):
        email,username,password,code,assertCode,assertText = data    #list赋值
        email_error = self.register.register_function(email,username,password,code,assertCode,assertText)
        self.assertTrue(email_error,"邮箱错误，case执行register_email_error用例")


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(),"report","first_case1.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report1",description=u"这个是第一次测试报告1",verbosity=2)
    runner.run(suite)