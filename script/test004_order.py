import os
from time import sleep

import page
from page.page_login import PageLogin
from page.page_order import PageOrder
from tool.get_driver import GetDriver
from tool.get_log import GetLogger
from tool.read_sql import read_sql
from tool.server_bat import WinRM

log = GetLogger.get_log()


class TestOrder:

    @classmethod
    def setup_class(cls):
        WinRM().run_bat_file()
        read_sql('tp_order.sql')
        read_sql('tp_order_goods.sql')
        print('初始化用户订单')
        cls.driver = GetDriver.get_web_driver(page.URL)
        cls.order = PageOrder(cls.driver)
        cls.login = PageLogin(cls.driver)
        cls.login.page_login()
        cls.login.page_keep_return_FP()
        cls.driver2 = GetDriver.get_web_driver2(page.URL2)
        cls.ms = PageOrder(cls.driver2)
        cls.order_number = None

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_web_driver()
        GetDriver.quit_web_driver2()

    @classmethod
    def modify_order_number(cls, num):
        cls.order_number = num

    def test01_front_order(self):
        log.info('测试生成订单')
        self.order.page_order_front()
        sleep(5)
        self.order.page_order_click_submit_order()
        try:
            assert self.order.page_order_if_submit_success()
            self.order.page_order_select_pay_style()
        except Exception as e:
            log.error(f"生成订单失败，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise
        try:
            log.info('正在进行断言当前订单状态')
            assert self.order.page_order_check_status() == '待发货'
            self.order_number = self.order.page_get_order_number()
            self.modify_order_number(self.order_number)
            log.info(f'订单编号是{self.order_number}')
        except Exception as e:
            log.error(f"订单状态错误，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.login.base_get_screenshot(module_name)
            raise

    def test02_ms_check_new_order(self):
        self.ms.page_order_ms_login()
        statues = self.ms.page_ms_statues(self.order_number)
        log.info(f'正在获取后台订单状态，状态为{statues}')
        self.ms.page_ms_check()
        try:
            log.info('正在进行断言')
            assert statues == ('待确认', '未支付', '未发货')
        except Exception as e:
            log.error(f"后台订单状态错误，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.ms.base_get_screenshot(module_name)
            raise

    def test03_ms_check_confirm(self):
        log.info('确认订单')
        self.ms.page_order_confirm()
        statues = self.ms.page_ms_statues(self.order_number)
        log.info(f'正在获取后台订单状态，状态为{statues}')
        self.ms.page_ms_check()
        try:
            log.info('正在进行断言')
            assert statues == ('已确认', '未支付', '未发货')
        except Exception as e:
            log.error(f"后台订单状态错误，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.ms.base_get_screenshot(module_name)
            raise

    def test04_ms_check_express(self):
        log.info('进行发货')
        self.ms.page_order_go_express()
        statues = self.ms.page_ms_statues(self.order_number)
        log.info(f'正在获取后台订单状态，状态为{statues}')
        self.ms.page_ms_check()
        try:
            log.info('正在进行断言')
            assert statues == ('已确认', '未支付', '已发货')
        except Exception as e:
            log.error(f"后台订单状态错误，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.ms.base_get_screenshot(module_name)
            raise

    def test05_ms_check_pay(self):
        log.info('进行支付')
        self.ms.page_order_go_pay()
        statues = self.ms.page_ms_statues(self.order_number)
        log.info(f'正在获取后台订单状态，状态为{statues}')
        self.ms.page_ms_check()
        try:
            log.info('正在进行断言')
            assert statues == ('已确认', '已支付', '已发货')
        except Exception as e:
            log.error(f"后台订单状态错误，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.ms.base_get_screenshot(module_name)
            raise

    def test06_front_confirm_goods(self):
        self.driver.refresh()
        try:
            log.info('正在进行断言前台订单状态')
            assert self.order.page_order_check_status() == '待收货'
            log.info('确认收货')
            self.order.page_confirm_goods()
        except Exception as e:
            log.error(f"前台状态错误，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.order.base_get_screenshot(module_name)
            raise

    def test07_check_confirm_goods(self):
        sleep(3)
        try:
            log.info('正在进行断言前台订单状态')
            assert self.order.page_order_check_status() == '待评价'
        except Exception as e:
            log.error(f"确认收货错误，断言失败:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.order.base_get_screenshot(module_name)
            raise

    def test08_ms_check_final_statues(self):
        self.driver2.switch_to.default_content()
        log.info('返回后台管理系统')
        statues = self.ms.page_ms_statues(self.order_number)
        log.info(f'正在获取后台订单状态，状态为{statues}')
        try:
            assert statues == ('已收货', '已支付', '已发货')
        except Exception as e:
            log.error(f"订单状态错误:{e}")
            module_name = str(os.path.basename(__file__)).split('.')[0]
            self.order.base_get_screenshot(module_name)
            raise
