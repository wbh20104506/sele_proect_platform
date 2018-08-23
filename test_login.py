# coding：utf-8

import unittest
from selenium import webdriver
import time

class test1(unittest.TestCase):
    u'''测试登陆功能点'''

    def test_001(self):
        u'''测试登陆：账号：admin，密码：root123'''
        driver=webdriver.Chrome()
        driver.get("http://192.168.0.76:8089/Aboard/#!/login?returnTo=%2Flogin")

        time.sleep(2)
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("root123")
        driver.find_element_by_id("loginBtn").click()

        time.sleep(2)
        s=driver.find_element_by_css_selector(".welcome-msg.ng-binding").text
        # print(s)
        self.assertTrue(s=="欢迎, Administrator")
        self.assertEqual(s,"欢迎, Administrator")    ## 判断实际结果和期望结果相等

if __name__=="__main__":
    unittest.main()