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

 Date: 07/11/2020 16:41:05
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
) ENGINE = MyISAM AUTO_INCREMENT = 126 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tp_cart
-- ----------------------------
INSERT INTO `tp_cart` VALUES (5, 2594, 'i75risfaenac63rq4o3chi44e7', 65, 'TP0000065', '长虹(CHANGHONG) 49A1U 49英寸双64位4K超清智能网络LED液晶电视', 2899.00, 2799.00, 2799.00, 100, '65', '尺寸:42', '', 1, 1603882094, 0, 0, '');
INSERT INTO `tp_cart` VALUES (98, 0, '34vd4m1no3681l9hoddr669oe7', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 2, '', '', '', 1, 1604658002, 0, 0, '');
INSERT INTO `tp_cart` VALUES (90, 0, 'evgfni8n33acdcnv2duu9r2463', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 0, '', '', '', 1, 1604654298, 0, 0, '');
INSERT INTO `tp_cart` VALUES (86, 0, '35tst8hv05ba5alq40ol3esir6', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 0, '', '', '', 1, 1604653454, 0, 0, '');
INSERT INTO `tp_cart` VALUES (87, 0, '5mhopctv7u9hs1urgqhatgrt57', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 0, '', '', '', 1, 1604653496, 0, 0, '');
INSERT INTO `tp_cart` VALUES (85, 0, 'ceec6mrna31u9ef64fviph59i2', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 1, '', '', '', 1, 1604653378, 0, 0, '');
INSERT INTO `tp_cart` VALUES (84, 0, 'pmlgt69lk8hgtvg2v3rf3bt4n6', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 0, '', '', '', 1, 1604653144, 0, 0, '');
INSERT INTO `tp_cart` VALUES (81, 0, 'cmvv2hb9q5npvqphh7aqeoqbm3', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 1, '', '', '', 1, 1604649223, 0, 0, '');
INSERT INTO `tp_cart` VALUES (82, 0, 'nroc9oa71rbpkarkujckt94i75', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 0, '', '', '', 1, 1604649446, 0, 0, '');
INSERT INTO `tp_cart` VALUES (83, 0, 'cgkg8pc8802gbg7ge1cv11q132', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 0, '', '', '', 1, 1604651868, 0, 0, '');
INSERT INTO `tp_cart` VALUES (80, 0, 'uht9ee3tubk03hk070iom7ast4', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 1, '', '', '', 1, 1604649042, 0, 0, '');
INSERT INTO `tp_cart` VALUES (77, 0, '0qfdqm7kvf7npd32lb7o7qltn2', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 1, '', '', '', 1, 1604648664, 0, 0, '');
INSERT INTO `tp_cart` VALUES (78, 0, '5rtjov2iurq6fm7glm53sa1jk3', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 1, '', '', '', 1, 1604648746, 0, 0, '');
INSERT INTO `tp_cart` VALUES (79, 0, 'h3c1it50op3snmd7dhe1rqen44', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 1, '', '', '', 1, 1604648979, 0, 0, '');
INSERT INTO `tp_cart` VALUES (76, 0, 'tqm3antghhsvi7r4mv3osn0qk7', 99, 'TP0000099', 'CNUTI粤通国际珠宝 黄金首饰 足金花生吊坠 男女同款 宝宝礼物 约1.25克左右', 509.00, 409.00, 409.00, 1, '', '', '', 1, 1604647750, 0, 0, '');

SET FOREIGN_KEY_CHECKS = 1;
