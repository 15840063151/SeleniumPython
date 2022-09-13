



# coding = utf-8

from selenium import webdriver
import random

# 生成用户名
class GetName:
    def __init__(self,driver):
        self.driver = driver

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
        return user_info
    
    # 随机数生成用户名
    def get_name(self):
        name = self.get_range_user()
        return name
    