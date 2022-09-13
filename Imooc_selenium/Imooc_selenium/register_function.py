

import sys
sys.path.append('F:/selenium_python/Imooc_selenium')
import code
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from util.read_image import GetImageCode
import random
from PIL import Image
import base64
import json
import requests
from find_element import FindElement



class RegisterFunction():
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    # 获取driver，并且打开url
    def get_driver(self,url,i):
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 1:
            driver = webdriver.Edge() 
        else:
            driver = webdriver.Firefox() 

        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self,key,data):
        (self.get_user_element(key)).send_keys(data)

    
    # 定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
        return user_info


# 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name) 
        code_element = self.get_user_element('code_image')                                                     

        left = code_element.location['x']          
        top = code_element.location['y']             
        right = code_element.size['width'] + left             
        height = code_element.size['height'] + top            
        im = Image.open(file_name)   

        old_width = im.size[0]
        old_heigth = im.size[1]
        newimg = im.resize((int(old_width * 0.8) ,int(old_heigth * 0.8)),Image.ANTIALIAS)
        img = newimg.crop((left,top,right,height))  
        img.save(file_name)  


# # 解析图片 获取验证码
#     def base64_api(uname, pwd, img, typeid):
#         #self.get_code_image(file_name)
#         with open(img, 'rb') as f:
#             base64_data = base64.b64encode(f.read())
#             b64 = base64_data.decode()
#         data = new_func(uname, pwd, typeid, b64)
#         result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
#         if result['success']:
#             return result["data"]["result"]
#         else:
#             return result["message"]
#         return ""

#     def new_func(uname, pwd, typeid, b64):
#         data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
#         return data

    
    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info +"@163.com"
        file_name = "F:/selenium_python/yanzhengma/image.png" 
        
        self.get_code_image(file_name)
        imagecode = GetImageCode()
        code_text = imagecode.base64_api(file_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name',user_name_info)
        self.send_user_info('password',"111111")
        self.send_user_info('code_text',code_text)    
        self.get_user_element('resister_button').click()
        code_text_error = self.get_user_element('code_text_error')
        if code_text_error == None:
            print("注册成功")
        else:
            print("注册失败")
            self.driver.save_screenshot('F:/selenium_python/yanzhengma/error.png')
        time.sleep(3)
        #self.driver.close()

if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()

    

