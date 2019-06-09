0# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from public import Login 
import time
import sys

start = time.process_time()
start_1 = time.perf_counter()

fp = open('manuallybook_log.txt','w')

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
#鼠标悬停在一级菜单-采购管理
mouse = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/ul[1]/li[4]/span/span[1]')
ActionChains(driver).move_to_element(mouse).perform()
#点击二级菜单-手工订货
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/ul[1]/li[4]/ul/li[2]').click()
time.sleep(1)

#将鼠标移动开
mouse = driver.find_element_by_xpath('//button[2]')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)

#点击新建
driver.find_element_by_xpath('//button[text()="新建(W)"]').click()
#输入
driver.find_element_by_xpath('//div[@class="form-row__wrap--item"]/div/div/div/input').send_keys('kdj')
time.sleep(1)
driver.find_element_by_xpath('//body/div[3]/div/div/ul/li[1]').click()
#下拉框
driver.find_element_by_xpath('//div[3]/select').click()
time.sleep(1)
driver.find_element_by_xpath('//option[@value="2"]').click()
#输入供货号和天数
driver.find_element_by_xpath('//div[4]/input').send_keys('123')
driver.find_element_by_xpath('//div[6]/input').send_keys('3')

#点击保存
# driver.find_element_by_xpath('//button[2]').click()
driver.find_element_by_id('saveBookList').click()
time.sleep(1)
#点击转在途并取消
driver.find_element_by_xpath('//button[text()="转在途(S)"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@class="addParts"]/div[3]/div/div/div[2]/button[2]').click()
time.sleep(1)

#点击取消单据并返回
driver.find_element_by_xpath('//button[text()="取消单据"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@class="addParts"]/div[3]/div/div/div[2]/button[2]').click()
time.sleep(1)
# //button[contains(@class,'search-book-list')]
#点击查询
driver.find_element_by_xpath('//div[@class="el-input-group__append"]/button').click()
time.sleep(1)
#点击综合查询
driver.find_element_by_xpath('//button[text()="综合查询(F2)"]').click()
time.sleep(1)
# 填入库存数筛选出有库存配件
driver.find_element_by_xpath('//div[@class="query-content__wrap"]/div[11]/div/input[1]').send_keys('10')
driver.find_element_by_xpath('//button[text()="查询(Enter)"]').click()
time.sleep(3)
#点击添加按钮
driver.find_element_by_xpath('//button[text()="添加(Enter)"]').click()
#点击确定
try:
	driver.find_element_by_xpath('//div[7]/div[3]/div/div/div[2]/button[1]').click()
except:
	pass
try:
	driver.find_element_by_id('addBookDetail').click()
except:
	pass
#点击配件*
time.sleep(1)
driver.find_element_by_xpath('//ul[@class="list-group__wrap"][2]/li[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="manuallyBookGoods"]/div[8]/div/div/h3/span[2]/img').click()
time.sleep(1)
#点击采购
driver.find_element_by_xpath('//ul[@class="list-group__wrap"][2]/li[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[9]/div/div/div[2]/div/button').click()
time.sleep(1)
#点击外购
driver.find_element_by_xpath('//ul[@class="list-group__wrap"][2]/li[3]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[10]/div/div/div[2]/div/button').click()
time.sleep(1)
#点击外司
driver.find_element_by_xpath('//ul[@class="list-group__wrap"][2]/li[4]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[11]/div/div/div[2]/div/button').click()
time.sleep(1)
#点击流量
driver.find_element_by_xpath('//ul[@class="list-group__wrap"][2]/li[5]').click()
time.sleep(2)
driver.find_element_by_xpath('//div[18]/div/div/div[2]/div/button').click()
time.sleep(1)

#点击上下限
driver.find_element_by_xpath('//div[3]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//div[12]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#点击修改
driver.find_element_by_xpath('//div[5]/div[2]/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[7]/div[1]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#点击删除
driver.find_element_by_xpath('//button[text()="删除(D)"]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[7]/div[3]/div/div/div[2]/button[1]').click()
time.sleep(1)

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
end = time.process_time()
end_1 = time.perf_counter()
print('Running time：%s Senconds'%(end-start))
print('Running time 2：%s Senconds'%(end_1-start_1))
fp.close()
driver.close()