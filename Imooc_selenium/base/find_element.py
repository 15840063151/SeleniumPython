
# 用于定位于所有元素

#coding=utf-8

from util.read_ini import ReadIni
from  selenium.webdriver.common.by import By

class FindElement():
    def __init__(self,driver) :
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadIni(key)                # 实例化对象
        data = read_ini.get_value()    # 传入key，data返回“id>register_nickname”这种形式的值
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element(by=By.ID,value=value)
            elif by == 'name':
                return self.driver.find_element(by=By.NAME,value=value)
            elif by == 'className':
                return self.driver.find_element(by=By.CLASS_NAME,value=value)
            else: 
                return self.driver.find_element(by=By.XPATH,value=value)
        except:
            self.driver.save_screenshot('F:/selenium_python/yanzhengma/%s.png' %value)  #当前定位的元素信息的元素信息 进行命名
            return None