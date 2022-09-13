
from unicodedata import name
from selenium import webdriver
import random
from util.get_name import GetName

class GetEmail:
    def __init__(self,driver):
        self.driver = driver

    
    # 用户名+@163.com生成邮箱
    def get_email(self):
        get_name = GetName(self.driver)
        name = get_name.get_name()
        email = name +"@163.com"
        return email