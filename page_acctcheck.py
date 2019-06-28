#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as ui
from public import Login
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('acctcheck_log.txt','w')

sys.stderr = fp
sys.stdout = fp

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('http://docker31-erp.qipeipu.net/#/login/10000')
Login().user_login(driver)
try:
	driver.find_element_by_xpath('//div[2]/button').click()
except:
	pass
#鼠标悬停在一级菜单-财务结算
mouse = driver.find_element_by_xpath('//*[@id="menu"]/li[7]/span/span[1]/img[2]')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-客户对账
driver.find_element_by_xpath('//*[@id="menu"]/li[7]/ul/li[3]/a').click()
time.sleep(1)
#移走鼠标
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div[1]').click()
time.sleep(1)

#输入客户名称
custname=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div/div/input')
custname.clear()
custname.send_keys('广州帅泽')
time.sleep(2)
#业务
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[4]/input').click()
time.sleep(3)
#销售&销售退货
driver.find_element_by_css_selector('#app > div.app-body > div > div.query-wrap.query-box > div.v-multi-checkbox-group > div>label:nth-child(1)').click()
driver.find_element_by_css_selector('#app > div.app-body > div > div.query-wrap.query-box > div.v-multi-checkbox-group > div>label:nth-child(2)').click()
time.sleep(1)

#未结算
driver.find_element_by_css_selector('#app > div.app-body > div > div.query-wrap.query-box > select:nth-child(9)').click()
driver.find_element_by_css_selector('#app > div.app-body > div > div.query-wrap.query-box > select:nth-child(9) > option:nth-child(2)').click()
time.sleep(1)
#未复核
driver.find_element_by_css_selector('#app > div.app-body > div > div.query-wrap.query-box > select:nth-child(11)').click()
driver.find_element_by_css_selector('#app > div.app-body > div > div.query-wrap.query-box > select:nth-child(11) > option:nth-child(2)').click()
time.sleep(1)

#查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button').click()
time.sleep(1)

#综合查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div[1]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div[1]/div/div/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#复核号
num=time.strftime("%m%d%H%M",time.localtime())
numinput=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div[1]/input')
numinput.clear()
numinput.send_keys(num)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[5]/div/div/div[2]/button[1]').click()
time.sleep(2)
#勾选第一条
driver.find_element_by_xpath('//*[@id="accountTable"]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div[1]/button').click()
time.sleep(2)
#确认复核
#driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[5]/div/div/div[2]/button[1]').click()
#导出
export=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div[1]/ul/li')
title=export.get_attribute("title")
print(title)
if title != "导出":
    print("导出有错误")

time.sleep(2)
driver.close()
