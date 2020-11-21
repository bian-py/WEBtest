import os
from time import sleep

import pytest

import page
from page.page_cart import PageCart
from page.page_login import PageLogin
from tool.get_driver import GetDriver
from tool.get_log import GetLogger
from tool.read_sql import read_sql
from tool.read_yaml import read_yaml
from tool.read_yaml_sigle import read_yaml_sigle
from tool.server_bat import WinRM

log = GetLogger.get_log()


class TestCart:

    @classmethod
    def setup_class(cls):
        WinRM().run_bat_file()
        cls.driver = GetDriver.get_web_driver(page.URL)
        cls.cart = PageCart(cls.driver)
        cls.login = PageLogin(cls.driver)
        cls.login.page_login()
        cls.login.page_keep_return_FP()

        # cls.cart.page_cart_click_cart_link()

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_web_driver()
        # pass

    @pytest.mark.flaky(rerun=1, rerun_delay=2)
    @pytest.mark.run(order=1)
    def test01_cart_empty(self):
        log.info('验证无商品时购物车为空')
        self.cart.page_cart_click_cart_link()
        try:
            assert self.cart.page_cart_if_empty()
        except Exception as e:
            log.error(f"断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            log.info('清空购物车,并返回首页')
            self.cart.page_cart_clear_all()
            raise

    @pytest.mark.run(order=2)
    def test02_add_huasheng_to_cart(self):
        log.info('添加花生到购物车')
        handle1 = self.driver.current_window_handle
        self.cart.page_cart_go_zhubao()
        handles = self.driver.window_handles
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
                self.driver.switch_to.window(handle2)
        name1 = self.cart.page_get_huasheng_name()
        price1 = '￥' + self.cart.page_get_huasheng_price()
        self.cart.page_cart_huasheng_commit()
        self.cart.page_cart_huasheng_go_to_cart()
        name2 = self.cart.page_get_cart_huasheng_name()
        price2 = self.cart.page_get_cart_huasheng_price()
        try:
            log.info('正在进行商品价格断言')
            assert price1 == price2
        except Exception as e:
            log.error(f"断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise
        try:
            log.info('正在进行商品名称断言')
            assert name1 == name2
        except Exception as e:
            log.error(f"断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise

    @pytest.mark.parametrize("num, result", read_yaml('cart_huasheng_number.yaml'))
    # @pytest.mark.skip()
    @pytest.mark.run(order=3)
    def test03_modify_cart_huasheng_num(self, num, result):
        log.info('修改购物车中商品数量')
        self.cart.page_cart_modify_huasheng_number(num)
        self.cart.page_cart_click_cart_blank()
        sleep(2)
        if result == '':
            log.info(f'正向用例修改数量为{num}')
            try:
                log.info('正在进行断言')
                assert self.cart.page_cart_get_huasheng_number() == num
            except Exception as e:
                log.error(f"断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
        else:
            # 003测试用例出口
            if result == '1':
                log.info("当前测试用例出口")
                self.cart.page_cart_modify_huasheng_number('1')
                self.cart.page_cart_click_continue_to_shopping()
                while True:
                    try:
                        assert self.cart.base_find_element(page.cart_huasheng_commit)
                        break
                    except:
                        print('等待页面跳转')
                        sleep(1)

            else:
                log.info(f'正向用例修改数量为{num}，预期结果是{result}')
                try:
                    log.info('正在进行断言')
                    assert self.cart.page_cart_get_huasheng_error() == result
                except Exception as e:
                    log.error(f"无错误提示信息，或者提示信息有误,断言失败:{e}")
                    module_name = str(os.path.basename(__file__)).split('.')[0]
                    self.login.base_get_screenshot(module_name)
                    raise

    @pytest.mark.flaky(rerun=1, rerun_delay=2)
    @pytest.mark.parametrize("num, result", read_yaml('cart_huasheng_number1.yaml'))
    # @pytest.mark.skip()
    @pytest.mark.run(order=4)
    def test04_modify_huasheng_num(self, num, result):
        log.info('修改添加商品时的数量')
        self.driver.refresh()
        self.cart.page_cart_modify_huasheng_number1(num)
        self.cart.page_cart_huasheng_commit()
        if result == '':
            log.info(f'正向用例修改数量为{num}')
            self.cart.page_cart_huasheng_go_to_cart()
            try:
                new_result = str(int(num) + 1)
                if new_result == '201':
                    new_result = '200'
                log.info('正在进行断言')
                assert self.cart.page_cart_get_huasheng_number() == new_result
            except Exception as e:
                log.error(f"商品数量有误,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
            finally:
                log.info("修改数量为1，继续执行下一条")
                self.cart.page_cart_modify_huasheng_number('1')
                self.cart.page_cart_click_continue_to_shopping()
                while True:
                    try:
                        assert self.cart.base_find_element(page.cart_huasheng_commit)
                        break
                    except:
                        print('等待页面跳转')
                        sleep(1)
        else:
            # 004测试用例出口
            if result == '1':
                log.info("是本条用例的出口")
                self.cart.page_cart_huasheng_go_to_cart()
                # self.cart.page_cart_modify_huasheng_number('1')
                # self.cart.page_cart_click_continue_to_shopping()
            else:
                log.info(f'逆向用例修改数量为{num}，预期结果是{result}')
                try:
                    log.info("正在进行断言")
                    assert self.cart.page_cart_get_huasheng_error() == result
                except Exception as e:
                    log.error(f"无错误提示信息，或者提示信息有误,断言失败:{e}")
                    module_name = str(os.path.basename(__file__)).split('.')[0]
                    self.login.base_get_screenshot(module_name)
                    raise

    @pytest.mark.parametrize("num, result", read_yaml('cart_goods_kinds_num.yaml'))
    # @pytest.mark.skip()
    @pytest.mark.run(order=5)
    def test05_modify_goods_kinds_number(self, num, result):
        file_name = 'tp_cart' + num + '.sql'
        read_sql(file_name)
        log.info(f"插入{num}件商品")
        self.driver.refresh()
        if result == '':
            try:
                log.info('正在进行断言，检查购物车中产品数量')
                assert self.cart.page_cart_get_goods_kinds_number().startswith(num)
            except Exception as e:
                log.error(f"商品数量有误,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
        else:
            log.info('逆向用例')
            try:
                log.info('正在进行断言，检查购物车中产品数量')
                assert self.cart.page_cart_get_huasheng_error() == result
            except Exception as e:
                log.error(f"无错误提示信息，或者提示信息有误,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise

    @pytest.mark.run(order=6)
    # @pytest.mark.skip()
    def test06_delete_goods_check(self):
        read_sql('tp_cart2.sql')
        self.driver.refresh()
        log.info('执行购物车中商品删除操作')
        self.cart.page_cart_click_continue_to_shopping()
        self.cart.page_cart_huasheng_commit()
        self.cart.page_cart_huasheng_go_to_cart()
        self.cart.page_cart_delete_by_x()
        sleep(3)
        try:
            log.info('正在进行断言，检测对应产品是否删除')
            assert self.cart.page_get_cart_huasheng_name()
        except Exception as e:
            log.error(f"商品删除错误，未对应商品被删除,断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise

    @pytest.mark.parametrize("num, result", read_yaml('cart_cut_btn.yaml'))
    @pytest.mark.run(order=7)
    # @pytest.mark.skip()
    def test07_check_cut_btn(self, num, result):
        log.info("测试购物车中加减号的功能")
        self.driver.refresh()
        self.cart.page_cart_modify_huasheng_number(num)
        self.cart.page_cart_click_cart_blank()
        sleep(3)
        if result == '':
            new_result = str(int(num) - 1)
            try:
                log.info('正在进行断言，判断减号是否可用')
                assert self.cart.page_cart_check_cut_if_enable()
                self.cart.page_cart_click_cut()
                log.info('-号可用，正在进行断言，验证减号功能')
                assert self.cart.page_cart_get_huasheng_number() == new_result
                log.info('-号功能正常')
            except Exception as e:
                log.error(f"正向用例，-号不可用，或者点击减号数量修改错误,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
        else:
            log.info('逆向用例，正在进行断言，判断减号为不可用')
            try:
                assert not self.cart.page_cart_check_cut_if_enable()
            except Exception as e:
                log.error(f"逆向用例，-号可用错误,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise

    @pytest.mark.parametrize("num, result", read_yaml('cart_add_btn.yaml'))
    @pytest.mark.run(order=8)
    # @pytest.mark.skip()
    def test08_check_add_btn(self, num, result):
        self.driver.refresh()
        self.cart.page_cart_modify_huasheng_number(num)
        self.cart.page_cart_click_cart_blank()
        sleep(3)
        if result == '':
            new_result = str(int(num) + 1)
            try:
                log.info('正在进行断言，判断+号是否可用')
                assert self.cart.page_cart_check_add_if_enable()
                log.info('+号可用，正在进行断言，验证减号功能')
                self.cart.page_cart_click_add()
                assert self.cart.page_cart_get_huasheng_number() == new_result
                log.info('+号功能正常')
            except Exception as e:
                log.error(f"正向用例，-号不可用，或者点击减号数量修改错误,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
        else:
            try:
                log.info('逆向用例，正在进行断言，判断+号为不可用')
                assert not self.cart.page_cart_check_add_if_enable()
            except Exception as e:
                log.error(f"逆向用例，+号可用错误,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise

    @pytest.mark.parametrize("num", read_yaml_sigle('cart_sub_price.yaml'))
    @pytest.mark.run(order=9)
    # @pytest.mark.skip()
    def test09_check_sub_total_price(self, num):
        log.info('测试小计功能')
        self.cart.page_cart_modify_huasheng_number(num)
        self.cart.page_cart_click_cart_blank()
        self.i = 0
        while True:
            self.i += 1
            self.str = str(num) + '件商品'
            if self.cart.page_cart_get_goods_kinds_number() == self.str:
                log.info('商品价格已刷新')
                break
            else:
                if self.i < 5:
                    sleep(1)
                    log.info('等待商品价格刷新')
                else:
                    self.i = 0
                    self.driver.refresh()
                    self.cart.page_cart_modify_huasheng_number(num)
                    self.cart.page_cart_click_cart_blank()

        if num == '1':
            try:
                log.info(f'正在进行断言,商品数量为{num}时，小计价格是否等于单价')
                assert self.cart.page_cart_get_member_price() == self.cart.page_cart_get_sub_total()
            except Exception as e:
                log.error(f"商品数量为1时，小计不等于商品价格,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise
        else:
            try:
                goods_price = self.cart.page_cart_get_member_price()
                sub_total = '￥' + str(float(goods_price[1::1]) * int(num))
                log.info(f'正在进行断言,商品数量为{num}时，小计价格是否等于单价乘以数量{sub_total}')
                assert sub_total in self.cart.page_cart_get_sub_total()
            except Exception as e:
                log.error(f"商品数量为{num}时,小计不等于单价与数量之积,断言失败:{e}")
                module_name = str(os.path.basename(__file__)).split('.')[0]
                self.login.base_get_screenshot(module_name)
                raise

    @pytest.mark.run(order=10)
    def test10_check_selected_kinds_num(self):
        log.info('测试购物车选中商品数量')
        read_sql('tp_cart2.sql')
        self.driver.refresh()
        log.info('执行部分选择操作')
        self.cart.page_cart_click_continue_to_shopping()
        self.cart.page_cart_huasheng_commit()
        self.cart.page_cart_huasheng_go_to_cart()
        self.orginfo = self.cart.page_cart_get_goods_kinds_number()
        self.cart.page_cart_click_2_in_3()
        while True:
            if self.orginfo == self.cart.page_cart_get_goods_kinds_number():
                log.info('等待商品数量刷新')
                sleep(1)
            else:
                break
        try:
            log.info('正在进行断言，选中2件商品')
            assert '2件商品' == self.cart.page_cart_get_goods_kinds_number()
        except Exception as e:
            log.error(f"断言失败，取消选择后商品数量错误,断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise

    @pytest.mark.run(order=11)
    def test11_check_total_price(self):
        log.info('测试购物车总价')
        try:
            log.info('正在进行断言购物车总价')
            assert self.cart.page_cart_get_total() == '￥1279.24'
        except Exception as e:
            log.error(f"取消选择后商品数量错误,断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise

    @pytest.mark.run(order=14)
    def test14_go_to_pay(self):
        log.info('测试生成订单')
        self.cart.page_cart_go_to_pay()
        try:
            log.info('正在进行生成订单断言')
            assert self.cart.page_if_go_to_pay_success()
        except Exception as e:
            log.error(f"生成订单失败,断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise

    @pytest.mark.run(order=12)
    def test12_check_goodsname_go_to_detail(self):
        log.info('测试点击商品名称是否会跳转')
        self.cart.page_cart_click_good_name()
        try:
            log.info('正在进行断言')
            assert self.cart.page_cart_check_if_go_detail()
            self.cart.page_cart_click_cart_link()
            sleep(2)
        except Exception as e:
            log.error(f"点击名称不能跳转到详情页,断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise

    @pytest.mark.run(order=13)
    def test13_check_picture_go_to_detail(self):
        log.info('测试点击商品图片是否会跳转')
        self.cart.page_cart_click_good_picture()
        try:
            log.info('正在进行断言')
            assert self.cart.page_cart_check_if_go_detail()
            self.cart.page_cart_click_cart_link()
            sleep(2)
        except Exception as e:
            log.error(f"点击图片不能跳转到详情页,断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise
