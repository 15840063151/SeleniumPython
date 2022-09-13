


# 元素定位 
# 1）id进行定位  2）name进行定位  3)class_name进行定位  4）xpath 进行定位

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()           
driver.get("http://www.5itest.cn/register")
time.sleep(3)
EC.title_contains("注册")  
driver.find_element(by=By.ID , value="register_email").send_keys("mushishi_01@163.com")               # id进行定位
user_name_element = driver.find_elements(by=By.CLASS_NAME , value="controls")[1]                    # class_name进行定位
user_name_element.find_element(by=By.CLASS_NAME , value="form-control").send_keys("Mushishi01")  
driver.find_element(by=By.NAME , value="password").send_keys("111111")                                # name进行定位
driver.find_element(by=By.XPATH , value="//*[@id='captcha_code']").send_keys("111111")                # xpath 进行定位（选中——>右键——>copy——>copyXpath）
# "captcha_code" 换成单引号 'captcha_code' 才不会报错；原因"//*[@id="captcha_code"]"   双引号之间输出字符串 ，双引号中间如果该有引号，需要换成单引号  
