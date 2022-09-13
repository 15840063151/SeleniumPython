


# 验证码截取

import email
from selenium import webdriver
import time
import random
from PIL import Image                # 引进Pillow库
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()           
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(3)
EC.title_contains("注册")  

for i in range(5):
    user_email = ''.join(random.sample('1234567890abcdefg',5))+"@163.com"              
    print(user_email)


driver.save_screenshot('F:/selenium_python/yanzhengma/test.png')        # save_screenshot(filename)获取当前屏幕截图并保存为指定文件,filename指定保存的路径或者图片的文件名
#driver.execute_script("document.body.style.zoom=0.8")                   # 将缩放与布局调整到100%。 当前电脑是125% 故诚意0.8
code_element = driver.find_element(by=By.ID , value='getcode_num')            
print(code_element.location)                                            # 通过localtion方法 获取验证码的坐标{x:123 , y:345} (验证码图片左上角的坐标)

left = code_element.location['x']            # 验证码横坐标
top = code_element.location['y']             # 验证码纵坐标
right = code_element.size['width'] + left              # 验证码的宽+横坐标值=验证码右上角的横坐标
height = code_element.size['height'] + top             # 验证码的高+纵坐标值=验证码左下角的纵坐标
im = Image.open('F:/selenium_python/yanzhengma/test.png')              # 打开 通过save_screenshot保存下来的图片

old_width = im.size[0]
old_heigth = im.size[1]
newimg = im.resize((int(old_width * 0.8) ,int(old_heigth * 0.8)),Image.ANTIALIAS)
img = newimg.crop((left,top,right,height))   # crop()函数用于裁剪图片，crop((x1,y1,x2,y2))四个参数如下：x1 起始 横向坐标 、 y1 起始 纵向坐标 、 x2 结束 横向坐标 、 y2 结束 纵向坐标
img.save('F:/selenium_python/yanzhengma/test1.png')  



locator = (By.CLASS_NAME , "controls")
WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))

email_element = driver.find_element(by=By.ID , value="register_email")     
print(email_element.get_attribute("placeholder"))                          
print(email_element.get_attribute("value"))

driver.find_element(by=By.ID , value="register_email").send_keys(user_email)                 
user_name_element = driver.find_elements(by=By.CLASS_NAME , value="controls")[1]                   
user_name_element.find_element(by=By.CLASS_NAME , value="form-control").send_keys("Mushishi01")                    
driver.find_element(by=By.NAME , value="password").send_keys("mima")                               
driver.find_element(by=By.XPATH , value="//*[@id='captcha_code']").send_keys("111111")             

# driver.close()