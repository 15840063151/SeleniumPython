


# 使用Expected_conditions判断元素是否可见

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
# EC.visibility_of_element_located(locator)   判断传入的元素是否可见     
# WebDriverWait(driver, timeout).until(method, message=’’)  程序每隔xx秒看一眼，如果条件成立了，则执行下一步；否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException异常

driver.find_element(by=By.ID , value="register_email").send_keys("mushishi_01@163.com")              
user_name_element = driver.find_elements(by=By.CLASS_NAME , value="controls")[1]                   
user_name_element.find_element(by=By.CLASS_NAME , value="form-control").send_keys("Mushishi01")                    
driver.find_element(by=By.NAME , value="password").send_keys("111111")                               
driver.find_element(by=By.XPATH , value="//*[@id='captcha_code']").send_keys("111111")             

driver.close()    #每次运行都是实例化了一个driver，driver需要关闭