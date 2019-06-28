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

fp = open('returnconfirm_log.txt','w')

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
#点击二级菜单-退货确认
driver.find_element_by_xpath('//*[@id="menu"]/li[7]/ul/li[8]/a').click()
time.sleep(1)
'''
#销售退货tab
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[4]/ul/li[1]').click()
time.sleep(1)
#刷新
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/button[5]').click()
#代收
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/button[1]').click()
time.sleep(5)

#挂账
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/button[2]').click()
time.sleep(3)
#现结
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/button[3]').click()
time.sleep(2)
driver.find_element_by_css_selector('#app > div.app-body > div > div:nth-child(1) > div.head.clearfix.query-box > div:nth-child(1) > select > option:nth-child(2)').click()
time.sleep(1)
beizhu=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/input[2]')
beizhu.clear()
beizhu.send_keys('xinzengbeizhu')
#存储要判断是否是现结结算，不然有弹窗，先不判断
#driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/button[4]').click()
time.sleep(5)
#取消退货
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/button[6]').click()
time.sleep(1)

#综合查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div/button[2]').click()

#采购退货确认呢
driver.find_element_by_css_selector('#app > div.app-body > div > div:nth-child(1) > div.head.clearfix.query-box > div.dimension.right > ul > li:nth-child(2)').click()
time.sleep(2)
#刷新
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[2]/button[4]').click()
time.sleep(2)
#挂账
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[2]/button[1]').click()
time.sleep(3)
#现结
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[2]/button[2]').click()
time.sleep(1)
acct=driver.find_element_by_css_selector('#app > div.app-body > div > div:nth-child(1) > div.head.clearfix.query-box > div:nth-child(2) > select > option:nth-child(2)').click()
time.sleep(1)
beizhu2=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[2]/input[2]')
beizhu2.clear()
beizhu2.send_keys('xinzengbeizhu2')
time.sleep(1)
#取消退货
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[2]/button[6]').click()
time.sleep(3)

#综合查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[2]/div/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/button[2]').click()
'''
#外采退货确认
driver.find_element_by_css_selector('#app > div.app-body > div > div:nth-child(1) > div.head.clearfix.query-box > div.dimension.right > ul > li:nth-child(3)').click()
time.sleep(2)
#刷新
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[3]/button[4]').click()
time.sleep(2)
#挂账
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[3]/button[1]').click()
time.sleep(3)
#现结
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[3]/button[2]').click()
time.sleep(1)
acct=driver.find_element_by_css_selector('#app > div.app-body > div > div:nth-child(1) > div.head.clearfix.query-box > div:nth-child(3) > select > option:nth-child(2)').click()
time.sleep(1)
beizhu3=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[3]/input[2]')
beizhu3.clear()
beizhu3.send_keys('xinzengbeizhu3')
time.sleep(1)

#综合查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[3]/div/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div/button[2]').click()


time.sleep(2)
print('测试完成，退出')
driver.close()
