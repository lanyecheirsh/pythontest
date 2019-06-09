# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from public import Login 
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('package_log.txt','w')

sys.stderr = fp
sys.stdout = fp


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('http://docker39-erp.qipeipu.net/#/login/10000')
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
#鼠标悬停在一级菜单
mouse = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/ul[1]/li[2]/span/span[1]')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-物流打包
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/ul[1]/li[2]/ul/li[4]').click()
time.sleep(1)

#将鼠标移动开
mouse = driver.find_element_by_xpath('//button')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)

#勾选第一个
driver.find_element_by_xpath('//tr[1]/td[3]/label/span').click()
#点击延长发货
driver.find_element_by_xpath('//button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[6]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#点击防伪码
driver.find_element_by_xpath('//button[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[7]/div/div/div[2]/div/button').click()
time.sleep(2)
#点击打包
driver.find_element_by_xpath('//button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[11]/div/div/div[2]/button[2]').click()
time.sleep(1)



# 待发货，已发货，抽检不通过
driver.find_element_by_xpath('//div[4]/div/div[1]/div/div[2]/div/ul/li[2]').click()
time.sleep(3) 
driver.find_element_by_xpath('//div[4]/div/div[1]/div/div[4]/div/ul/li[3]').click()
time.sleep(1)
# driver.find_element_by_xpath('//div[4]/div/ul/li[4]').click()
# time.sleep(1)
# #服务器错误
# try:
# 	driver.find_element_by_xpath('//div[7]/div/div/div[2]/button').click()
# except:
# 	pass
# driver.find_element_by_xpath('//div[2]/div/ul/li').click()
# time.sleep(1)
# #服务器错误
# try:
# 	driver.find_element_by_xpath('//div[7]/div/div/div[2]/button').click()
# except:
# 	pass

#获取单号
ordcode_1 = driver.find_element_by_xpath('//div[4]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/span').text
print(ordcode_1)

# ordno_1 = ord_1.get_attribute('text')
# print(ord_1)
# print(ordno_1)
#输入单号
driver.find_element_by_xpath('//div[4]/div/div[1]/div/input[1]').send_keys(ordcode_1)
# #获取编号
parts_1 = driver.find_element_by_xpath('//div[4]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[5]/span').text
# partscode_1=parts_1.get_attribute('text')
# #输入编号
driver.find_element_by_xpath('//div[4]/div/div[1]/div/input[2]').send_keys(parts_1)
#点击查询
driver.find_element_by_xpath('//div[4]/div/div[1]/div/button[1]').click()


now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))
fp.close()
driver.close()