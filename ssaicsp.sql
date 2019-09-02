/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1_3306
Source Server Version : 50723
Source Host           : 127.0.0.1:3306
Source Database       : ssaicsp

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2018-08-07 09:19:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add user', '3', 'add_user');
INSERT INTO `auth_permission` VALUES ('10', 'Can change user', '3', 'change_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete user', '3', 'delete_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can view user', '3', 'view_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add group', '4', 'add_group');
INSERT INTO `auth_permission` VALUES ('14', 'Can change group', '4', 'change_group');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete group', '4', 'delete_group');
INSERT INTO `auth_permission` VALUES ('16', 'Can view group', '4', 'view_group');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add activebuzzer', '7', 'add_activebuzzer');
INSERT INTO `auth_permission` VALUES ('26', 'Can change activebuzzer', '7', 'change_activebuzzer');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete activebuzzer', '7', 'delete_activebuzzer');
INSERT INTO `auth_permission` VALUES ('28', 'Can view activebuzzer', '7', 'view_activebuzzer');
INSERT INTO `auth_permission` VALUES ('29', 'Can add aroadtracing', '8', 'add_aroadtracing');
INSERT INTO `auth_permission` VALUES ('30', 'Can change aroadtracing', '8', 'change_aroadtracing');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete aroadtracing', '8', 'delete_aroadtracing');
INSERT INTO `auth_permission` VALUES ('32', 'Can view aroadtracing', '8', 'view_aroadtracing');
INSERT INTO `auth_permission` VALUES ('33', 'Can add current', '9', 'add_current');
INSERT INTO `auth_permission` VALUES ('34', 'Can change current', '9', 'change_current');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete current', '9', 'delete_current');
INSERT INTO `auth_permission` VALUES ('36', 'Can view current', '9', 'view_current');
INSERT INTO `auth_permission` VALUES ('37', 'Can add dht11', '10', 'add_dht11');
INSERT INTO `auth_permission` VALUES ('38', 'Can change dht11', '10', 'change_dht11');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete dht11', '10', 'delete_dht11');
INSERT INTO `auth_permission` VALUES ('40', 'Can view dht11', '10', 'view_dht11');
INSERT INTO `auth_permission` VALUES ('41', 'Can add equipments', '11', 'add_equipments');
INSERT INTO `auth_permission` VALUES ('42', 'Can change equipments', '11', 'change_equipments');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete equipments', '11', 'delete_equipments');
INSERT INTO `auth_permission` VALUES ('44', 'Can view equipments', '11', 'view_equipments');
INSERT INTO `auth_permission` VALUES ('45', 'Can add fire', '12', 'add_fire');
INSERT INTO `auth_permission` VALUES ('46', 'Can change fire', '12', 'change_fire');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete fire', '12', 'delete_fire');
INSERT INTO `auth_permission` VALUES ('48', 'Can view fire', '12', 'view_fire');
INSERT INTO `auth_permission` VALUES ('49', 'Can add human', '13', 'add_human');
INSERT INTO `auth_permission` VALUES ('50', 'Can change human', '13', 'change_human');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete human', '13', 'delete_human');
INSERT INTO `auth_permission` VALUES ('52', 'Can view human', '13', 'view_human');
INSERT INTO `auth_permission` VALUES ('53', 'Can add infraredemission', '14', 'add_infraredemission');
INSERT INTO `auth_permission` VALUES ('54', 'Can change infraredemission', '14', 'change_infraredemission');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete infraredemission', '14', 'delete_infraredemission');
INSERT INTO `auth_permission` VALUES ('56', 'Can view infraredemission', '14', 'view_infraredemission');
INSERT INTO `auth_permission` VALUES ('57', 'Can add infraredreception', '15', 'add_infraredreception');
INSERT INTO `auth_permission` VALUES ('58', 'Can change infraredreception', '15', 'change_infraredreception');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete infraredreception', '15', 'delete_infraredreception');
INSERT INTO `auth_permission` VALUES ('60', 'Can view infraredreception', '15', 'view_infraredreception');
INSERT INTO `auth_permission` VALUES ('61', 'Can add led', '16', 'add_led');
INSERT INTO `auth_permission` VALUES ('62', 'Can change led', '16', 'change_led');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete led', '16', 'delete_led');
INSERT INTO `auth_permission` VALUES ('64', 'Can view led', '16', 'view_led');
INSERT INTO `auth_permission` VALUES ('65', 'Can add light', '17', 'add_light');
INSERT INTO `auth_permission` VALUES ('66', 'Can change light', '17', 'change_light');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete light', '17', 'delete_light');
INSERT INTO `auth_permission` VALUES ('68', 'Can view light', '17', 'view_light');
INSERT INTO `auth_permission` VALUES ('69', 'Can add obstacleavoidance', '18', 'add_obstacleavoidance');
INSERT INTO `auth_permission` VALUES ('70', 'Can change obstacleavoidance', '18', 'change_obstacleavoidance');
INSERT INTO `auth_permission` VALUES ('71', 'Can delete obstacleavoidance', '18', 'delete_obstacleavoidance');
INSERT INTO `auth_permission` VALUES ('72', 'Can view obstacleavoidance', '18', 'view_obstacleavoidance');
INSERT INTO `auth_permission` VALUES ('73', 'Can add pins', '19', 'add_pins');
INSERT INTO `auth_permission` VALUES ('74', 'Can change pins', '19', 'change_pins');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete pins', '19', 'delete_pins');
INSERT INTO `auth_permission` VALUES ('76', 'Can view pins', '19', 'view_pins');
INSERT INTO `auth_permission` VALUES ('77', 'Can add propertymapping', '20', 'add_propertymapping');
INSERT INTO `auth_permission` VALUES ('78', 'Can change propertymapping', '20', 'change_propertymapping');
INSERT INTO `auth_permission` VALUES ('79', 'Can delete propertymapping', '20', 'delete_propertymapping');
INSERT INTO `auth_permission` VALUES ('80', 'Can view propertymapping', '20', 'view_propertymapping');
INSERT INTO `auth_permission` VALUES ('81', 'Can add rain', '21', 'add_rain');
INSERT INTO `auth_permission` VALUES ('82', 'Can change rain', '21', 'change_rain');
INSERT INTO `auth_permission` VALUES ('83', 'Can delete rain', '21', 'delete_rain');
INSERT INTO `auth_permission` VALUES ('84', 'Can view rain', '21', 'view_rain');
INSERT INTO `auth_permission` VALUES ('85', 'Can add relay', '22', 'add_relay');
INSERT INTO `auth_permission` VALUES ('86', 'Can change relay', '22', 'change_relay');
INSERT INTO `auth_permission` VALUES ('87', 'Can delete relay', '22', 'delete_relay');
INSERT INTO `auth_permission` VALUES ('88', 'Can view relay', '22', 'view_relay');
INSERT INTO `auth_permission` VALUES ('89', 'Can add sensors', '23', 'add_sensors');
INSERT INTO `auth_permission` VALUES ('90', 'Can change sensors', '23', 'change_sensors');
INSERT INTO `auth_permission` VALUES ('91', 'Can delete sensors', '23', 'delete_sensors');
INSERT INTO `auth_permission` VALUES ('92', 'Can view sensors', '23', 'view_sensors');
INSERT INTO `auth_permission` VALUES ('93', 'Can add smoke', '24', 'add_smoke');
INSERT INTO `auth_permission` VALUES ('94', 'Can change smoke', '24', 'change_smoke');
INSERT INTO `auth_permission` VALUES ('95', 'Can delete smoke', '24', 'delete_smoke');
INSERT INTO `auth_permission` VALUES ('96', 'Can view smoke', '24', 'view_smoke');
INSERT INTO `auth_permission` VALUES ('97', 'Can add soil', '25', 'add_soil');
INSERT INTO `auth_permission` VALUES ('98', 'Can change soil', '25', 'change_soil');
INSERT INTO `auth_permission` VALUES ('99', 'Can delete soil', '25', 'delete_soil');
INSERT INTO `auth_permission` VALUES ('100', 'Can view soil', '25', 'view_soil');
INSERT INTO `auth_permission` VALUES ('101', 'Can add sound', '26', 'add_sound');
INSERT INTO `auth_permission` VALUES ('102', 'Can change sound', '26', 'change_sound');
INSERT INTO `auth_permission` VALUES ('103', 'Can delete sound', '26', 'delete_sound');
INSERT INTO `auth_permission` VALUES ('104', 'Can view sound', '26', 'view_sound');
INSERT INTO `auth_permission` VALUES ('105', 'Can add ultrasonic', '27', 'add_ultrasonic');
INSERT INTO `auth_permission` VALUES ('106', 'Can change ultrasonic', '27', 'change_ultrasonic');
INSERT INTO `auth_permission` VALUES ('107', 'Can delete ultrasonic', '27', 'delete_ultrasonic');
INSERT INTO `auth_permission` VALUES ('108', 'Can view ultrasonic', '27', 'view_ultrasonic');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'ssaicsp', 'activebuzzer');
INSERT INTO `django_content_type` VALUES ('8', 'ssaicsp', 'aroadtracing');
INSERT INTO `django_content_type` VALUES ('9', 'ssaicsp', 'current');
INSERT INTO `django_content_type` VALUES ('10', 'ssaicsp', 'dht11');
INSERT INTO `django_content_type` VALUES ('11', 'ssaicsp', 'equipments');
INSERT INTO `django_content_type` VALUES ('12', 'ssaicsp', 'fire');
INSERT INTO `django_content_type` VALUES ('13', 'ssaicsp', 'human');
INSERT INTO `django_content_type` VALUES ('14', 'ssaicsp', 'infraredemission');
INSERT INTO `django_content_type` VALUES ('15', 'ssaicsp', 'infraredreception');
INSERT INTO `django_content_type` VALUES ('16', 'ssaicsp', 'led');
INSERT INTO `django_content_type` VALUES ('17', 'ssaicsp', 'light');
INSERT INTO `django_content_type` VALUES ('18', 'ssaicsp', 'obstacleavoidance');
INSERT INTO `django_content_type` VALUES ('19', 'ssaicsp', 'pins');
INSERT INTO `django_content_type` VALUES ('20', 'ssaicsp', 'propertymapping');
INSERT INTO `django_content_type` VALUES ('21', 'ssaicsp', 'rain');
INSERT INTO `django_content_type` VALUES ('22', 'ssaicsp', 'relay');
INSERT INTO `django_content_type` VALUES ('23', 'ssaicsp', 'sensors');
INSERT INTO `django_content_type` VALUES ('24', 'ssaicsp', 'smoke');
INSERT INTO `django_content_type` VALUES ('25', 'ssaicsp', 'soil');
INSERT INTO `django_content_type` VALUES ('26', 'ssaicsp', 'sound');
INSERT INTO `django_content_type` VALUES ('27', 'ssaicsp', 'ultrasonic');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-08-04 14:54:12.259601');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-08-04 14:54:13.440859');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-08-04 14:54:13.771209');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-08-04 14:54:13.916992');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2018-08-04 14:54:13.976771');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2018-08-04 14:54:14.231040');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2018-08-04 14:54:14.361213');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2018-08-04 14:54:14.694640');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2018-08-04 14:54:14.768052');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2018-08-04 14:54:14.972196');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2018-08-04 14:54:14.988488');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2018-08-04 14:54:15.062844');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2018-08-04 14:54:15.609823');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2018-08-04 14:54:16.132759');
INSERT INTO `django_migrations` VALUES ('15', 'sessions', '0001_initial', '2018-08-04 14:54:16.230366');
INSERT INTO `django_migrations` VALUES ('16', 'ssaicsp', '0001_initial', '2018-08-04 15:14:07.637618');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_activebuzzer
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_activebuzzer`;
CREATE TABLE `ssaicsp_activebuzzer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_activebuzzer` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_activebuzzer
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_aroadtracing
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_aroadtracing`;
CREATE TABLE `ssaicsp_aroadtracing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_aroadtracing` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_aroadtracing
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_current
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_current`;
CREATE TABLE `ssaicsp_current` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `current_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_current
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_dht11
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_dht11`;
CREATE TABLE `ssaicsp_dht11` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `temperature` double NOT NULL,
  `humidity` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_dht11
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_equipments
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_equipments`;
CREATE TABLE `ssaicsp_equipments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rpi_code` varchar(20) NOT NULL,
  `rpi_name` varchar(20) NOT NULL,
  `remote_serverhost` varchar(20) NOT NULL,
  `remote_serverport` int(11) NOT NULL,
  `local_serverhost` varchar(20) NOT NULL,
  `local_serverport` int(11) NOT NULL,
  `local_servermaxconcount` int(11) NOT NULL,
  `local_clientcount` int(11) NOT NULL,
  `sendtime` int(11) NOT NULL,
  `checkcontime` int(11) NOT NULL,
  `equipmentInfos` varchar(255) DEFAULT NULL,
  `equipmentkey` varchar(255) DEFAULT NULL,
  `r1` varchar(255) DEFAULT NULL,
  `r2` varchar(255) DEFAULT NULL,
  `isciphertransfer` int(2) unsigned zerofill DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_equipments
