import time

from fontTools.subset.svg import xpath
# 这步有点多余
from selenium import webdriver
from time import sleep

driver=webdriver.Edge()
# 浏览器类型
driver.get("https://kyfw.12306.cn/otn/resources/login.html")
# 网址
driver.find_element('xpath','//*[@id="J-userName"]').send_keys("12306手机号")
sleep(0.1)
# 输入手机号
driver.find_element('xpath','//*[@id="J-password"]').send_keys("12306密码")
sleep(0.1)
# 输入密码
driver.find_element('xpath','//*[@id="J-login"]').click()
sleep(0.1)
driver.find_element('xpath','//*[@id="id_card"]').send_keys("身份证后四位")
sleep(30)
# 获取验证码得手动点击
driver.find_element('xpath','//*[@id="sureClick"]').click()
#至此，就可以自动登录
sleep(1000)
