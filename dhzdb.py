#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://docker30-erp.qipeipu.net/#login/10000")
time.sleep(2)
#账号
account = driver.find_element_by_id('account')
account.send_keys('pss')
#密码
pwd = driver.find_element_by_id('password')
pwd.send_keys('123456')
#登录
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div/div[6]/button[2]').click()
time.sleep(2)
#选中第一个厂牌，确认
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[4]/div/ul/li[1]/span').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[4]/div/div[2]/button').click()
#悬停在卖家中心，点击
above= driver.find_element_by_xpath('//*[@id="menu"]/li[2]/span/span[2]')
ActionChains(driver).move_to_element(above).perform()
#订货自动报
driver.find_element_by_xpath('//*[@id="menu"]/li[2]/ul/li[14]/a').click()
#移走鼠标
above = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div/input')
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)

#查询框
input = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div/input')
input.clear()
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[1]/div/div/button/i').click()
time.sleep(2)

#综合查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/button').send_keys(Keys.F2)
time.sleep(1)
#查询
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/div[2]/div/div/div/div[2]/div/button[1]').click()
time.sleep(1)

#修改
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[3]/div/div/div[2]/div/button[1]').click()
time.sleep(1)

#新增
#time.sleep(1)
#text = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[3]/div/div/h3/span[1]').text
#print(text)
#driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[3]/div/div/div[2]/div/button[1]').click()

#删除
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[6]/div/div/div[2]/button[2]').send_keys(Keys.ESCAPE)

#批量调价
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[5]/div/div/div[2]/div/button[1]').click()

#批量调天数
#driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[1]/label/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[5]').click()
time.sleep(1)
text = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[6]/div/div/h3').text
print(text)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[6]/div/div/div[2]/div/button[1]').click()
time.sleep(2)

#全部删除
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[6]').click()
time.sleep(1)
text = driver.find_element_by_xpath('//*[@id="app"]/div[6]/div/div/div[1]').text
print(text)
driver.find_element_by_xpath('//*[@id="app"]/div[6]/div/div/div[2]/button[2]').click()

#调整历史
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/button[7]').click()
time.sleep(1)
text = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[8]/div/div/h3/span[1]').text
print(text)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[8]/div/div/div[2]/div/button').click()
time.sleep(1)
#下载模板
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/ul/li[1]/a/img').click()
time.sleep(3)
#导入
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/ul/li[2]/img').click()
time.sleep(1)
text = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[4]/div/div/h3/span[1]').text
print(text)
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[4]/div/div/div[2]/div/button').click()
time.sleep(1)
#导出
driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div[1]/ul/li[3]/img').click()




time.sleep(5)
driver.quit()



























