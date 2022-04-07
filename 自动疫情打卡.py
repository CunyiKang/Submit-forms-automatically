# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:55:47 2020

@author: 康存义
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://xgfx.bnuz.edu.cn/xsdtfw/sys/emapfunauth/pages/funauth-login.do?service=%2Fxsdtfw%2Fsys%2Fswmxsyqxxsjapp%2F*default%2Findex.do#/')


# 将屏幕滚动定位到最上方
js = 'window.scrollTo(0,0);'
driver.execute_script(js)

# 停顿2秒后再进行操作
time.sleep(1)

el = driver.find_element_by_xpath("//input[@placeholder='请输入用户名']")
el.send_keys('XXXXXXXXXX')

el = driver.find_element_by_xpath("//input[@placeholder='请输入密码']")
el.send_keys('XXXXXXXXXX')

time.sleep(0.5)

el=driver.find_element_by_xpath("//button[@type='button']")
el.click()



#按每日报平安
time.sleep(5)

el= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/a[2]')
el.click()

#输入体温
time.sleep(5)
el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[7]/div/a/div[2]/div[2]/input")
el.send_keys('36')
#选择问题一第一部分
time.sleep(1)
 
el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[10]/div/a")
el.click()

#选择第一题的否

time.sleep(1)

el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[10]/div/div/div[1]/div/div/div/a[2]/div[2]/div[1]/label/span[1]/span")
el.click()


#选择问题二第一部分
time.sleep(1)
 
el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[12]/div/a")
el.click()

#选择第二题的否

time.sleep(1)

el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[12]/div/div/div[1]/div/div/div/a[2]/div[2]/div[1]/label/span[1]/span")
el.click()


#选择问题三第一部分
time.sleep(1)
 
el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[14]/div/a")
el.click()

#选择第三题的否

time.sleep(1)

el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[14]/div/div/div[1]/div/div/div/a[2]/div[2]/div[1]/label/span[1]/span")
el.click()


#选择问题四第一部分
time.sleep(1)
 
el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[16]/div/a")
el.click()

#选择第四题的否

time.sleep(1)

el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[16]/div/div/div[1]/div/div/div/a[2]/div[2]/div[1]/label/span[1]/span")
el.click()


#选择问题五第一部分
time.sleep(1)
 
el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[18]/div/a")
el.click()

#选择第五题的否

time.sleep(1)

el = driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div/div/div/div/div[18]/div/div/div[1]/div/div/div/a[2]/div[2]/div[1]/label/span[1]/span")
el.click()


#提交
time.sleep(1)

el = driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/div/button")
el.click()

