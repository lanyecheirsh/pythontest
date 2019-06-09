#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from public import Login 
import time
import sys

cputimestart = time.process_time()
runtimestart = time.perf_counter()
#结果日志
fp = open('stockln_log.txt','w')
sys.stderr = fp
sys.stdout = fp
#打开chrome浏览器
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get('http://docker30-erp.qipeipu.net/#/login/10000')

Login().user_login(driver)

# account = driver.find_element_by_id('account')
# #输入账号密码
# account.send_keys('erp')
# pwd = driver.find_element_by_id('password')
# pwd.send_keys('123')
# #点击【登录】
# driver.find_element_by_class_name('btn-group').click()
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
mouse = driver.find_element_by_xpath('//*[@id="app"]/div[3]/ul[1]/li[4]/span/span[1]')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
#点击二级菜单-散件入库
driver.find_element_by_xpath('//*[@id="app"]/div[3]/ul[1]/li[4]/ul/li[1]/a').click()
#将鼠标移动开
mouse = driver.find_element_by_xpath('//button')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)

#点击新建
driver.find_element_by_xpath('//button').click()
#输入DG，选择第一个
driver.find_element_by_xpath('//input').send_keys('dg')
time.sleep(1)
driver.find_element_by_xpath('//div[2]/div/div/ul/li').click()
#点击库存并选择第一个
driver.find_element_by_id('warehouse').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/select/option').click()
#输入业务员和备注
driver.find_element_by_id('agent').send_keys('ywy')
driver.find_element_by_id('remark').send_keys('testrm')
#点击保存
driver.find_element_by_id('saveStockInBill').click()
time.sleep(1)
#点击取消单据并取消
driver.find_element_by_xpath('//button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[13]/div/div/div[2]/button[2]').click()
#添加配件
driver.find_element_by_xpath('//div[5]/div/div[2]/button').click()
time.sleep(1)
#浏览
driver.find_element_by_xpath('//div[3]/div/div/span').click()
#查询
driver.find_element_by_xpath('//div[6]/div/div/div/div/div/div/button').click()
time.sleep(1)
driver.find_element_by_id('filterPartsCode').send_keys('888')

driver.find_element_by_id('filterPartsName').send_keys('大灯')
driver.find_element_by_id('filterCarType').send_keys('test')
driver.find_element_by_xpath('//div[2]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/input').send_keys('1') 
time.sleep(1)
driver.find_element_by_id('confirmPartEdit').click()
driver.find_element_by_xpath('//div[3]/button[2]').click()
time.sleep(1)
#点击修改，输入2，确定
driver.find_element_by_xpath('//div[5]/div/div[2]/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[4]/input').send_keys('2') 
driver.find_element_by_id('confirmPartEdit').click()
driver.find_element_by_xpath('//div[3]/button[2]').click()

#点击删除并取消
driver.find_element_by_xpath('//div[5]/div/div[2]/button[3]').click()
driver.find_element_by_xpath('//div[13]/div/div/div[2]/button[2]').click()
#价格调整然后取消
driver.find_element_by_xpath('//button[5]').click()
driver.find_element_by_xpath('//div[8]/div/div/div[2]/div/button').click()
#整单费用然后取消
time.sleep(1)
driver.find_element_by_xpath('//button[6]').click()
#单项费用
driver.find_element_by_id('freight').send_keys('11')
driver.find_element_by_xpath('//div[2]/div/div/div/input').send_keys('1')
time.sleep(1)
driver.find_element_by_xpath('//div[3]/div/div/ul/li').click()
driver.find_element_by_xpath('//div[11]/div/div/div/div/div[2]/div/input').send_keys('22')
driver.find_element_by_xpath('//div[2]/div[2]/div/div/div/input').send_keys('2')
time.sleep(1)
driver.find_element_by_xpath('//div[4]/div/div/ul/li').click()
driver.find_element_by_xpath('//div[11]/div/div/div/div/div[3]/div/input').send_keys('33')
driver.find_element_by_xpath('//div[3]/div[2]/div/div/div/input').send_keys('3')
time.sleep(1)
driver.find_element_by_xpath('//div[3]/div[2]/div/div/div/input').clear()
# driver.find_element_by_xpath('//div[5]/div/div/ul/li').click()

driver.find_element_by_xpath('//div[11]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#单项费用然后取消
driver.find_element_by_xpath('//button[7]').click()
driver.find_element_by_xpath('//div[11]/div/div/div/div/div/div/input').clear()
driver.find_element_by_xpath('//div[11]/div/div/div/div/div/div/input').send_keys('1')
driver.find_element_by_xpath('//div[11]/div/div/div/div/div[2]/div/input').clear()
driver.find_element_by_xpath('//div[11]/div/div/div/div/div[2]/div/input').send_keys('2')
driver.find_element_by_xpath('//div[11]/div/div/div/div/div[3]/div/input').clear()
driver.find_element_by_xpath('//div[11]/div/div/div/div/div[3]/div/input').send_keys('3')
driver.find_element_by_xpath('//div[11]/div/div/div[2]/div/button[2]').click()
time.sleep(1)
#重置费用然后取消
driver.find_element_by_xpath('//button[8]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[13]/div/div/div[2]/button[2]').click()
#提交，选择不打印
driver.find_element_by_xpath('//div[5]/div/div[2]/button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//div[7]/div/div/div/div[2]/div/button[2]').click()

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print( '%s : sucess!' %now)
cputimeend = time.process_time()
runtimeend = time.perf_counter()
print('Running time 1：%s Senconds'%(cputimeend-cputimestart))
print('Running time 2：%s Senconds'%(runtimeend-runtimestart))
fp.close()
driver.close()