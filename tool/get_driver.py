from selenium import webdriver

from tool.get_log import GetLogger

log = GetLogger.get_log()


class GetDriver:
    __driver = None
    __driver2 = None

    @classmethod
    def get_web_driver(cls, url):
        log.info('火狐浏览器驱动')
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.set_window_position(-1000, 0)
            cls.__driver.maximize_window()
            cls.__driver.get(url)
        return cls.__driver

    @classmethod
    def quit_web_driver(cls):
        log.info('关闭火狐浏览器驱动，并置空')
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None

    @classmethod
    def get_web_driver2(cls, url):
        log.info('谷歌浏览器驱动')
        if cls.__driver2 is None:
            cls.__driver2 = webdriver.Firefox()
            # cls.__driver2 = webdriver.Chrome()
            cls.__driver2.set_window_position(0, 0)
            cls.__driver2.maximize_window()
            cls.__driver2.get(url)
        return cls.__driver2

    @classmethod
    def quit_web_driver2(cls):
        log.info('关闭谷歌浏览器驱动，并置空')
        if cls.__driver2 is not None:
            cls.__driver2.quit()
            cls.__driver2 = None
