


# coding = utf-8

from tkinter import N
from page.register_page import RegisterPage
from util.get_code import GetCode
from util.get_emali import GetEmail
from util.get_name import GetName

class RegisterHandle():
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(driver)
    # 输入邮箱
    def send_user_email(self,email):
        # 调用get.email.py文件生成邮箱（name+@163.com）
        # get_email = GetEmail(self.driver)
        # email = get_email.get_email()
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self,name):
        # 调用get.name.py文件生成随机数用户名
        # get_name = GetName(self.driver)
        # name = get_name.get_name()
        self.register_p.get_username_element().send_keys(name)    

    # 输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self,code):
        get_code_text = GetCode(self.driver)
        code = get_code_text.analysis_code()
        self.register_p.get_code_element().send_keys(code)

    # 获取文字信息（获取元素通过.text方法转化成文字）
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text        
            elif info == 'password_error':
                text = self.register_p.get_password_error_element().text  
            else:
                text = self.register_p.get_code_error_element().text
        except:
            text =  None 
        return text

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    # 获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text