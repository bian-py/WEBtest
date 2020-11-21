/*
 Navicat MySQL Data Transfer

 Source Server         : 商城
 Source Server Type    : MySQL
 Source Server Version : 50553
 Source Host           : 192.168.128.128:3306
 Source Schema         : tpshop2.0

 Target Server Type    : MySQL
 Target Server Version : 50553
 File Encoding         : 65001

 Date: 07/11/2020 17:02:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tp_cart
-- ----------------------------
DROP TABLE IF EXISTS `tp_cart`;
CREATE TABLE `tp_cart`  (
  `id` int(8) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '购物车表',
  `user_id` mediumint(8) UNSIGNED NOT NULL DEFAULT 0 COMMENT '用户id',
  `session_id` char(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' COMMENT 'session',
  `goods_id` mediumint(8) UNSIGNED NOT NULL DEFAULT 0 COMMENT '商品id',
  `goods_sn` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '商品货号',
  `goods_name` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '商品名称',
  `market_price` decimal(10, 2) UNSIGNED NOT NULL DEFAULT 0.00 COMMENT '市场价',
  `goods_price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '本店价',
  `member_goods_price` decimal(10, 2) DEFAULT 0.00 COMMENT '会员折扣价',
  `goods_num` smallint(5) UNSIGNED DEFAULT 0 COMMENT '购买数量',
  `spec_key` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '' COMMENT '商品规格key 对应tp_spec_goods_price 表',
  `spec_key_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '' COMMENT '商品规格组合名称',
  `bar_code` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '' COMMENT '商品条码',
  `selected` tinyint(1) DEFAULT 1 COMMENT '购物车选中状态',
  `add_time` int(11) DEFAULT 0 COMMENT '加入购物车的时间',
  `prom_type` tinyint(1) DEFAULT 0 COMMENT '0 普通订单,1 限时抢购, 2 团购 , 3 促销优惠',
  `prom_id` int(11) DEFAULT 0 COMMENT '活动id',
  `sku` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '' COMMENT 'sku',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `session_id`(`session_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `goods_id`(`goods_id`) USING BTREE,
  INDEX `spec_key`(`spec_key`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 147 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tp_cart
-- ----------------------------
INSERT INTO `tp_cart` VALUES (145, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 57, 'TP0000057', 'TCL D50A710 50英寸 40万小时视频 全高清 内置WiFi 八核安卓智能LED液晶电视', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (144, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 56, 'TP0000056', '创维（skyworth）55M5 55英寸4K超高清网络智能液晶电视机', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (143, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 55, 'TP0000055', '华为（HUAWEI）WS832 1200M 11AC双频智能无线路由器（白色）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (142, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 54, 'TP0000054', '荣耀盒子 标准版（4K，H.265，4核芯片1G内存+4G存储，300Mwifi，HDMI/SD卡/USB/AV/SPDIF/网口）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (141, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 53, 'TP0000053', '华为 HUAWEI MediaQ M330 华为盒子 4K极清网络机顶盒（黑色）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (140, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 52, 'TP0000052', '荣耀路由Pro 大户型穿墙王1200Mbps智能AC有线无线双千兆旗舰路由器（白色）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (139, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 51, 'TP0000051', '华为 HUAWEI Mate 8 4GB+64GB版 全网通（香槟金）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (138, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 50, 'TP0000050', '华为 HUAWEI 畅享5S 全网通 2GB RAM+16GB ROM（金色）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (137, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 49, 'TP0000049', '荣耀畅玩5X 双卡双待 移动版 智能手机（破晓银）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (136, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 48, 'TP0000048', '荣耀7 双卡双待双通 移动4G版 16GB存储（冰河银）豪华套装一', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (135, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 47, 'TP0000047', '【联通合约机 50元本地套餐】荣耀畅玩5X 双卡双待 增强全网通版 智能手机（落日金）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (134, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 46, 'TP0000046', '【北京移动老用户专享 话费六折】荣耀畅玩5X 双卡双待 移动版 智能手机（破晓银）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (133, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 45, 'TP0000045', '华为 HUAWEI C199S 麦芒3S 电信4G智能手机FDD-LTE /TD-LTE/CDMA2000/GSM（麦芒金）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (132, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 44, 'TP0000044', '荣耀平板 8.0英寸平板电脑（Wi-Fi版 四核1.2GHz处理器 1GB内存 8GB存储）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (131, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 43, 'TP0000043', '荣耀畅玩平板note 9.6英寸平板电脑 移动/联通双4G LTE版', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (130, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 42, 'TP0000042', 'Teclast/台电 X80 Plus WIFI 32GB Win10平板电脑双系统8英寸', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (129, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 41, 'TP0000041', '华为（HUAWEI） M2 8英寸平板电脑（1920×1200 IPS屏 海思麒麟930 16GB WiFi）香槟金', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (128, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 40, 'TP0000040', '荣耀X2 标准版 双卡双待双通 移动/联通双4G 16GB ROM（月光银）', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (126, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 1, 'TP000000', 'Apple iPhone 6s Plus 16G 玫瑰金 移动联通电信4G手机', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');
INSERT INTO `tp_cart` VALUES (127, 2603, 'qjg1ohs4jv5rtd365upo18bli3', 39, 'TP0000039', '华为（HUAWEI） M2 10.0 平板电脑 WiFi 月光银', 222.00, 888.00, 870.24, 1, '', '', '', 1, 0, 0, 0, '');

SET FOREIGN_KEY_CHECKS = 1;
