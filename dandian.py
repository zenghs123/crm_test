# 导入seleniu 模块
from selenium import webdriver
# 导入时间工具类
from time import sleep
# 创建浏览器对象
driver = webdriver.Firefox()
# 浏览器打开单点项目登录页面
driver.get("http://192.168.10.254:81/general/ERP/LOGIN/")
sleep(2)
# 定位用户名，密码框，输入用户名密码
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("")
# 点击登录按钮登录页面
driver.find_element_by_name("imageField").click()
sleep(4)
driver.switch_to_frame("topFrame")
sleep(2)
# 退出系统
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/span").click()
sleep(2)
# 切换到确定退出弹出框
driver.switch_to_alert().accept()
sleep(2)
# 关闭浏览器
driver.quit()
