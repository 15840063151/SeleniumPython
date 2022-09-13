


#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from util.read_image import GetImageCode
import random
from PIL import Image
import base64
import json
import requests


driver = webdriver.Chrome()
# 浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(3)


# 获取element信息
def get_element(id):
    element = driver.find_element(by=By.ID,value=id)
    return element


# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
    return user_info


# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name) 
    code_element = driver.find_element(by=By.ID , value='getcode_num')                                                     

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
# def base64_api(uname, pwd, img, typeid):
#     with open(img, 'rb') as f:
#         base64_data = base64.b64encode(f.read())
#         b64 = base64_data.decode()
#     data = new_func(uname, pwd, typeid, b64)
#     result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
#     if result['success']:
#         return result["data"]["result"]
#     else:
#         return result["message"]
#     return ""

# def new_func(uname, pwd, typeid, b64):
#     data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
#     return data



# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info +"@163.com"
    file_name = "F:/selenium_python/yanzhengma/image.png"

    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    imagecode = GetImageCode()
    test = imagecode.base64_api(file_name)
    get_element("captcha_code").send_keys(test)
    get_element("register-btn").click()

run_main()