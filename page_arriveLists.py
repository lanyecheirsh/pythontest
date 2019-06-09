# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from public import Login 
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('arrivelists_log.txt','w')

sys.stderr = fp
sys.stdout = fp


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('http://docker30-erp.qipeipu.net/#/login/10000')

Login().user_login(driver)
# account = driver.find_element_by_id('account')
# #输入账号
# account.send_keys('erp')
# pwd = driver.find_element_by_id('password')
# pwd.send_keys('123')
# #点击【登录】
# driver.find_element_by_class_name('btn-group').click()
# #弹出选择厂牌窗口，验证是否弹出，title=‘选择厂牌’

# time.sleep(1)
# #选择厂牌和点击确定
# driver.find_element_by_xpath('//div[@id="app"]/div[2]/div/div[3]/div/ul/li[1]/span').click()
# driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div/div[2]/button').click()
# time.sleep(1)
#服务器错误的对话框
try:
	driver.find_element_by_xpath('//div[2]/button').click()
except:
	pass
#鼠标悬停在一级菜单-采购管理
mouse = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/ul[1]/li[4]/span/span[1]')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-在途管理
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/ul[1]/li[4]/ul/li[3]').click()
time.sleep(1)

#将鼠标移动开
mouse = driver.find_element_by_xpath('//button')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)

#点击查询
driver.find_element_by_xpath('//button').click()
#获取单号
ord_no = driver.find_element_by_xpath('//td/span').text
ord_no_m = ord_no.split('_',1)[0]
#输入单号
driver.find_element_by_xpath('//input').send_keys(ord_no_m)
driver.find_element_by_xpath('//button').click()
time.sleep(1)
#选择1
driver.find_element_by_xpath('//td').click()
time.sleep(1)
#点击调单价
driver.find_element_by_xpath('//div[2]/ul/li[2]/span/span').click()
time.sleep(1)
driver.find_element_by_xpath('//div[2]/div/button').click()
driver.find_element_by_xpath('//span[2]/img').click()
time.sleep(1)
#点击批量调价
driver.find_element_by_xpath('//div[2]/ul/li[3]/span/span').click()
time.sleep(1)
driver.find_element_by_xpath('//div[2]/div/button[2]').click()

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))
fp.close()
driver.close()