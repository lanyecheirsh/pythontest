#coding=utf-8
from typing import Optional, Any

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from public import Login
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('shouldpay_log.txt','w')

sys.stderr = fp
sys.stdout = fp



driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('http://docker34-erp.qipeipu.net/#/login/10000')
Login().user_login(driver)
try:
	driver.find_element_by_xpath('//div[2]/button').click()
except:
	pass
#鼠标悬停在一级菜单-财务结算
mouse = driver.find_element_by_xpath('//*[@id="menu"]/li[7]/span/span[1]/img[2]')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-应收应付
driver.find_element_by_xpath('//*[@id="menu"]/li[7]/ul/li[2]/a').click()
time.sleep(1)

#将鼠标移动开
mouse = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/ul/li[1]')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)

#综合查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/button').click()
time.sleep(1)

input=driver.find_element_by_xpath('//*[@id="focusCursor"]/div/div/div/input')
input.clear()
input.send_keys('广州宝誉')
input.click()
time.sleep(3)
#wait = ui.WebDriverWait(driver , 10)
#wait.until(lambda driver:driver.find_element_by_class('el-scrollbar__view el-autocomplete-suggestion__list'))
#driver.find_element_by_css_selector("[class='el-scrollbar__view el-autocomplete-suggestion__list']").click()
driver.find_element_by_css_selector('.el-scrollbar__view.el-autocomplete-suggestion__list>li:nth-child(1)').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div/div/div/div[2]/div/button[1]').click()
time.sleep(1)
'''
#账期设置
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[7]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/label[1]/input').click()
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[7]/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/label[2]/input').click()
#限额
limit=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[7]/div/div/div[1]/div/div[3]/div/div/div[1]/input')
limit.clear()
limit.send_keys('100000')
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[7]/div/div/div[2]/div/button[1]').click()
time.sleep(2)

#附加账期和限额
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[2]').click()
time.sleep(1)
account=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[8]/div/div/div[1]/div/div[2]/div/div/div[1]/input')
account.clear()
account.send_keys('1')
addlimit=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[8]/div/div/div[1]/div/div[2]/div/div/div[2]/input')
addlimit.clear()
addlimit.send_keys('100')
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[8]/div/div/div[2]/div/button[1]').click()
time.sleep(2)
#期初
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[5]/div/div/div[2]/div/button[2]').click()
time.sleep(2)
#备注
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[5]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="focusCursor" and @class="reset-textarea"]').clear()
driver.find_element_by_xpath('//*[@id="focusCursor" and @class="reset-textarea"]').send_keys('beizhu')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[10]/div/div/div[2]/div/button[1]').click()
#导出
title=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/ul/li').get_attribute("title")
print(title)
if title != "导出":
    print("导出异常")

#明细账
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/ul/li[2]').click()
time.sleep(1)
#综合查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div').click()
driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul>li:nth-child(3)').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div/div/div/div[2]/div/button[1]').click()
time.sleep(2)
#选中
first=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[3]/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]')
first.click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[4]/div/div/div[2]/div/button').click()
time.sleep(1)
'''
#导出
export=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/ul/li')
title=export.get_attribute("title")
print(title)
if title != "导出":
    print("导出有错误")

time.sleep(2)
driver.close()

