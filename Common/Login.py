#!/usr/bin/env python
# -*- coding: cp936 -*-
from Common.SetUp import setup
from selenium import webdriver
from Util.write_fail_log import write_fail_log
from Util.write_pass_log import write_pass_log

import time
class Login:
    def __init__(self):
        self.driver=setup().driver
    def login(self,dict):
        self.driver.find_element_by_id("phone1").clear()
        self.driver.find_element_by_id("phone1").send_keys(dict["username"])
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(dict["passwd"])
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div/div[3]/div[5]/input").click()
        return self.driver

    def assert_suc(self, dict, exception):
        # 正确的账户和密码
        self.driver = Login().login(dict)
        text = self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[5]/a").text
        try:
            if exception in text:
                write_pass_log("right username and passwd case pass!!!")
        except Exception as e:
            write_fail_log("right username and passwd case  fail!!!result is" + e)
        self.driver.implicitly_wait(10)
        self.driver.close()

    def assert_fail(self, dict, exception):
        self.driver = Login().login(dict)
        text = self.driver.find_element_by_xpath("//*[@id='J_alertBox']/p").text
        self.driver.implicitly_wait(10)
        # print(text)
        if exception in text:
            write_pass_log("the test case pass!!!")
        else:
            write_fail_log("the test case fail!!!result is" + exception)
        self.driver.implicitly_wait(10)
        self.driver.close()

    def assert_null(self, dict, exception):
        # 正确的密码，空的手机号
        self.driver = Login().login(dict)
        text = self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div/div[3]/div[1]/p").text
        self.driver.implicitly_wait(10)
        # print(text)
        if exception in text:
            write_pass_log("the test case pass!!!")
        else:
            write_fail_log("the test case fail!!!result is" + exception)
        self.driver.implicitly_wait(10)
        self.driver.close()

    def assert_null1(self, dict, exception):
        # 正确的手机号，空的密码
        self.driver = Login().login(dict)
        text = self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div/div[3]/div[2]/p").text
        self.driver.implicitly_wait(10)
        # print(text)
        if exception in text:
            write_pass_log("the test case pass!!!")
        else:
            write_fail_log("the test case fail!!!result is" + exception)
        self.driver.implicitly_wait(10)
        self.driver.close()

    def forget_passwd(self, dict, exception):
        # 忘记密码
        self.driver = setup().driver
        self.driver.find_element_by_id("phone1").clear()
        self.driver.find_element_by_id("phone1").send_keys(dict["username"])
        self.driver.find_element_by_link_text("忘记密码").click()
        self.driver.find_element_by_id("phone").clear()
        self.driver.find_element_by_id("phone").send_keys(dict["username"])
        verifyCode = input("please input your verifycode:")
        self.driver.implicitly_wait(120)
        self.driver.find_element_by_id("verifyCode").clear()
        self.driver.find_element_by_id("verifyCode").send_keys(verifyCode)
        self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div/div[3]/input").click()
        smsVerifyCode = input("please input your smsVerifyCode:")
        self.driver.find_element_by_id("smsVerifyCode").clear()
        self.driver.find_element_by_id("smsVerifyCode").send_keys(smsVerifyCode)
        self.driver.implicitly_wait(120)
        self.driver.find_element_by_id("pwd").send_keys(dict["passwd"])
        self.driver.find_element_by_id("repwd").send_keys(dict["passwd"])
        self.driver.find_element_by_xpath("//*[@id='app']/div[1]/div/div/div/div[5]/input").click()
        # self.driver.implicitly_wait(10)
        text=self.driver.find_element_by_xpath(".//*[@id='app']/div[1]/div/p").text
        if exception in text:
            pass
f=Login()
dict={"username":"18030839210","passwd":123456}
f.login(dict)