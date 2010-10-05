-- phpMyAdmin SQL Dump
-- version 3.3.7
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2010 年 10 月 06 日 01:05
-- 服务器版本: 5.1.48
-- PHP 版本: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `webpy`
--

-- --------------------------------------------------------

--
-- 表的结构 `todo`
--

CREATE TABLE IF NOT EXISTS `todo` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` text CHARACTER SET utf8 COLLATE utf8_bin,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `done` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- 转存表中的数据 `todo`
--

INSERT INTO `todo` (`id`, `title`, `created`, `done`) VALUES
(1, 'Learn web.py', '2010-10-06 00:37:37', NULL),
(2, 'love py', '2010-10-06 00:49:19', NULL),
(3, '???', '2010-10-06 00:49:28', NULL),
(4, 'hao yang de!', '2010-10-06 00:49:54', NULL),
(5, 'webpy.org', '2010-10-06 00:59:17', NULL),
(6, '你好', '2010-10-06 01:01:06', NULL),
(7, '好了，改变数据库字段为utf-8，即能进行中文输入', '2010-10-06 01:01:38', NULL);
