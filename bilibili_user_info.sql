DROP TABLE IF EXISTS `bilibili_user_info`;

CREATE TABLE `bilibili_user_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `mid` varchar(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `sex` varchar(11) DEFAULT NULL,
  `face` varchar(200) DEFAULT NULL,
  `coins` int(11) DEFAULT NULL,
  `regtime` varchar(45) DEFAULT NULL,
  `spacesta` int(11) DEFAULT NULL,
  `birthday` varchar(45) DEFAULT NULL,
  `place` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `article` int(11) DEFAULT NULL,
  `fans` int(11) DEFAULT NULL,
  `friend` int(11) DEFAULT NULL,
  `attention` int(11) DEFAULT NULL,
  `sign` varchar(300) DEFAULT NULL,
  `attentions` text,
  `level` int(11) DEFAULT NULL,
  `exp` int(11) DEFAULT NULL,
  `approve` tinyint(1) DEFAULT NULL,
  `im9_sign` varchar(45) DEFAULT NULL,
  `official_verify` int(11) DEFAULT NULL,
  `playNum` int(20) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=873982 DEFAULT CHARSET=utf8;