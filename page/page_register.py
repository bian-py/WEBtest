import page
from base.base import Base
from tool.get_log import GetLogger

log = GetLogger.get_log()


class PageRegister(Base):

    def page_click_register_link(self):
        self.base_click_element(page.register_link)

    def page_click_register_phone_link(self):
        self.base_click_element(page.register_phone_link)

    def page_click_register_email_link(self):
        self.base_click_element(page.register_email_link)

    def page_input_register_username(self, username):
        self.base_input_text(page.register_username, username)

    def page_input_register_password(self, password):
        self.base_input_text(page.register_password, password)

    def page_input_register_code(self, code):
        self.base_input_text(page.register_code, code)

    def page_input_register_confirm_password(self, password):
        self.base_input_text(page.register_password_confirm, password)

    def page_input_register_invite_phone(self, phone):
        self.base_input_text(page.register_invite_phone, phone)

    def page_click_register_agree_protocol(self):
        self.base_click_element(page.register_agree_protocol)

    def page_click_register_submit_btn(self):
        self.base_click_element(page.register_submit_btn)

    def page_click_logout(self):
        self.base_click_element(page.logout)

    def page_logout_text(self):
        return self.base_get_text(page.logout)

    def page_get_register_error_text(self):
        return self.base_get_text(page.register_error_text)

    def page_click_register_error_btn(self):
        self.base_click_element(page.register_error_btn)

    def page_if_register_success(self):
        el = None
        try:
            el = self.base_find_element(page.logout, 10)
            print("注册成功")
        except:
            print("注册失败")
        finally:
            if el:
                return True
            else:
                return False

    def page_register_return_FB(self):
        self.base_click_element(page.register_error_return)
        self.base_click_element(page.login_return)

    def page_register(self, username, password, password2, code, phone):
        log.info(f'调用手机号注册业务组合方法，用户名为{username},密码为{password},'
                 f'确认密码{password2},验证码{code},推荐人手机号{phone}')
        self.page_click_register_link()
        self.page_input_register_username(username)
        self.page_input_register_password(password)
        self.page_input_register_code(code)
        self.page_input_register_confirm_password(password2)
        self.page_input_register_invite_phone(phone)
        self.page_click_register_submit_btn()

    def page_register_email(self, username, password, password2, code, phone):
        log.info(f'调用邮箱注册业务组合方法，用户名为{username},密码为{password},'
                 f'确认密码{password2},验证码{code},推荐人手机号{phone}')
        self.page_click_register_link()
        self.page_click_register_email_link()
        self.page_input_register_username(username)
        self.page_input_register_password(password)
        self.page_input_register_code(code)
        self.page_input_register_confirm_password(password2)
        self.page_input_register_invite_phone(phone)
        self.page_click_register_submit_btn()
