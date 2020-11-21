from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
h = driver.current_window_handle
print(h)
driver.find_element_by_link_text('贴吧').click()
sleep(10)
hs = driver.window_handles
print(hs,type(hs))