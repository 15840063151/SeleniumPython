


# 使用pytesseract识别图片中的问题

import email
from selenium import webdriver
import time
import random
from PIL import Image                # 引进Pillow库
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytesseract
from PIL import Image
import base64
import json
import requests

# 打开注册页面
driver = webdriver.Chrome()           
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(3)
EC.title_contains("注册")  

for i in range(5):
    user_email = ''.join(random.sample('1234567890abcdefg',5))+"@163.com"              
    print(user_email)


# 截取二维码图片
driver.save_screenshot('F:/selenium_python/yanzhengma/test.png')       
#driver.execute_script("document.body.style.zoom=0.8")                   
code_element = driver.find_element(by=By.ID , value='getcode_num')            
print(code_element.location)                                            

left = code_element.location['x']          
top = code_element.location['y']             
right = code_element.size['width'] + left             
height = code_element.size['height'] + top            
im = Image.open('F:/selenium_python/yanzhengma/test.png')            

old_width = im.size[0]
old_heigth = im.size[1]
newimg = im.resize((int(old_width * 0.8) ,int(old_heigth * 0.8)),Image.ANTIALIAS)
img = newimg.crop((left,top,right,height))  
img.save('F:/selenium_python/yanzhengma/test1.png')  

# 识别二维码
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = new_func(uname, pwd, typeid, b64)
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

def new_func(uname, pwd, typeid, b64):
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    return data


if __name__ == "__main__":
    img_path = "F:/selenium_python/yanzhengma/test1.png"
    result = base64_api(uname='gangjin', pwd='fanhongdamm', img=img_path, typeid=3)
    print(result)



time.sleep(3)
locator = (By.CLASS_NAME , "controls")
WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))

email_element = driver.find_element(by=By.ID , value="register_email")     
print(email_element.get_attribute("placeholder"))                          
print(email_element.get_attribute("value"))

driver.find_element(by=By.ID , value="register_email").send_keys(user_email)                 
user_name_element = driver.find_elements(by=By.CLASS_NAME , value="controls")[1]                   
user_name_element.find_element(by=By.CLASS_NAME , value="form-control").send_keys("Mushishi01")                    
driver.find_element(by=By.NAME , value="password").send_keys("mima")                               
driver.find_element(by=By.XPATH , value="//*[@id='captcha_code']").send_keys(result)             

#driver.close()