/*
 Navicat Premium Data Transfer

 Source Server         : COMP0035
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : schema-group07

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 07/01/2021 16:50:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for wrt
-- ----------------------------
DROP TABLE IF EXISTS `wrt`;
CREATE TABLE `wrt`  (
  `idwrt` int(0) NOT NULL,
  `属性名称` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`idwrt`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of wrt
-- ----------------------------
INSERT INTO `wrt` VALUES (1, '宋智龙');
INSERT INTO `wrt` VALUES (2, '陈大有');
INSERT INTO `wrt` VALUES (3, '马文腾');
INSERT INTO `wrt` VALUES (4, '陆炫彤');
INSERT INTO `wrt` VALUES (5, '杜子浩');

SET FOREIGN_KEY_CHECKS = 1;
