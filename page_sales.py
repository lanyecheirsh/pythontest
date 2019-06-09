# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from public import Login 
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('sales_log.txt','w')

sys.stderr = fp
sys.stdout = fp



driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('http://docker31-erp.qipeipu.net/#/login/10000')
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
#鼠标悬停在一级菜单-销售管理
mouse = driver.find_element_by_xpath('//*[@id="menu"]/li[6]/span')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-销售开单
driver.find_element_by_xpath('//*[@id="menu"]/li[6]/ul/li[1]/a').click()
time.sleep(1)

#将鼠标移动开
mouse = driver.find_element_by_xpath('//button[2]')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)

font = driver.find_element_by_xpath('//button').value_of_css_property("font-size")
print(font)
if font != '17px':
	print('字体大小不符')

#点击新建
driver.find_element_by_xpath('//button').click()
time.sleep(1)
#新建
driver.find_element_by_xpath('//div[3]/div/div/div[1]/div/div[1]/div/div/div[1]/input').send_keys('gz')
time.sleep(2)
driver.find_element_by_xpath('//body/div[3]/div/div/ul/li[1]').click()
driver.find_element_by_xpath('//*[@id="salesDeliveryInfo"]').send_keys('test')
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div[3]/div/div/div[2]/div/button').click()
time.sleep(1)
#修改
driver.find_element_by_xpath('//div[4]/div/div[1]/div[1]/div[2]/div[1]/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div[3]/div/div/div[2]/div/button').click()
time.sleep(1)
#取消单据
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div[2]/div[1]/button[2]').click()
time.sleep(1)
# 取消
driver.find_element_by_xpath('//div[4]/div/div[20]/div/div/div[2]/button[2]').click()
time.sleep(1)
#配件查询
driver.find_element_by_xpath('//div[2]/div[2]/div[1]/div/div/button').click()
time.sleep(2)
# 综合查询
driver.find_element_by_xpath('//div[3]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//div[3]/div/div/div/div[2]/div/button[1]').click()  # 确定
time.sleep(1)
#快速报价
driver.find_element_by_xpath('//div[4]/div/div[1]/div[2]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div[7]/div/div/div/div[2]/div/button[2]').click()
#外司
driver.find_element_by_xpath('//div[2]/ul[2]/li[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[6]/div/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#报价
driver.find_element_by_xpath('//div[2]/ul/li[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[21]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#配件
driver.find_element_by_xpath('//div[2]/ul/li[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[8]/div/div/div/h3/span[2]/img').click()
time.sleep(1)
#外购
driver.find_element_by_xpath('//div[2]/ul/li[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[18]/div/div/h3/span[2]/img').click()
time.sleep(1)
#图片
driver.find_element_by_xpath('//div[2]/ul/li[5]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[3]/div/div/div/div/div/div/button[2]').click()
time.sleep(1)
#添加
driver.find_element_by_xpath('//div[3]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//div[19]/div/div/div[2]/div/button').click()
time.sleep(3)
driver.find_element_by_xpath('//div[5]/div/div[7]/div/div/div[1]/div/div[7]/div/input').clear()
driver.find_element_by_xpath('//div[5]/div/div[7]/div/div/div[1]/div/div[7]/div/input').send_keys('1')
driver.find_element_by_xpath('//div[9]/input').send_keys('2')
driver.find_element_by_xpath('//div[7]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#选择配件
driver.find_element_by_xpath('//div[3]/div[3]/div/div[2]/div[2]/table/tbody/tr/td').click()
#修改
driver.find_element_by_xpath('//div[3]/div[2]/button[2]').click()
driver.find_element_by_xpath('//div[5]/div/div[7]/div/div/div[1]/div/div[7]/div/input').clear()
driver.find_element_by_xpath('//div[5]/div/div[7]/div/div/div[1]/div/div[7]/div/input').send_keys('2')
driver.find_element_by_xpath('//div[7]/div/div/div[2]/div/button[2]').click()
#占用单
driver.find_element_by_xpath('//div[3]/div[2]/button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[14]/div/div/div/div[2]/div/button').click()
#整单打折
driver.find_element_by_xpath('//button[5]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[20]/div/div/div[2]/div/button[2]').click()
#新编码
driver.find_element_by_xpath('//button[6]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[17]/div/div/div[2]/div/button[2]').click()
#提交
driver.find_element_by_xpath('//div[2]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//div[22]/div/div/div[2]/button').click()

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))
fp.close()
driver.close()