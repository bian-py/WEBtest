import os
import time

import allure
from selenium.webdriver.support.wait import WebDriverWait

import page
from config import BASE_PATH

from tool.get_driver import GetDriver
from tool.get_log import GetLogger

log = GetLogger.get_log()


class Base:
    # 初始化driver,调用时传入driver
    def __init__(self, driver):
        log.info(f'正在初始化driver对象{driver}')
        self.driver = driver

    # 显示等待，并将driver传入后面的lambda表达式
    def base_find_element(self, loc, timeout=10, poll=0.5):
        log.info(f'查找元素{loc}')
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click_element(self, loc):
        log.info(f'点击元素{loc}')
        self.base_find_element(loc).click()

    # 输入内容
    def base_input_text(self, loc, values):
        log.info(f'在元素{loc}，输入{values}')
        el = self.base_find_element(loc)
        log.info(f'情况元素{loc}')
        el.clear()
        el.send_keys(values)

    # 获取文本
    def base_get_text(self, loc):
        log.info(f'获取元素{loc}的文本信息')
        return self.base_find_element(loc).text

    # 截图
    def base_get_screenshot(self, module_name):
        path = (BASE_PATH + os.sep + 'image' + os.sep + module_name + '-{}.png').format(
            time.strftime('%Y_%m_%d %H_%M_%S'))
        list1 = path.split('\\')
        list1.reverse()
        filename = list1[0]
        log.info(f'正在截图,截图为{path}')
        self.driver.get_screenshot_as_file(path)
        self.__base_write_img(path,filename)

    # 私有方法，将截图添加到报告中
    def __base_write_img(self, path, filename):
        log.info(f'正在将截图{filename}写入报告中')
        with open(path, 'rb') as f:
            log.info('打开文件')
            allure.attach(f.read(),f'这里是错误原因，截图名字:{filename}', allure.attachment_type.PNG)

    # 获取页面元素属性
    def base_get_element_values(self, loc, value):
        log.info(f'获取元素{loc}属性{value}的值')
        return self.base_find_element(loc).get_attribute(value)

    # 判断元素是否可用
    def base_if_el_is_enabled(self, loc):
        log.info(f"判断元素{loc}是否可用")
        if self.base_find_element(loc).is_enabled():
            log.info('元素可用，返回True')
            return True
        else:
            log.info('元素不可用，返回False')
            return False


if __name__ == '__main__':
    driver = GetDriver.get_web_driver(page.URL)
    b = Base(driver)
    b.base_get_screenshot('111')
