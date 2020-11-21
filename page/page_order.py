from time import sleep

from selenium.webdriver.support.select import Select

import page
from base.base import Base
from page.page_cart import PageCart
from tool.get_log import GetLogger

log = GetLogger.get_log()


class PageOrder(Base):

    def page_order_front(self):
        log.info('清空购物车并添加花生到购物车')
        self.cart = PageCart(self.driver)
        self.cart.page_cart_click_cart_link()
        if self.cart.page_cart_if_empty():
            pass
        else:
            print('清空购物车,并返回首页')
            self.cart.page_cart_clear_all()
        handle1 = self.driver.current_window_handle
        print('handle1的值是：', handle1)
        self.cart.page_cart_go_zhubao()
        while True:
            handles = self.driver.window_handles
            print('handles', handles)
            if len(handles) == 1:
                print('继续等待窗口完全打开')
                sleep(1)
            else:
                break
        for h in handles:
            if h != handle1:
                handle2 = h
                print('handle2的值是：', handle2)
                self.driver.switch_to.window(handle2)
        print('切换后handle的值是：', self.driver.current_window_handle)
        self.cart.page_cart_huasheng_commit()
        self.cart.page_cart_huasheng_go_to_cart()
        self.cart.page_cart_go_to_pay()

    def page_order_click_submit_order(self):
        self.base_click_element(page.cart_order_btn)

    def page_order_if_submit_success(self):

        self.el = None
        try:
            self.el = self.base_find_element(page.order_pay_style)
        except Exception:
            print('生成订单失败')
            raise
        finally:
            if self.el:
                print('生成订单成功')
                return True
            else:
                return False

    def page_order_select_pay_style(self):
        self.base_click_element(page.order_pay_hdfk)
        self.base_click_element(page.order_pay_style)
        sleep(5)
        self.base_click_element(page.order_detail)

    def page_order_check_status(self):
        return self.base_get_text(page.order_status)

    def page_get_order_number(self):
        return self.base_get_text(page.order_number)

    def page_confirm_goods(self):
        self.base_click_element(page.order_confirm_goods)
        self.base_click_element(page.order_confirm_goods2)
        sleep(5)

    def page_order_ms_login(self, username='admin', password='123456', code='8888'):
        log.info(f'调用后台管理登录方法，用户名{username},密码{password},验证码{code}')
        self.base_input_text(page.ms_username, username)
        self.base_input_text(page.ms_password, password)
        self.base_input_text(page.ms_code, code)
        self.base_click_element(page.ms_login)

    def page_order_ms_go_to_order_list(self):
        self.base_click_element(page.ms_shop)
        sleep(3)
        self.base_click_element(page.ms_order)
        self.base_click_element(page.ms_order_list)
        sleep(5)

    def page_order_search_order_number(self, order_number):
        self.driver.switch_to.frame(self.base_find_element(page.ms_frame))
        el = self.base_find_element(page.ms_search_key)
        Select(el).select_by_value(page.ms_search_key_order_number)
        self.base_input_text(page.ms_search, order_number)
        self.base_click_element(page.ms_search_btn)

    def page_order_get_order_statues(self):
        statues1 = self.base_get_text(page.ms_statues1)
        statues2 = self.base_get_text(page.ms_statues2)
        statues3 = self.base_get_text(page.ms_statues3)
        return statues1, statues2, statues3

    def page_order_confirm(self, msg='订单已确认'):
        self.base_input_text(page.ms_input_note, msg)
        self.base_click_element(page.ms_confirm_btn)
        self.driver.switch_to.default_content()

    def page_order_go_express(self, msg='已经发货', num='123456789'):
        self.base_input_text(page.ms_input_note, msg)
        self.base_click_element(page.ms_express_btn)
        self.base_input_text(page.ms_input_express_num, num)
        self.base_click_element(page.ms_confirm_express_btn)
        self.driver.switch_to.default_content()

    def page_order_go_pay(self, msg='已经付款'):
        self.base_input_text(page.ms_input_note, msg)
        self.base_click_element(page.ms_pay)
        self.driver.switch_to.default_content()

    # 组合获取订单状态业务方法
    def page_ms_statues(self, order_number):
        log.info("调用后台系统业务组合方法")
        sleep(3)
        self.page_order_ms_go_to_order_list()
        self.page_order_search_order_number(order_number)
        return self.page_order_get_order_statues()

    def page_ms_check(self):
        self.base_click_element(page.ms_check_order)
