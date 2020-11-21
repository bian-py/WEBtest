import os

import pytest

import page
from page.page_register import PageRegister
from tool.get_driver import GetDriver
from tool.get_log import GetLogger
from tool.read_sql import read_sql
from tool.read_yaml import read_yaml
from tool.server_bat import WinRM

log = GetLogger.get_log()


class TestRegister:

    @classmethod
    def setup_class(cls):
        WinRM().run_bat_file()
        cls.driver = GetDriver.get_web_driver(page.URL)
        cls.register = PageRegister(cls.driver)
        read_sql('tp_users.sql')

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username, password, password2, code, phone,expect", read_yaml('register.yaml'))
    def test_register(self, username, password, password2, code, phone, expect):
        self.register.page_register(username, password, password2, code, phone)
        if self.register.page_if_register_success():
            log.info('正向用例，注册成功')
            if expect == '':
                try:
                    log.info('断言是否注册成功')
                    assert self.register.page_logout_text() == '安全退出'
                except Exception as e:
                    log.error(f"断言失败:{e}")
                    module_name = str(os.path.basename(__file__)).split('.')[0]
                    self.register.base_get_screenshot(module_name)
                    raise
                finally:
                    log.info('安全退出')
                    self.register.page_click_logout()
            else:
                log.info('正向用例，注册失败')
                log.error(f"错误的用例，能够成功注册，用例不通过")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.register.base_get_screenshot(module_name)
                self.register.page_click_logout()
                raise Exception("错误的用例，能够成功注册，用例不通过")

        else:
            log.info('逆向用例')
            try:
                log.info('正在进行错误信息断言')
                assert self.register.page_get_register_error_text() == expect

            except Exception as e:
                log.error(f"断言失败，信息有误或无提示：{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.register.base_get_screenshot(module_name)
                raise

            finally:
                try:
                    self.register.page_click_register_error_btn()
                except Exception as e:
                    log.error(f"无错误提示框{e}")
                    raise
                finally:
                    self.register.page_register_return_FB()

    @pytest.mark.parametrize("username, password, password2, code, phone, expect", read_yaml('register_email.yaml'))
    def test_register_email(self, username, password, password2, code, phone, expect):
        self.register.page_register_email(username, password, password2, code, phone)
        if self.register.page_if_register_success():
            log.info('正向用例，注册成功')
            if expect == '':
                try:
                    log.info('断言是否注册成功')
                    assert self.register.page_logout_text() == '安全退出'
                except Exception as e:
                    log.error(f"断言失败:{e}")
                    module_name = str(os.path.basename(__file__)).split('.')[0]
                    self.register.base_get_screenshot(module_name)
                    raise
                finally:
                    self.register.page_click_logout()
            else:
                log.error(f"错误的用例，能够成功注册，用例不通过")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.register.base_get_screenshot(module_name)
                self.register.page_click_logout()
                self.register.page_click_logout()
                raise Exception("错误的用例，能够成功注册，用例不通过")

        else:
            log.info('逆向用例')
            try:
                log.info('正在进行错误信息断言')
                assert self.register.page_get_register_error_text() == expect

            except Exception as e:
                log.error(f"断言失败，信息有误或无提示：{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.register.base_get_screenshot(module_name)
                raise

            finally:
                try:
                    self.register.page_click_register_error_btn()
                except Exception as e:
                    log.error(f"无错误提示框{e}")
                    raise
                finally:
                    self.register.page_register_return_FB()
