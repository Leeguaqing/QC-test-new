# 执行文件
# 导入文件
from common import test
from test_date import test_date
from selenium import webdriver

driver = webdriver.Edge()  # 注意大小写
# 加一个隐式等待
driver.implicitly_wait(10)

# 调用函数 1、先将参数取出来  2、传参到函数调用里
url = test_date.url['url']
username = test_date.login_date['username']
password = test_date.login_date['password']
s_key = test_date.s_key["s_key"]

# 函数调用 传参
# 给函数定义了一个返回值--调用的时候一个变量接收返回值
result = test.search_key(url,driver,username,password,s_key)
if s_key in result:
    print("测试用例通过")
else:
    print("测试用例不通过")
