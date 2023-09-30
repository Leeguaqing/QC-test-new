# 实现功能的代码
import time
from selenium import webdriver

def login_page(username,password,driver):# 形参   --参数化   --提高代码复用率
    # 找到username这个id的元素--点，输入内容
    driver.find_element("id","username").send_keys(username)
    driver.find_element("id","password").send_keys(password)
    driver.find_element("id","btnSubmit").click()

def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element("xpath","//span[text() = '零售出库']").click()
    driver.switch_to.frame(1)
    driver.find_element("id","searchNumber").send_keys(s_key)
    driver.find_element("xpath","//span[@class ='l-btn-text icon-search l-btn-icon-left']").click()
    test_date = driver.find_element("xpath","//tr[@id = 'datagrid-row-r1-2-0']//td[@field = 'number']//div").text
    return test_date

