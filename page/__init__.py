from selenium.webdriver.common.by import By

# 域名配置信息
URL = "http://www.myshop.com/"

# 以下是登录模块配置信息
login_link = By.PARTIAL_LINK_TEXT, "登录"
login_username = By.CSS_SELECTOR, "#username"
login_password = By.CSS_SELECTOR, "#password"
login_code = By.CSS_SELECTOR, "#verify_code"
login_btn = By.CSS_SELECTOR, ".J-login-submit"
login_code_img = By.CSS_SELECTOR, "#verify_code_img"
login_error = By.CSS_SELECTOR, ".layui-layer-content"
login_error_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
logout = By.PARTIAL_LINK_TEXT, "安全退出"
login_return = By.CSS_SELECTOR, '[title ="首页"]'

# 以下是注册模块配置信息
register_link = By.LINK_TEXT, "注册"
register_phone_link = By.PARTIAL_LINK_TEXT, "手机注册"
register_email_link = By.PARTIAL_LINK_TEXT, "邮箱注册"
register_username = By.CSS_SELECTOR, "#username"
register_password = By.CSS_SELECTOR, "#password"
register_code = By.CSS_SELECTOR, "[name = 'verify_code']"
register_refresh_btn = By.CSS_SELECTOR, ".ma-le-210"
register_password_confirm = By.CSS_SELECTOR, "#password2"
register_invite_phone = By.CSS_SELECTOR, '[name ="invite"]'
register_agree_protocol = By.CSS_SELECTOR, ".iyes"
register_submit_btn = By.CSS_SELECTOR, ".regbtn"
register_error_text = By.CSS_SELECTOR, ".layui-layer-content"
register_error_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
register_error_return = By.PARTIAL_LINK_TEXT, '登录'

# 以下是购物车模块配置信息
cart_link = By.CSS_SELECTOR, '.c-n'
cart_empty = By.CSS_SELECTOR, ".shopcar_empty"
cart_FB_zhubao = By.XPATH, '//ul[@id="navitems"]/li[3]/a'

cart_huasheng_add = By.CSS_SELECTOR, ".increment"
cart_huasheng_cut = By.CSS_SELECTOR, ".decrement"
cart_huasheng_number1 = By.CSS_SELECTOR, '#number_99'
cart_huasheng_commit = By.XPATH, '//*[@class="s_xsall"][1]/../../li[2]//div[@class="p-btn"]'
cart_huasheng_frame = By.CSS_SELECTOR, '#layui-layer-iframe1'
cart_huasheng_continue = By.CSS_SELECTOR, '.ui-button-f80'
cart_huasheng_go = By.CSS_SELECTOR, '.ui-button-122'
cart_huasheng_name2 = By.PARTIAL_LINK_TEXT, 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右'
cart_huasheng_price1 = By.XPATH, "//*[contains(@href, \'/index.php/Home/Goods/goodsInfo/id/99.html\')]/../..//span[@class = 'now']/em[2]"
cart_huasheng_name1 = By.XPATH, "//a[@href = '/index.php/Home/Goods/goodsInfo/id/99.html']/../../div[4]/a"
cart_huasheng_price2 = By.XPATH, "//td[contains(@id,'goods_price')][1]"
cart_huasheng_market_price = By.XPATH, "//td[contains(@id,'market_price')]"
cart_huasheng_number = By.CSS_SELECTOR, '.wi43'
cart_huasheng_error_msg = By.CSS_SELECTOR, '.layui-layer-content'
cart_huasheng_error_btn = By.CSS_SELECTOR, '.layui-layer-btn0'
cart_goods_number = By.CSS_SELECTOR, '#goods_num'
cart_goods_fee = By.CSS_SELECTOR, "#total_fee"
cart_order_btn = By.CSS_SELECTOR, '[onclick ="submit_order();" ]'
cart_go_to_pay_btn = By.LINK_TEXT, '去结算'
cart_continue_btn = By.LINK_TEXT, '继续购物'
cart_goods_number_add = By.CSS_SELECTOR, '.increment'
cart_goods_number_cut = By.CSS_SELECTOR, '.decrement'
cart_delete_X1 = By.CSS_SELECTOR, '[data-cart-id="144"]'
cart_delete_X2 = By.CSS_SELECTOR, '[data-cart-id="145"]'
cart_order_back = By.CSS_SELECTOR, '.logo'
cart_user_back = By.CSS_SELECTOR, '.ecsc-logo'
cart_checkall = By.CSS_SELECTOR, '.checkCartAll'
cart_remove_all = By.CSS_SELECTOR, '#removeGoods'
cart_blank = By.CSS_SELECTOR, '.progress-area-wd'
cart_detail_check = By.CSS_SELECTOR, '#join_cart'
cart_detail_picture = By.CSS_SELECTOR, '.wi63'
cart_huasheng_membergoodsprice = By.XPATH, "//td[contains(@id,'member_goods_price')]"
cart_checked_goods = By.CSS_SELECTOR, '[value="145"]'

# 以下为下单流程配置信息
order_pay_style = By.CSS_SELECTOR, '.button-style-5'
order_pay_hdfk = By.CSS_SELECTOR, '[value="pay_code=cod"]'
order_detail = By.LINK_TEXT, '订单详情'
order_status = By.CSS_SELECTOR, '.ddn2'
order_number = By.XPATH, '//*[@class="ddn1"]/span[2]'
order_confirm_goods = By.CSS_SELECTOR, '.ddn3'
order_confirm_goods2 = By.CSS_SELECTOR, '.layui-layer-btn0'
# 以下为后台管理系统配置信息
URL2 = 'http://www.myshop.com/Admin/Admin/login'
ms_username = By.CSS_SELECTOR, '[name="username"]'
ms_password = By.CSS_SELECTOR, '[name="password"]'
ms_code = By.CSS_SELECTOR, '[name="vertify"]'
ms_login = By.CSS_SELECTOR, '.sub'
ms_shop = By.CSS_SELECTOR, '[data-param="shop"]'
ms_order = By.CSS_SELECTOR, '.ico-shop-1'
ms_order_list = By.CSS_SELECTOR, '[data-param="index|Order"]'
ms_frame = By.CSS_SELECTOR, '#workspace'
ms_search_key = By.CSS_SELECTOR, '[name="keytype"]'
ms_search_key_order_number = 'order_sn'
ms_search = By.CSS_SELECTOR, '[name="keywords"]'
ms_search_btn = By.CSS_SELECTOR, '[value="搜索"]'
ms_statues1 = By.XPATH, "//*[@id = '1509']/td[6]/div"
ms_statues2 = By.XPATH, "//*[@id = '1509']/td[7]/div"
ms_statues3 = By.XPATH, "//*[@id = '1509']/td[8]/div"
ms_check_order = By.CSS_SELECTOR,'.green'
ms_input_note = By.CSS_SELECTOR, '#note'
ms_confirm_btn = By.LINK_TEXT, '确认'
ms_express_btn = By.LINK_TEXT, '去发货'
ms_input_express_num = By.CSS_SELECTOR,'.input-txt'
ms_confirm_express_btn = By.LINK_TEXT,'确认发货'
ms_pay = By.LINK_TEXT,'付款'






