/*
Navicat MySQL Data Transfer

Source Server         : mydb
Source Server Version : 50633
Source Host           : localhost:3306
Source Database       : hardware_maker

Target Server Type    : MYSQL
Target Server Version : 50633
File Encoding         : 65001

Date: 2017-06-20 09:07:55
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for product_case
-- ----------------------------
DROP TABLE IF EXISTS `product_case`;
CREATE TABLE `product_case` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `caseType` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `structure` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `smallPosition` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bigPosition` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `panelPort` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `powerSupport` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `caseTheme` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `caseMaterial` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `extSlot` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `weight` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mainboardSupport` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fan` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lineMode` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4003 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for product_cpu
-- ----------------------------
DROP TABLE IF EXISTS `product_cpu`;
CREATE TABLE `product_cpu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `socketType` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `frequency` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `turboFrequency` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `craftsmanship` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `secondCache` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `thirdCache` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `coreNum` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `coreCode` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tdp` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ht` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1641 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for product_graph
-- ----------------------------
DROP TABLE IF EXISTS `product_graph`;
CREATE TABLE `product_graph` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `coreType` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `port` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `chipset` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ram` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `bit` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `coreFrequency` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vmFrequency` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fanType` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1270 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for product_hdd
-- ----------------------------
DROP TABLE IF EXISTS `product_hdd`;
CREATE TABLE `product_hdd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `size` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `port` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `type` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rpm` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cache` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `portBit` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `inchType` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=622 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for product_mainboard
-- ----------------------------
DROP TABLE IF EXISTS `product_mainboard`;
CREATE TABLE `product_mainboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `socketType` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `chipset` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ddrSupport` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cpuSupport` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `integratedChip` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `integratedGraph` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `boardSize` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `usbPort` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8017 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for product_power
-- ----------------------------
DROP TABLE IF EXISTS `product_power`;
CREATE TABLE `product_power` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `ratedPower` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maxPower` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `powerVersion` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `support` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fan` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `powerType` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `other` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `plusAuth` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `safeAuth` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pfc` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `safeFunction` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `voltageSupport` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lineMode` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7506 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for product_ram
-- ----------------------------
DROP TABLE IF EXISTS `product_ram`;
CREATE TABLE `product_ram` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `size` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `desc` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ddrType` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `frequency` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cl` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pin` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `voltage` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=605 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for product_ssd
-- ----------------------------
DROP TABLE IF EXISTS `product_ssd`;
CREATE TABLE `product_ssd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zolId` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `size` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `port` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `readSpeed` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `writeSpeed` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `inchType` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `warranty` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `architecture` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `chipset` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `seekTime` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fourKRandom` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zolScore` float DEFAULT NULL,
  `image` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `page` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2075 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `createTime` datetime DEFAULT NULL,
  `lastLoginTime` datetime DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
