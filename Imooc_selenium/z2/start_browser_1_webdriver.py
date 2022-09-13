# coding = utf-8
from multiprocessing.sharedctypes import Value
from threading import local
from turtle import title
from xml.sax.xmlreader import Locator
from selenium import webdriver
driver = webdriver.Chrome()            #启动浏览器（1.将chromdriver放到python的安装目录下  2.运行代码前关闭管不浏览器，该功能只能第一次打开浏览器）
driver.get("http://www.baidu.com")


from selenium import webdriver 
driver = webdriver.Edge() 
driver.get("http://www.baidu.com")


from selenium import webdriver 
driver = webdriver.Firefox() 
driver.get("http://www.baidu.com")



