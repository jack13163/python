#!/usr/bin/python
#coding: utf-8
#自动化测试脚本
#当出现selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 错误时
#需要卸载selenium，安装低版本的selenium

#导入selenium命名空间
from selenium import webdriver

#获取火狐浏览器的句柄对象
driver = webdriver.Ie()

#打开连接
driver.get("http://www.baidu.com")

#获取表单元素，并设置表单元素的值
driver.find_element_by_id('kw').send_keys('selenium')

#提交表单
driver.find_element_by_id('su').click()

#退出浏览器
#driver.quit()