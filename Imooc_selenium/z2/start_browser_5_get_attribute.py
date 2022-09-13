


# 输入注册用户名字及获取用户信息

import email
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()           
driver.get("http://www.5itest.cn/register")
time.sleep(3)
EC.title_contains("注册")  

locator = (By.CLASS_NAME , "controls")
WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))

email_element = driver.find_element(by=By.ID , value="register_email")     # 找到email元素 赋值给email_element
print(email_element.get_attribute("placeholder"))                          # get_attribute('textContent')获取元素标签内容      get_attribute('innerHTML')获取包含选中元素内的HTML
email_element.send_keys("yangyangyang@qq.com")
print(email_element.get_attribute("value"))


# driver.find_element(by=By.ID , value="register_email").send_keys("mushishi_01@163.com")              
user_name_element = driver.find_elements(by=By.CLASS_NAME , value="controls")[1]                   
user_name_element.find_element(by=By.CLASS_NAME , value="form-control").send_keys("Mushishi01")                    
driver.find_element(by=By.NAME , value="password").send_keys("111111")                               
driver.find_element(by=By.XPATH , value="//*[@id='captcha_code']").send_keys("111111")             

# driver.close()