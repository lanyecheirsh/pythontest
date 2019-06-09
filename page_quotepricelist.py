# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from public import Login 
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('quotepricelist_log.txt','w')

sys.stderr = fp
sys.stdout = fp

driver = webdriver.Chrome()
driver.implicitly_wait(4)
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
except Exception as er:
	print('except:',er)
#鼠标悬停在一级菜单
mouse = driver.find_element_by_xpath('//*[@id="menu"]/li[2]/span')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-报价业务
driver.find_element_by_xpath('//*[@id="menu"]/li[2]/ul/li[1]/a').click()
time.sleep(2)
#将鼠标移动开
mouse = driver.find_element_by_xpath('//button')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
#定位第一个单号，并将单号保存在list_num_1
list_1=driver.find_element_by_xpath('//div[@id="app"]/div[5]/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/span/a')
list_num_1=list_1.get_attribute('text')


#输入单号点击查询
driver.find_element_by_xpath('//input').send_keys(list_num_1)
driver.find_element_by_xpath('//button').click()
time.sleep(2)
#点击接受新通知
checkbox_1 = driver.find_element_by_class_name('el-checkbox__inner')
checkbox_1.click()
#验证是否已勾选
try:
	checkbox_1.is_selected()
except Exception as er:
	print('未勾选,',er)

#去掉日期选择框的readonly属性
js = 'document.getElementsByClassName("el-input__inner")[0].removeAttribute("readonly");document.getElementsByClassName("el-input__inner")[1].removeAttribute("readonly");'
driver.execute_script(js)

#清空日期框，点击日期，输入日期
driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div/div[1]/div[1]/input').clear()
driver.find_element_by_css_selector('input.el-input__inner').click()
driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div/div[1]/div[1]/input').send_keys('2019-01-01')


#日期2
driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div/div[1]/div[2]/input').click()
driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div/div[1]/div[2]/input').send_keys('2019-01-09')
# driver.find_element_by_xpath('//td[3]').click()

#点击第一个单号
list_1.click()
time.sleep(3)
#服务器错误的对话框
try:
	driver.find_element_by_xpath('//div[7]/div/div/div[2]/button[1]').click()
except Exception as er:
	print('except:',er)
#已报价，已超时，全部
driver.find_element_by_xpath('//div/div/div/ul/li[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div/div/div/ul/li[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//div/div/div/ul/li[4]').click()
time.sleep(1)
#增加、删除
driver.find_element_by_xpath('//div[5]/div/div/div/div[3]/ul/li[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[5]/div/div/div/div[3]/ul/li[5]').click()
time.sleep(1)
#订货、返回
driver.find_element_by_xpath('//div[5]/div/div/div/div[3]/ul/li[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[2]/div/button[2]').click()
time.sleep(1)
#参考
driver.find_element_by_xpath('//div[5]/div/div/div/div[3]/ul/li[1]').click()
time.sleep(1)
#保存、确定
driver.find_element_by_xpath('//button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[2]/button').click()
time.sleep(1)
#提交报价
driver.find_element_by_xpath('//button').click()
time.sleep(3)
try:
	driver.find_element_by_xpath('//div[2]/button').click()
except:
	pass
time.sleep(1)
#返回
driver.find_element_by_xpath('//button[3]').click()

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))
fp.close()
driver.close()