-- ----------------------------
INSERT INTO `ssaicsp_equipments` VALUES ('1', '10011', '204rpi11', '172.16.55.162', '6666', '127.0.0.1', '8888', '10', '10', '15', '30', '1.0.1*15083520249*10011*2423B4B96630B779C12679F1D9C40295CD11029DB2FB288ADB697C96C58C5E5B01A1EEE6867288381727A1665CFE568ACD65AAF4F43AFD6FA10D51748BC934DE', '00020B040F080005', '47228156', '45967953', null, '2018-08-05 13:45:28.638641', '204rpi11', '1');

-- ----------------------------
-- Table structure for ssaicsp_fire
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_fire`;
CREATE TABLE `ssaicsp_fire` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_fire` int(11) NOT NULL,
  `fire_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_fire
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_human
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_human`;
CREATE TABLE `ssaicsp_human` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_human` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_human
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_infraredemission
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_infraredemission`;
CREATE TABLE `ssaicsp_infraredemission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_infraredemission` int(11) NOT NULL,
  `infraredemission_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_infraredemission
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_infraredreception
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_infraredreception`;
CREATE TABLE `ssaicsp_infraredreception` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_infraredreception` int(11) NOT NULL,
  `infraredreception_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_infraredreception
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_led
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_led`;
CREATE TABLE `ssaicsp_led` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_led` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_led
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_light
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_light`;
CREATE TABLE `ssaicsp_light` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_light` int(11) NOT NULL,
  `light_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_light
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_obstacleavoidance
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_obstacleavoidance`;
CREATE TABLE `ssaicsp_obstacleavoidance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_obstacleavoidance` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_obstacleavoidance
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_pins
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_pins`;
CREATE TABLE `ssaicsp_pins` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pin` int(11) DEFAULT NULL,
  `wPi` int(11) DEFAULT NULL,
  `BCM` int(11) DEFAULT NULL,
  `description` varchar(20) DEFAULT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_pins
