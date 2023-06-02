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
# 切换到左侧菜单导航栏
driver.switch_to_frame("function_panel_index")
sleep(1)
driver.switch_to_frame("menu_main")
sleep(1)
# 点击系统管理
driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td[3]/a").click()
# 点击组织机构管理
driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td/table[1]/tbody/tr/td[4]/a").click()
# 点击“用户及权限”菜单
driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td/table[2]/tbody/tr/td/table[3]/tbody/tr/td[5]/a").click()
# # 切换到中间的页面显示frame
driver.switch_to_default_content()
driver.switch_to_frame("table_index")
driver.switch_to_frame("table_main")
driver.switch_to_frame("edu_main")
sleep(1)
# 点击新建按钮
driver.find_element_by_xpath("/html/body/table[1]/thead[1]/tr/td/table/thead/tr/td[1]/input[1]").click()
sleep(1)
# 新增用户
driver.find_element_by_name("USER_ID").send_keys("test")
driver.find_element_by_name("USER_NAME").send_keys("张三")
driver.find_element_by_name("TEL_NO_DEPT").send_keys("12345678907")
driver.find_element_by_name("")

# sleep(2)
# # 退出系统
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div/span").click()
# sleep(2)
# # 切换到确定退出弹出框
# driver.switch_to_alert().accept()
# sleep(2)
# # 关闭浏览器
# driver.quit()
