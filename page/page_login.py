from selenium import webdriver

import page
from base.base import Base
from tool.get_driver import GetDriver
from tool.get_log import GetLogger

log = GetLogger.get_log()


class PageLogin(Base):

    def page_click_login(self):
        self.base_click_element(page.login_link)

    def page_input_username(self, username):
        self.base_input_text(page.login_username, username)

    def page_input_password(self, password):
        self.base_input_text(page.login_password, password)

    def page_input_code(self, code):
        self.base_input_text(page.login_code, code)

    def page_click_login_btn(self):
        self.base_click_element(page.login_btn)

    def page_click_code_img(self):
        self.base_click_element(page.login_code_img)

    def page_get_error_text(self):

        return self.base_get_text(page.login_error)

    def page_click_error_btn(self):
        self.base_click_element(page.login_error_btn)

    def page_if_success(self):
        log.info('判断是否登录成功')
        self.el = None
        try:
            self.el = self.base_find_element(page.logout, 10)
        except Exception:
            log.info("未登录成功,返回False")
        finally:
            if self.el:
                log.info('登录成功，返回True')
                return True
            else:
                return False

    def page_logout_text(self):
        return self.base_get_text(page.logout)

    def page_click_logout(self):
        self.base_click_element(page.logout)

    def page_return_FP(self):
        self.base_click_element(page.login_return)

    def page_keep_return_FP(self):
        self.base_click_element(page.cart_user_back)

    def page_login(self, username='1234@qq.com', password="123456", code="8888"):
        log.info(f'调用组合业务登录方法，登录用户名为{username},密码{password},验证码{code}')
        self.page_click_login()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_code(code)
        self.page_click_login_btn()


if __name__ == "__main__":
    driver = GetDriver().get_web_driver(page.URL)
    PageLogin(driver).page_login()
    b = 0
    b = PageLogin(driver).page_get_error_text()
    print(b)
    GetDriver().quit_web_driver()
