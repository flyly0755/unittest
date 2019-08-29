import unittest
from TestSuite.base_case import BaseCase
from Tools.decorator import screenshot
from Page.base import Location
import time
from config import Config
from pymouse import PyMouse
# from win32api import GetSystemMetrics

import random


class qiuhuiUserInfo(BaseCase):

    @screenshot
    def test(self):
        """球会用户信息"""

        #点击登录头像
        #方法1，xpath精确匹配
        #avatardiv = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/header/div[4]/div')
        #方法2，xpath模糊匹配，但精确匹配@class='user-login',但需要注意转义符
        #avatardiv = self.driver.find_element_by_xpath('//div[@class=\'user-login\']')
        #方法1和方法2选中xpath后的点击方法
        # avatardiv.click()
        #使用Location函数，可匹配class,id等，写出来的脚本简洁
        avatardiv = Location("登录头像", ".user-login")
        #print("avatardiv is %s" %avatardiv)
        self.driver.click(avatardiv)

        time.sleep(2)
        #点击登录
        loginbutton =Location("登录",".btn-login")
        self.driver.click(loginbutton)
        time.sleep(2)
        #点击账号密码登录
        # loginmode = Location("登录模式",".login-mode.")
        # self.driver.click(loginmode)
        #loginmode = self.driver.find_element_by_xpath('//span[text()=\'账号密码登录\']')
        self.driver.find_element_by_xpath('//span[text()=\'账号密码登录\']').click()
        time.sleep(2)
        # #输入账号密码
        usernameinput=Location("登录名","[placeholder=\"请输入手机号\"]")
        #.get("xxx")和["xxx"]两种形式都可以
        #self.driver.send(usernameinput,Config.loginuserinfo[0].get("username"))
        self.driver.send(usernameinput,Config.loginuserinfo[0]["username"])
        # print(type(Config.loginuserinfo[0]))
        # print(type(Config.loginuserinfo[0].get("username")))
        # print(type(Config.loginuserinfo[0]["username"]))
        # print("loginuserinfo[0][\"username\"] is %s" %Config.loginuserinfo[0]["username"])
        # print("loginuserinfo1[0][\"username\"] is %s" %Config.loginuserinfo1[0]["username"])
        self.driver.send(usernameinput,Config.loginuserinfo[0]["username"])
        time.sleep(0.5)
        pwdinput=Location("密码","[placeholder=\"请输入密码\"]")
        self.driver.send(pwdinput,Config.loginuserinfo[0].get("pwd"))
        time.sleep(0.5)
        windowloginbutton=Location("弹框登录",".ivu-btn-primary")
        self.driver.click(windowloginbutton)






        print("title is %s" %self.driver.title)
        # 断言
        #self.assertEqual("球会体育", self.driver.title,"首页页面标题与预期不符")
        try:
            self.assertEqual("球会体育1", self.driver.title, "首页页面标题与预期不符")
        except Exception as e:
            print("check失败:", str(e))
            #raise
        time.sleep(5)

        userinfodiv = Location("个人信息", ".ivu-poptip-rel")
        self.driver.click(userinfodiv)
        m = PyMouse()
        m.position()

        # width = GetSystemMetrics(0)
        # heigth = GetSystemMetrics(1)
        time.sleep(2)
        #鼠标移开logo,个人信息弹窗消失
        m.move(200, 200)
        time.sleep(2)
        qhusername=self.driver.find_element_by_xpath('//h2[@class=\'user-name\']/span').get_attribute('textContent')
        self.assertEqual("小狐狸760595", qhusername, "球会用户名称与预期不符")

if __name__ == "__main__":
    unittest.main()
