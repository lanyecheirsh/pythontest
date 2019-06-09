# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from public import Login 
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()
fp = open('purchase.txt','w')

sys.stderr = fp
sys.stdout = fp

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get('http://docker31-erp.qipeipu.net/#/login/10000')

Login().user_login(driver)
# account = driver.find_element_by_id('account')
# #输入账号
# account.send_keys('erp')
# pwd = driver.find_element_by_id('password')
# pwd.send_keys('123')
# #点击【登录】
# driver.find_element_by_class_name('btn-group1').click()

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
#鼠标悬停在一级菜单-销售管理
mouse = driver.find_element_by_xpath('//*[@id="menu"]/li[6]/span')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-外购登记
driver.find_element_by_xpath('//*[@id="menu"]/li[6]/ul/li[4]/a').click()
time.sleep(1)

#将鼠标移动开
mouse = driver.find_element_by_xpath('//button[2]')
ActionChains(driver).move_to_element(mouse).perform()

#获取配件编号、客户名、单号
parts_code=driver.find_element_by_xpath('//div[4]/div/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[4]/span').text
cus_name=driver.find_element_by_xpath('//div[4]/div/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/span').text
order_no=driver.find_element_by_xpath('//div[4]/div/div[1]/div[3]/div[1]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/span').text
#输入编号、客户名、单号
driver.find_element_by_id('partsCode').send_keys(parts_code)
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(cus_name)
time.sleep(1)
driver.find_element_by_xpath('//body/div[3]/div/div/ul/li[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div[1]/div[2]/input[2]').send_keys(order_no)
time.sleep(1)
#点击查询
driver.find_element_by_xpath('//div[4]/div/div[1]/div[2]/button').click()
time.sleep(2)
#点击查询
#选择第一条外司记录
driver.find_element_by_xpath('//div[4]/div/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]').click()

time.sleep(1)
driver.find_element_by_xpath('//div[2]/div/div[2]/div/button[1]').click()
#如果弹出确认窗口，点击确认
try:
	# driver.find_element_by_xpath('//div[7]/div/div/div[2]/buttonn').click()
    driver.find_element_by_xpath('//div[5]/div/div[7]/div/div/div[2]/button[1]').click()
except:
	pass
time.sleep(1)
#保存备注
driver.find_element_by_xpath('//div[4]/div/div[1]/div[4]/input[2]').send_keys('test')
time.sleep(1)
driver.find_element_by_xpath('//div[4]/button[2]').click()
time.sleep(1)
#
driver.find_element_by_xpath('//div[3]/div/div[2]/div[2]/table/tbody/tr/td').click()
time.sleep(1)
#供方资料
driver.find_element_by_xpath('//div[2]/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[5]/div/div/div/div[2]/div/button').click()
time.sleep(1)
#合并退货
driver.find_element_by_xpath('//div[2]/button[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[3]/div/div/div/div/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//span[2]/img').click()
time.sleep(1)
#重新采购
driver.find_element_by_xpath('//button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div/div[2]/div/button[2]').click()
time.sleep(2)
#登记
driver.find_element_by_xpath('//div[4]/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
try:
	driver.find_element_by_xpath('//div[4]/div/div[7]/div/div/div[2]/button[1]').click()
except:
	pass

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))

driver.close()
fp.close()
driver.close()