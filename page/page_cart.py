from time import sleep

import page
from base.base import Base
from tool.get_log import GetLogger

log = GetLogger.get_log()


class PageCart(Base):

    def page_cart_click_cart_link(self):
        self.base_click_element(page.cart_link)

    def page_cart_if_empty(self):
        self.el = None
        try:
            self.el = self.base_get_element_values(page.cart_empty, 'style')
            print(self.el)
        except Exception:
            print("购物车不为空")
        finally:
            if not self.el == 'display: none;':
                print('购物车为空，去购物')
                self.page_cart_empty_to_FB()
                return True
            else:
                return False

    def page_cart_empty_to_FB(self):
        self.base_click_element(page.cart_order_back)

    def page_cart_go_zhubao(self):
        self.base_click_element(page.cart_FB_zhubao)

    def page_cart_click_huashengadd(self):
        self.base_click_element(page.cart_huasheng_add)

    def page_cart_click_huashengcut(self):
        self.base_click_element(page.cart_huasheng_cut)

    def page_cart_modify_huasheng_number(self, values):
        self.base_input_text(page.cart_huasheng_number, values)

    def page_cart_get_huasheng_error(self):
        msg = self.base_get_text(page.cart_huasheng_error_msg)
        sleep(2)
        self.base_click_element(page.cart_huasheng_error_btn)
        return msg

    def page_cart_modify_huasheng_number1(self, values):
        self.base_input_text(page.cart_huasheng_number1, values)

    def page_cart_huasheng_commit(self):
        self.base_click_element(page.cart_huasheng_commit)

    def page_cart_huasheng_go_to_cart(self):
        sleep(2)
        self.driver.switch_to.frame(self.base_find_element(page.cart_huasheng_frame))
        # print('111')
        sleep(2)
        self.base_click_element(page.cart_huasheng_go)
        # print('111')
        self.driver.switch_to.default_content()

    def page_get_huasheng_name(self):
        return self.base_get_text(page.cart_huasheng_name1)

    def page_get_huasheng_price(self):
        return self.base_get_text(page.cart_huasheng_price1)

    def page_get_cart_huasheng_name(self):
        return self.base_get_text(page.cart_huasheng_name2)

    def page_get_cart_huasheng_price(self):
        return self.base_get_text(page.cart_huasheng_price2)

    def page_cart_click_cart_blank(self):
        self.base_click_element(page.cart_blank)

    def page_cart_click_continue_to_shopping(self):
        self.base_click_element(page.cart_continue_btn)

    def page_cart_get_huasheng_number(self):
        return self.base_get_element_values(page.cart_huasheng_number, 'value')

    def page_cart_get_goods_kinds_number(self):
        sleep(5)
        return self.base_get_text(page.cart_goods_number)

    def page_cart_delete_by_x(self):
        self.base_click_element(page.cart_delete_X1)
        sleep(2)
        self.base_click_element(page.cart_delete_X2)
        sleep(2)

    def page_cart_click_add(self):
        self.base_click_element(page.cart_huasheng_add)

    def page_cart_click_cut(self):
        self.base_click_element(page.cart_huasheng_cut)

    def page_cart_check_add_if_enable(self):
        value = self.base_get_element_values(page.cart_huasheng_add, 'class')
        print(value)
        if value == 'increment':
            return True
        else:
            return False

    def page_cart_check_cut_if_enable(self):
        value = self.base_get_element_values(page.cart_huasheng_cut, 'class')
        print(value)
        if value == 'decrement':
            return True
        else:
            return False

    def page_cart_get_huasheng_number1(self, values):
        self.base_input_text(page.cart_huasheng_number1, values)

    def page_cart_check_if_go_detail(self):
        if self.base_find_element(page.cart_detail_check):
            return True
        else:
            return False

    def page_cart_click_good_name(self):
        self.base_click_element(page.cart_huasheng_name2)

    def page_cart_click_good_picture(self):
        self.base_click_element(page.cart_detail_picture)

    def page_cart_get_member_price(self):
        return self.base_get_text(page.cart_huasheng_membergoodsprice)

    def page_cart_get_sub_total(self):
        return self.base_get_text(page.cart_huasheng_market_price)

    def page_cart_click_2_in_3(self):
        self.base_click_element(page.cart_checked_goods)


    def page_cart_get_total(self):
        return self.base_get_text(page.cart_goods_fee)

    def page_cart_go_to_pay(self):
        sleep(2)
        self.base_click_element(page.cart_go_to_pay_btn)

    def page_if_go_to_pay_success(self):
        self.el = None
        try:
            self.el = self.base_find_element(page.cart_order_btn, 10)
        except Exception:
            print("生成订单失败")
        finally:
            if self.el:
                print('生成订单成功，返回主页')
                self.el.click()
                return True
            else:
                return False

    def page_cart_clear_all(self):
        if self.base_find_element(page.cart_checkall).is_selected():
            self.base_click_element(page.cart_remove_all)
            print('已经清空完毕1')
            # sleep(5)
            self.page_cart_empty_to_FB()
        else:
            self.base_click_element(page.cart_checkall)
            self.base_click_element(page.cart_remove_all)
            print('已经清空完毕2')
            # sleep(5)
            self.page_cart_empty_to_FB()
