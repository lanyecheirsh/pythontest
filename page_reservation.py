# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from public import Login
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('reservation_log.txt','w')

sys.stderr = fp
sys.stdout = fp


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get('http://docker31-erp.qipeipu.net/#/login/10000')

Login().user_login(driver)

#服务器错误的对话框
try:
	driver.find_element_by_xpath('//div[2]/button').click()
except:
	pass
#鼠标悬停在一级菜单
mouse = driver.find_element_by_xpath('//*[@id="menu"]/li[2]/span')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-代订业务
driver.find_element_by_xpath('//*[@id="menu"]/li[2]/ul/li[3]/a').click()
time.sleep(1)

#将鼠标移动开
mouse = driver.find_element_by_xpath('//button')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
#点击查询
driver.find_element_by_xpath('//button[1]').click()
time.sleep(2)
#勾选第一个
driver.find_element_by_xpath('//tbody/tr[1]/td[1]/label/span').click()
#点击库存交付
driver.find_element_by_xpath('//button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[7]/div/div/div[2]/button[2]').click()
time.sleep(1)
#点击延长发货
driver.find_element_by_xpath('//button[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#点击无货
driver.find_element_by_xpath('//button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[3]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#点击合并退货
driver.find_element_by_xpath('//button[5]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div[5]/div/div/div[1]/div/div[1]/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[5]/div/div/div[2]/div/button').click()
time.sleep(1)
#检查输入框
driver.find_element_by_xpath('//input').send_keys('11')

driver.find_element_by_xpath('//div[2]/div/div/div/input').send_keys('22')

driver.find_element_by_xpath('//div[3]/input').send_keys('33')


driver.find_element_by_xpath('//div[5]/input').send_keys('55')

driver.find_element_by_xpath('//div[2]/div/div/div/div/input').send_keys('66')

driver.find_element_by_xpath('//div[2]/input').send_keys('77')

driver.find_element_by_xpath('//div[2]/div[3]/input').send_keys('66')

#下拉选择框

driver.find_element_by_xpath('//div[2]/div[4]/select').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div[2]/div[2]/div[4]/select/option[2]').click()
#点击保存
driver.find_element_by_xpath('//div[2]/button[1]').click()

# save = driver.find_element_by_xpath('//body/div/div[5]/div/div[8]/div').is_displayed()
# print(save)

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))
fp.close()
driver.close()
