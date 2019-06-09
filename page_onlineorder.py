# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from public import Login
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('onlineorder_log.txt','w')

sys.stderr = fp
sys.stdout = fp

driver = webdriver.Chrome()
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
#鼠标悬停在一级菜单
mouse = driver.find_element_by_xpath('//*[@id="menu"]/li[2]/span')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-在线接单
driver.find_element_by_xpath('//*[@id="menu"]/li[2]/ul/li[2]/a').click()
time.sleep(2)


#将鼠标移动开
mouse = driver.find_element_by_xpath('//button')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)

#定位第一个单号，并将单号保存在list_num_1
list_1=driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/span/a')
list_num_1=list_1.get_attribute('text')
print(list_num_1)
#输入单号点击查询
driver.find_element_by_xpath('//div[4]/div/div/div/div[1]/input').send_keys(list_num_1)
driver.find_element_by_xpath('//div[4]/div/div/div/div[1]/button').click()
time.sleep(2)

#点击接受新通知
checkbox_1 = driver.find_element_by_class_name('embellish-checkbox')
checkbox_1.click()
time.sleep(2)
# #验证是否已勾选
# if checkbox_1.is_selected():
# 	print('已勾选')
# else:
# 	print('未勾选')
#掉日期选择框的readonly属性
js = 'document.getElementsByClassName("el-input__inner")[0].removeAttribute("readonly");document.getElementsByClassName("el-input__inner")[1].removeAttribute("readonly");'
driver.execute_script(js)

#日期清除、点击、输入_1
date_input_1 = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div/div[1]/div[1]/input')
date_input_1.clear()
date_input_1.click()
date_input_1.send_keys('2019-01-01')
#日期清除、点击、输入_2
date_input_2 = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div/div[1]/div[2]/input')
date_input_2.clear()
date_input_2.click()
date_input_2.send_keys('2019-01-09')

#点击第一个单号
list_1.click()
time.sleep(2)
#还原
driver.find_element_by_xpath('//table/tr[3]/td').click()
time.sleep(1)
driver.find_element_by_xpath('//div[2]/div/div/div/button').click()
time.sleep(1)
driver.find_element_by_css_selector('#online-order-detail > div.v-modal > div > div > div.v-modal-btn > button.btn.normal-btn.cancel').click()
time.sleep(1)
#无货
driver.find_element_by_xpath('//div[2]/div/div/div/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//select').click()
time.sleep(1)
driver.find_element_by_xpath('//option[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[2]/div/button[2]').click()
time.sleep(1)
#延长发货
driver.find_element_by_xpath('//button[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[6]/div/div/div/div/div/div/select').click()
time.sleep(1)
driver.find_element_by_xpath('//div[6]/div/div/div/div/div/div/select/option[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[6]/div/div/div/div/div/div[2]/select').click()
time.sleep(1)
driver.find_element_by_xpath('//div[6]/div/div/div/div/div/div[2]/select/option[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[6]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#查报价
driver.find_element_by_xpath('//button[4]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[7]/div/div/div[2]/div/button').click()
time.sleep(1)
#同步属性
driver.find_element_by_xpath('//button[5]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[7]/div/div/div[2]/button').click()
time.sleep(1)
#确认提交
driver.find_element_by_xpath('//div[4]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//div[11]/div/div/div[2]/button[2]').click()
time.sleep(1)
#返回
driver.find_element_by_xpath('//div[4]/button[2]').click()

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))
fp.close()
driver.close()