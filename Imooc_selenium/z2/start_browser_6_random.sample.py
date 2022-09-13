


# 生成用户名

import email
from selenium import webdriver
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()           
driver.get("http://www.5itest.cn/register")
time.sleep(3)
EC.title_contains("注册")  



for i in range(5):
    user_email = ''.join(random.sample('1234567890abcdefg',5))+"@163.com"               # random.sample(seq, n) 从序列seq中选择n个随机且独立的元素
    print(user_email)




locator = (By.CLASS_NAME , "controls")
WebDriverWait(driver,5).until(EC.visibility_of_element_located(locator))

email_element = driver.find_element(by=By.ID , value="register_email")     
print(email_element.get_attribute("placeholder"))                          
print(email_element.get_attribute("value"))


driver.find_element(by=By.ID , value="register_email").send_keys(user_email)           # send_keys 传入生成的随机数       
user_name_element = driver.find_elements(by=By.CLASS_NAME , value="controls")[1]                   
user_name_element.find_element(by=By.CLASS_NAME , value="form-control").send_keys("Mushishi01")                    
driver.find_element(by=By.NAME , value="password").send_keys("111111")                               
driver.find_element(by=By.XPATH , value="//*[@id='captcha_code']").send_keys("111111")             

#driver.close()