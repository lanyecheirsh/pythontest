# coding=utf-8
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from public import Login

fp = open("financeconfirm_log.txt", "w")
sys.stderr = fp
sys.stdout = fp

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://docker34-erp.qipeipu.net/#/login/10000')
Login().user_login(driver)

# 跳过报错
try:
    driver.find_element_by_xpath('//div[2]/button').click()
except:
    pass

# 进入财务确认菜单
above = driver.find_element_by_xpath('//*[@id="menu"]/li[7]/span/span[1]/img[2]')
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu"]/li[7]/ul/li[1]/a').click()
time.sleep(2)

# 移开鼠标，点击销售确认 //*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[7]/ul/li[1]
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[7]/ul/li[1]').click()
time.sleep(3)
'''
# 查询
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/button[1]').click()
time.sleep(1)

# 高级查询
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[4]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[4]/div/div[3]/button').click()
time.sleep(1)
# 高级查询-返回
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[4]/button').send_keys(Keys.ESCAPE)
time.sleep(1)

# 确认
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/button[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[3]/div/div/div[2]/div/button[1]').click()
time.sleep(3)

# 勾选已确认-查询,还原操作业务逻辑比较多，UI自动化会比较难
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[3]/label/span[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/button[1]').click()
time.sleep(1)
#还原
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/button[3]').click()
time.sleep(1)
text = driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[5]/div/div/div[1]').text
print(text)
if text != '确定还原':
    print('不是还原弹窗，错误')
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[5]/div/div/div[2]/button[2]').send_keys(Keys.ESCAPE)
#去掉已确认勾选框
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[3]/label/span[2]').click()
time.sleep(1)

#选中销售单
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]').click()
time.sleep(3)
# 打回
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/button[4]').click()
time.sleep(1)

# 打印-悬浮，没有实现
above = driver.find_element_by_css_selector('#finance-confirm > div:nth-child(1) > div.tag-box > div.query-box.clearfix > div.mr16.el-dropdown > button > span')
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
text = driver.find_element_by_css_selector('.el-dropdown-menu.el-popper>li:nth-child(1)').get_attribute('textContent')
print(text)
if text != '实售金额':
    print("打印选项缺失实售金额选项")
text2 = driver.find_element_by_css_selector('.el-dropdown-menu.el-popper>li:nth-child(2)').get_attribute('textContent')
print(text2)
if text2 != '销售金额':
    print("打印选项缺失销售金额选项")

#选中现结收银的第一条数据
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/table/thead/tr/th[1]/label/span').click()
time.sleep(4)
#获取金额
money=driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[9]').get_attribute('textContent')
print(money)
# 收款金额输入框  //*[@id="finance-confirm"]/div[1]/div[2]/div[2]/div[3]/input[1]
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[2]/div[2]/div[3]/input[1]').clear()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[2]/div[2]/div[3]/input[1]').send_keys(money)
time.sleep(1)
# 支付方式下拉选第一个
driver.find_element_by_css_selector('#finance-confirm > div:nth-child(1) > div.out-storage > div:nth-child(2) > div.addition-wrap > select > option:nth-child(2)').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[2]/div[2]/div[3]/button').click()
time.sleep(2)
#确定现结收银
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[4]/div/div/div[2]/div/button[1]').click()

#切换到采购确认
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[7]/ul/li[2]').click()
#driver.find_element_by_css_selector('#finance-confirm > div:nth-child(2) > div.tag-box > div.query-box.clearfix > div.dimension.right > ul > li:nth-child(1)').click()
time.sleep(1)
#查询
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/button[1]').click()
time.sleep(1)
#高级查询
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/div[4]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/div[4]/div/div[3]/button').click()
time.sleep(1)
# 高级查询-返回
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/div[4]/button').click()
time.sleep(1)
#选中第一行，确认
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[3]/div/div/div[2]/div/button[1]').click()
time.sleep(3)

#勾选已确认
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/div[3]/label/span[1]').click()
time.sleep(1)
#查询
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/button[1]').click()
time.sleep(1)
#还原
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[1]/div[2]/button[3]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[5]/div/div/div[2]/button[1]').click()
time.sleep(2)

#点击现结收银
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[2]/ul/li[1]').click()
time.sleep(1)
#获取第一条数据的金额
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]').click()
#现金
driver.find_element_by_css_selector('#finance-confirm > div:nth-child(2) > div.in-storage > div.main-table > div.addition-wrap > select > option:nth-child(2)').click()
time.sleep(1)
#获取采购金额
money = driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[6]/span').get_attribute('textContent')
print(money)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[2]/div[1]/div[3]/input[1]').send_keys(money)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[2]/div[1]/div[3]/button[2]').click()
time.sleep(2)
#确定收银
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[2]/div[4]/div/div/div[2]/div/button[1]').click()
'''
#切换外购入账
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[1]/div[1]/div[2]/div[7]/ul/li[3]').click()
time.sleep(1)
#查询
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[1]/div[2]/button[1]').click()
time.sleep(2)
#综合查询
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[1]/div[2]/div[4]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[1]/div[2]/div[4]/div/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[1]/div[2]/div[4]/button').click()
time.sleep(1)
#确认
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[1]/div[2]/button[2]').click()
time.sleep(2)
driver.find_element_by_css_selector('#finance-confirm > div:nth-child(3) > div.v-layer.external-confirm > div > div > div.v-layer-content > div > div:nth-child(2) > select > option:nth-child(1)').click()
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[3]/div/div/div[2]/div/button[1]').click()
time.sleep(3)

#现结收银
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[2]/ul/li[1]/a').click()
time.sleep(1)
money3=driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[9]').get_attribute('textContent')
print(money3)
#输入框
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[2]/div[1]/div[3]/input[1]').send_keys(money3)
time.sleep(1)
#支付方式-现金
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[2]/div[1]/div[3]/select/option[2]').click()
#清空预付
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[2]/div[1]/div[3]/input[2]').clear()
#备注
beizhu3=driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[2]/div[1]/div[3]/input[3]')
beizhu3.clear()
beizhu3.send_keys('beizhu')
#收银
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[2]/div[1]/div[3]/button[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="finance-confirm"]/div[3]/div[4]/div/div/div[2]/div/button[1]').click()


time.sleep(3)
driver.close()
