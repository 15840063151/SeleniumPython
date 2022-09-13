


# coding = utf-8
from email.mime import image
from util.read_image import GetImageCode
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class GetCode:
    # 获取图片
    def __init__(self,driver):
        self.driver = driver
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name) 
        code_element = self.driver.find_element(by=By.ID , value='getcode_num')                                                     

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
        time.sleep(1)

    

    # 解析图片 获取验证码
    def analysis_code(self):
        file_name = os.path.join(os.getcwd(),"image","code.png")
        self.get_code_image(file_name)
        imagecode = GetImageCode()
        code_text = imagecode.base64_api(file_name)
        time.sleep(1)
        return code_text



       
