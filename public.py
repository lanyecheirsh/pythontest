#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'a public module'

from selenium import webdriver
import time

#登录
class Login():

    #登录
    def user_login(self,driver):
        driver.find_element_by_id('account').clear()  
        driver.find_element_by_id('account').send_keys('erp')
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys('123')
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div[3]/div/div/div[6]/button[2]").click()
        time.sleep(2)
        #选择厂牌和点击确定
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[4]/div/ul/li[1]/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[4]/div/div[2]/button').click()
        #服务器错误的对话框
        try:
            driver.find_element_by_xpath('//div[2]/button').click()
        except:
            pass

