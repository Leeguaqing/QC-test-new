"""
web 自动化：
代码                翻译（中间人）               浏览器
python             浏览器驱动                   edge
selenium:python的工具 三个部分 --了解
1)ide :录制脚本 -- 用的少
2)webdriver:库 -- 提供对网页的各种操作 + 结合语言使用  -- python java   --重点
3)grid 分布式 --用的少

"""
import time
from time import sleep
from selenium import webdriver
driver = webdriver.Edge()
driver.implicitly_wait(10)# 隐式等待，默认等待10s == 最多等到10S，提前出线了就不继续等待
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()
# driver.find_element("id","username").send_keys("123456")
# sleep(3)
# driver.find_element("id","password").send_keys("123456")
# sleep(3)
# driver.find_element("id","btnSubmit").click()
"""driver.refresh()
driver.minimize_window()
driver.quit()# 关闭驱动 会话
driver.close()"""
driver.find_element("xpath","//input[@id = 'username']").send_keys("test123")
driver.find_element("id","password").send_keys("123456")
text = driver.find_element("xpath","//div[@class = 'login-logo']//b").text#获取文本
if text == "柠檬ERP":
    print("标题无误")
else:
    print("测试用例不通过")
# text_2 = driver.find_element("xpath","//b[text() = '柠檬ERP']").text
# print(text_2)
driver.find_element("xpath","//button[@type  = 'submit']").click()
# text_2 = driver.find_element("xpath", "//div[@class = 'pull-left info']//p").text
text_2 = driver.find_element("xpath","//p[text() = '测试用户']").text#文本属性定位
if text_2 == "测试用户":
    print("账户正确")
else:
    print("测试用例不通过")
text_title = driver.title
if text_title == "柠檬ERP":
    print("标题正确")
else:
    print("测试用例不通过")
print('-------------')
# 点击零售管理
# driver.find_element("xpath","//span[text() = '零售管理']").click()
# 点击零售出库
driver.find_element("xpath","//span[text() = '零售出库']").click()

# 因为ID不是唯一的，会随机变化，所以获取上一层一样的id前缀再拼接,
P_id = driver.find_element("xpath","//div[text()='零售出库']/..").get_attribute("id")
F_id = P_id+"-frame"
# print(F_id)
# 方法一：1、通id进行的iframe切换
"""driver.switch_to.frame(F_id)
driver.find_element('id',"searchNumber").send_keys("314")
"""
#方法二：2、通过元素定位(xpath）来切换iframe
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(F_id)))

# 方法三：通过iframe的下标来切换
driver.switch_to.frame(1)
driver.find_element("id","searchNumber").send_keys("258")
driver.find_element('xpath',"//span[text() = '查询']").click()

# 找到单据编号
text_3 = driver.find_element("xpath","//tr[@id = 'datagrid-row-r1-2-0']//td[@field = 'number']//div").text#获取文本
print(text_3)
if '258' in text_3:
    print("编号正确")
else:
    print("测试用例不正确")
