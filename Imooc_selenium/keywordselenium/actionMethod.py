


# coding = utf-8
import time
from selenium import webdriver
from base.find_element import FindElement

class ActinoMethod:
    # 打开浏览器
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge() 

    # 输入地址
    def get_url(self,url):  
        self.driver.get(url)

    # 定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element
    
    # 输入元素
    def element_send_keys(self,key,value):   # 因为method_value(send_value,handle_value)是代表找到方法(拿到输入数据，拿到操作值)，所以element_send_keys
        element = self.get_element(key)      # 定位元素
        element.send_keys(value)             # 给定位的元素输入值

    # 点击元素
    def click_element(self,key):
        self.get_element(key).click()
    
    # 等待
    def sleep_time(self):
        time.sleep(3)
    
    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title标题
    def get_title(self):
        return self.driver.title

