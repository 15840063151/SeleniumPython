


# 通过title判断 是否成功进入登录页面

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC    # 扩展库（expected_conditions包的名字比较长 通过as方式只写首字母，这样就可以通过EC对这个模块的方法进行调用）
driver = webdriver.Chrome()           
driver.get("http://www.5itest.cn/register")
time.sleep(5)
EC.title_contains("注册")                                           # 通过EC对这个模块的方法进行调用，获取title

# title_contains   判断当前页面的title是否包含预期字符串，返回布尔值
# title_is  判断当前页面的title是否完全等于（==）预期字符串，返回是布尔值
