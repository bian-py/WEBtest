import os
from time import sleep
import allure
import pytest
from page.page_login import PageLogin
from tool.get_driver import GetDriver
import page
from tool.get_log import GetLogger
from tool.read_yaml import read_yaml
from tool.server_bat import WinRM

log = GetLogger.get_log()


class TestLogin:

    @classmethod
    def setup_class(cls):
        WinRM().run_bat_file()
        cls.driver = GetDriver.get_web_driver(page.URL)
        cls.login = PageLogin(cls.driver)

    @classmethod
    def teardown_class(cls):
        GetDriver().quit_web_driver()

    @pytest.mark.parametrize("username,password,code", read_yaml("login11.yaml"))
    def test_login(self, username, password, code):
        self.login.page_login(username, password, code)
        if not self.login.page_if_success():
            log.info('未登录成功')
            try:
                text = self.login.page_get_error_text()
                log.info(f'正在进行断言,获取断言关键字{text}')
                assert self.login.page_get_error_text() in \
                       ('用户名不能为空!', '密码错误!', '账号格式不匹配!', '密码不能为空!',
                        '账号不存在!78789', '验证码错误', '验证码不能为空!')
            except Exception as e:
                log.error(f"断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
            finally:
                sleep(3)
                try:
                    self.login.page_click_error_btn()
                finally:
                    log.info('返回首页')
                    self.login.page_return_FP()

        else:
            log.info('未登录成功')
            try:
                log.info('正在进行断言')
                assert self.login.page_logout_text() == "安全退出"
            except Exception as e:
                log.error(f"断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
            sleep(3)
            log.info('正在登出')
            self.login.page_click_logout()

            #
# if __name__ == '__main__':
# # a = PageLogin(GetDriver().get_web_driver(page.URL))
# # print(a)
#     print(TestLogin.login)
#     print(TestLogin.driver)
#     try:
#         TestLogin().test_login()
#     finally:
#         print(TestLogin.login)
# # driver = GetDriver().get_web_driver(page.URL)
# # PageLogin(driver).page_login()