-- ----------------------------
INSERT INTO `ssaicsp_pins` VALUES ('1', '1', null, null, '3.3V', '2018-07-13 10:04:47.000000', '1');
INSERT INTO `ssaicsp_pins` VALUES ('2', '2', null, null, '5.0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('3', '3', '8', '2', 'SDA.1', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('4', '4', null, null, '5.0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('5', '5', '9', '3', 'SCL.1', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('6', '6', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('7', '7', '7', '4', 'GPIO.7', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('8', '8', '15', '14', 'TxD', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('9', '9', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('10', '10', '16', '15', 'RxD', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('11', '11', '0', '17', 'GPIO.0', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('12', '12', '1', '18', 'GPIO.1', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('13', '13', '2', '27', 'GPIO.2', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('14', '14', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('15', '15', '3', '22', 'GPIO.3', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('16', '16', '4', '23', 'GPIO.4', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('17', '17', null, null, '3.3V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('18', '18', '5', '24', 'GPIO.5', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('19', '19', '12', '10', 'MOSI', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('20', '20', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('21', '21', '13', '9', 'MISO', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('22', '22', '6', '25', 'GPIO.6', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('23', '23', '14', '11', 'SCLK', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('24', '24', '10', '8', 'CE0', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('25', '25', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('26', '26', '11', '7', 'CE1', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('27', '27', '30', '0', 'SDA.0', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('28', '28', '31', '1', 'SCL.0', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('29', '29', '21', '5', 'GPIO.21', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('30', '30', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('31', '31', '22', '6', 'GPIO.22', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('32', '32', '26', '12', 'GPIO.26', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('33', '33', '23', '13', 'GPIO.23', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('34', '34', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('35', '35', '24', '19', 'GPIO.24', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('36', '36', '27', '16', 'GPIO.27', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('37', '37', '25', '26', 'GPIO.25', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('38', '38', '28', '20', 'GPIO.28', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('39', '39', null, null, '0V', null, null);
INSERT INTO `ssaicsp_pins` VALUES ('40', '40', '29', '21', 'GPIO.29', null, null);

-- ----------------------------
-- Table structure for ssaicsp_propertymapping
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_propertymapping`;
CREATE TABLE `ssaicsp_propertymapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_name` varchar(20) DEFAULT NULL,
  `property_value` varchar(20) DEFAULT NULL,
  `property_meaning` varchar(50) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `create_time` datetime(6) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_propertymapping
-- ----------------------------
INSERT INTO `ssaicsp_propertymapping` VALUES ('1', 'sensor_type', '1', 'activebuzzer', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('2', 'sensor_type', '2', 'aroadtracing', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('3', 'sensor_type', '3', 'dht11', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('4', 'sensor_type', '4', 'fire', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('5', 'sensor_type', '5', 'human', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('6', 'sensor_type', '6', 'infraredemission', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('7', 'sensor_type', '7', 'infraredreception', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('8', 'sensor_type', '8', 'light', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('9', 'sensor_type', '9', 'obstacleavoidance', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('10', 'sensor_type', '10', 'rain', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('11', 'sensor_type', '11', 'smoke', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('12', 'sensor_type', '12', 'soil', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('13', 'sensor_type', '13', 'sound', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('14', 'sensor_type', '14', 'ultrasonic', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('15', 'sensor_type', '15', 'led', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('16', 'sensor_type', '16', 'rgbled', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('17', 'sensor_type', '17', 'relay', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('18', 'sensor_type', '18', 'current', null, null, null);
INSERT INTO `ssaicsp_propertymapping` VALUES ('19', 'sensor_type', '19', 'xy', null, null, null);

-- ----------------------------
-- Table structure for ssaicsp_rain
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_rain`;
CREATE TABLE `ssaicsp_rain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_rain` int(11) NOT NULL,
  `rain_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_rain
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_relay
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_relay`;
CREATE TABLE `ssaicsp_relay` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_relay` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_relay
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_sensors
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_sensors`;
CREATE TABLE `ssaicsp_sensors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rpi_code` char(20) DEFAULT NULL,
  `sensor_code` char(3) DEFAULT NULL,
  `sensor_name` varchar(20) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `acqfre` double(10,2) DEFAULT NULL,
  `tranfre` double(10,2) DEFAULT NULL,
  `enable` int(11) DEFAULT NULL,
  `keep_time` int(11) DEFAULT NULL,
  `rediscount` int(11) DEFAULT NULL,
  `pins` varchar(50) DEFAULT NULL,
  `parameters` varchar(100) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_sensors
-- ----------------------------
INSERT INTO `ssaicsp_sensors` VALUES ('1', '10011', '1', '蜂鸣器1', '1', '0.00', '5.00', '0', '1', '10', '0', '', '2018-07-30 02:12:49', '收到收', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('2', '10011', '2', '寻迹1', '2', '0.00', '1.00', '0', '1', '10', '0', null, '2018-07-19 03:07:06', '1', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('3', '10011', '3', '温湿度1', '3', '2.00', '1.00', '0', '1', '10', '4', '', '2018-08-02 09:26:04', '引脚：', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('4', '10011', '4', '火焰1', '4', '1.00', '1.00', '0', '1', '10', '22,22', '', '2018-08-02 01:36:34', '引脚：do、ao', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('5', '10011', '5', '人体红外线1', '5', '0.00', '1.00', '0', '1', '10', '0', null, '2018-07-19 03:07:12', '引脚：', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('6', '10011', '6', '红外发射1', '6', '0.00', '1.00', '0', '1', '10', '0', null, '2018-07-19 03:07:14', '1', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('7', '10011', '7', '红外接收1', '7', '0.00', '1.00', '0', '1', '10', '0', null, '2018-07-27 07:30:56', '1', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('8', '10011', '8', '光敏1', '8', '2.00', '1.00', '0', '1', '10', '23,23', null, '2018-07-27 07:30:48', '引脚：do、ao', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('9', '10011', '9', '避障1', '9', '0.00', '1.00', '0', '1', '10', '7,7', null, '2018-07-19 03:07:18', '引脚：', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('10', '10011', '10', '雨滴1', '10', '2.00', '2.00', '0', '4', '10', '25,25', '', '2018-07-30 13:10:24', '引脚：do、ao', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('11', '10011', '11', '烟雾1', '11', '2.00', '1.00', '0', '1', '10', '27,27', null, '2018-07-28 02:39:53', '引脚：do、ao', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('12', '10011', '12', '土壤1', '12', '2.00', '1.00', '0', '1', '10', '24,24', '', '2018-08-01 09:03:40', '引脚：do、ao', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('13', '10011', '13', '声音1', '13', '0.00', '1.00', '0', '1', '10', '8,8', null, '2018-07-19 03:07:03', '引脚：', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('14', '10011', '14', '超声波1', '14', '2.00', '1.00', '0', '1', '10', '17,18', '', '2018-08-02 07:26:05', '引脚：do、ao', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('15', '10011', '15', '灯1', '15', '0.00', '1.00', '1', '1', '10', '14', '1', '2018-08-02 01:11:14', '参数：亮度（多个参数之前使用|隔开）', '1');
INSERT INTO `ssaicsp_sensors` VALUES ('16', '10011', '16', 'rgb灯1', '16', '0.00', '0.00', '0', '1', '10', '21,20,16', '0', '2018-07-28 15:05:46', '参数：亮度', null);
INSERT INTO `ssaicsp_sensors` VALUES ('17', '10011', '17', '继电器1', '17', '0.00', '0.00', '0', '1', '10', '12', '0', '2018-07-28 15:06:27', '参数：无', null);
INSERT INTO `ssaicsp_sensors` VALUES ('18', '10011', '18', '电流1', '18', '0.00', '0.00', '0', '1', '10', '26', '0', '2018-08-02 01:25:23', '参数：无', null);
INSERT INTO `ssaicsp_sensors` VALUES ('19', '10011', '19', '灯2', '15', '0.00', '1.00', '0', '1', '10', '12', '0.01', '2018-08-01 10:24:02', '参数：亮度', '1');

-- ----------------------------
-- Table structure for ssaicsp_smoke
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_smoke`;
CREATE TABLE `ssaicsp_smoke` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_smoke` int(11) NOT NULL,
  `smoke_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_smoke
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_soil
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_soil`;
CREATE TABLE `ssaicsp_soil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_soil` int(11) NOT NULL,
  `soil_value` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_soil
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_sound
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_sound`;
CREATE TABLE `ssaicsp_sound` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `is_sound` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_sound
-- ----------------------------

-- ----------------------------
-- Table structure for ssaicsp_ultrasonic
-- ----------------------------
DROP TABLE IF EXISTS `ssaicsp_ultrasonic`;
CREATE TABLE `ssaicsp_ultrasonic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_code` varchar(3) NOT NULL,
  `distance` double NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ssaicsp_ultrasonic
-- ----------------------------
SET FOREIGN_KEY_CHECKS=1;
