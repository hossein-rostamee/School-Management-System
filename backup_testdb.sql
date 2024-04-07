-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add class',7,'add_class'),(26,'Can change class',7,'change_class'),(27,'Can delete class',7,'delete_class'),(28,'Can view class',7,'view_class'),(29,'Can add users',8,'add_users'),(30,'Can change users',8,'change_users'),(31,'Can delete users',8,'delete_users'),(32,'Can view users',8,'view_users'),(33,'Can add volunteer',9,'add_volunteer'),(34,'Can change volunteer',9,'change_volunteer'),(35,'Can delete volunteer',9,'delete_volunteer'),(36,'Can view volunteer',9,'view_volunteer'),(37,'Can add student',10,'add_student'),(38,'Can change student',10,'change_student'),(39,'Can delete student',10,'delete_student'),(40,'Can view student',10,'view_student');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$VKUqdE1LiXK7joQ2aaZiP8$FLrAQyR93yAGJ22NRpudzqRVOdsciJmMbwXD0V22rg8=','2023-11-06 13:44:12.595381',1,'test','','','rostamee1@gmail.com',1,1,'2023-11-06 10:20:43.828945');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-11-06 13:44:38.336115','hossein','hossein',1,'[{\"added\": {}}]',8,1),(2,'2023-11-07 12:16:31.432287','1','Class object (1)',1,'[{\"added\": {}}]',7,1),(3,'2023-11-07 17:31:31.400619','2','Class object (2)',1,'[{\"added\": {}}]',7,1),(4,'2023-11-07 17:42:23.687137','3','Class object (3)',1,'[{\"added\": {}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'register','class'),(10,'register','student'),(8,'register','users'),(9,'register','volunteer'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-11-06 09:52:16.862481'),(2,'auth','0001_initial','2023-11-06 09:52:20.333266'),(3,'admin','0001_initial','2023-11-06 09:52:21.072091'),(4,'admin','0002_logentry_remove_auto_add','2023-11-06 09:52:21.114432'),(5,'admin','0003_logentry_add_action_flag_choices','2023-11-06 09:52:21.171604'),(6,'contenttypes','0002_remove_content_type_name','2023-11-06 09:52:21.641755'),(7,'auth','0002_alter_permission_name_max_length','2023-11-06 09:52:21.976763'),(8,'auth','0003_alter_user_email_max_length','2023-11-06 09:52:22.149697'),(9,'auth','0004_alter_user_username_opts','2023-11-06 09:52:22.197100'),(10,'auth','0005_alter_user_last_login_null','2023-11-06 09:52:22.483560'),(11,'auth','0006_require_contenttypes_0002','2023-11-06 09:52:22.512986'),(12,'auth','0007_alter_validators_add_error_messages','2023-11-06 09:52:22.569919'),(13,'auth','0008_alter_user_username_max_length','2023-11-06 09:52:22.973967'),(14,'auth','0009_alter_user_last_name_max_length','2023-11-06 09:52:23.350734'),(15,'auth','0010_alter_group_name_max_length','2023-11-06 09:52:23.457440'),(16,'auth','0011_update_proxy_permissions','2023-11-06 09:52:23.507384'),(17,'auth','0012_alter_user_first_name_max_length','2023-11-06 09:52:23.877305'),(18,'register','0001_initial','2023-11-06 09:52:25.228434'),(19,'register','0002_student_whichbooksdoyouliketoread_and_more','2023-11-06 09:52:26.026997'),(20,'register','0003_student_date_volunteer_date','2023-11-06 09:52:26.603740'),(21,'register','0004_student_whatlevelofskilldoyouhaveinculturalactivity_and_more','2023-11-06 09:52:27.444516'),(22,'sessions','0001_initial','2023-11-06 09:52:27.775146');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('dpaz7lkoy2ltvrg13v7uflvp5njlu5wz','.eJxVjDkOwjAUBe_iGllego0p6TmD9TfjAHKkOKkQd4dIKaB9M_NeKsO61Lx2mfPI6qysOvxuCPSQtgG-Q7tNmqa2zCPqTdE77fo6sTwvu_t3UKHXb02FkoscPIAQGnAJI8kJj64kELYBTXFUjLHkvLecIEZXWMQPBgMN6v0BG205Cg:1qzwms:wQOp3846PPOJC7ldT1NIq0OSdCLIxsr7dwReS2057YQ','2023-11-20 10:24:54.091441'),('f6etvuajmxagqjxukfiaag8tjdg6uhbh','.eJxVjDkOwjAUBe_iGllego0p6TmD9TfjAHKkOKkQd4dIKaB9M_NeKsO61Lx2mfPI6qysOvxuCPSQtgG-Q7tNmqa2zCPqTdE77fo6sTwvu_t3UKHXb02FkoscPIAQGnAJI8kJj64kELYBTXFUjLHkvLecIEZXWMQPBgMN6v0BG205Cg:1qzztk:Po1FNjbQxuFQUynhZEXQ-OTd9lCg_cPgKFHmdkDjA3k','2023-11-20 13:44:12.616482');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_class`
--

DROP TABLE IF EXISTS `register_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_class` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `anvar_name` varchar(30) NOT NULL,
  `anvar_startTime` time(6) NOT NULL,
  `anvar_endTime` time(6) NOT NULL,
  `anvar_location` varchar(30) NOT NULL,
  `anvar_dayInWeek` varchar(30) NOT NULL,
  `anvar_grade` varchar(30) NOT NULL,
  `anvar_moreDetail` longtext NOT NULL,
  `anvar_teacher` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_class`
--

LOCK TABLES `register_class` WRITE;
/*!40000 ALTER TABLE `register_class` DISABLE KEYS */;
INSERT INTO `register_class` VALUES (1,'کلاس نقاشی','12:00:00.000000','14:00:00.000000','دیپارتمان هنری','شنبه ها','از اول تا پنجم ابتدایی','همراه خود آبرنگ بیاورید','سلیمانی'),(2,'کلاس شیمی','14:00:00.000000','16:00:00.000000','اتاق شاندیز','سه شنبه ها و پنجشنبه ها','دهم تا دوازهم','همراه خود کتاب تست بهمن بازرگان را بیاورید','بهمن بازرگان'),(3,'کلاس فیزیک','15:00:00.000000','18:00:00.000000','بخش علوم','دوشنبه ها و یکشنبه ها','ششم تا نهم','کتاب فیزیک هالیدی را همراه خود بیاورید','جعفر حبیبی');
/*!40000 ALTER TABLE `register_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_student`
--

DROP TABLE IF EXISTS `register_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_student` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `anvar_fullName` varchar(30) NOT NULL,
  `anvar_fatherName` varchar(30) NOT NULL,
  `anvar_birthCity` varchar(30) NOT NULL,
  `anvar_schoolName` varchar(30) NOT NULL,
  `anvar_classNumber` varchar(30) NOT NULL,
  `anvar_birthDate` date NOT NULL,
  `anvar_nationalCode` varchar(15) NOT NULL,
  `anvar_fatherPhoneNumber` varchar(15) NOT NULL,
  `anvar_motherPhoneNumber` varchar(15) NOT NULL,
  `anvar_schoolShift` varchar(30) NOT NULL,
  `anvar_religion` varchar(30) NOT NULL,
  `anvar_grade` varchar(30) NOT NULL,
  `anvar_personelPhoto` varchar(100) NOT NULL,
  `anvar_birthCertificate` varchar(100) NOT NULL,
  `anvar_passField` varchar(50) NOT NULL,
  `anvar_whatIsParentsGrade` longtext NOT NULL,
  `anvar_howDidGetToKnowQuranSessions` longtext NOT NULL,
  `anvar_WhoEncourageYouToComeQuranSessions` longtext NOT NULL,
  `anvar_WhichSessionDidYouParticipate` longtext NOT NULL,
  `anvar_WhichSportsDoYouInterestedIn` longtext NOT NULL,
  `anvar_WhichBooksDoYouRecentlyRead` longtext NOT NULL,
  `anvar_WriteTheNamesOfYourTwoFriends` longtext NOT NULL,
  `anvar_WhichCulturalActivitiesDoYouInterested` longtext NOT NULL,
  `anvar_WhichFieldsDoYouTalentedIn` longtext NOT NULL,
  `anvar_HowMuchDoYouFamiliarWithQuran` longtext NOT NULL,
  `anvar_WhichCommitionsDoYouInterestedIn` longtext NOT NULL,
  `anvar_HowDoYouSpendYourHolidays` longtext NOT NULL,
  `classitem_id` bigint DEFAULT NULL,
  `user_id` varchar(100) NOT NULL,
  `anvar_WhichBooksDoYouLikeToRead` longtext NOT NULL DEFAULT (_utf8mb3''),
  `anvar_date` date NOT NULL,
  `anvar_WhatLevelofSkillDoYouHaveInCulturalActivity` longtext NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `register_student_classitem_id_2af7853b_fk_register_class_id` (`classitem_id`),
  CONSTRAINT `register_student_classitem_id_2af7853b_fk_register_class_id` FOREIGN KEY (`classitem_id`) REFERENCES `register_class` (`id`),
  CONSTRAINT `register_student_user_id_f2621c1f_fk_register_users_user_name` FOREIGN KEY (`user_id`) REFERENCES `register_users` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_student`
--

LOCK TABLES `register_student` WRITE;
/*!40000 ALTER TABLE `register_student` DISABLE KEYS */;
INSERT INTO `register_student` VALUES (1,'حسین','محمد ','تهران','رشد','','2023-10-31','38755555','09104019912','093888888','صبح','شیعه','هشتم','documents/images_3.jpg','documents/shenas.jpg','hosseinhossein','لیسانس ','دوستم','خودم','خیر ','تنیس','بی نوایان','یاسر و چنگیز','مداحی,فیلم برداری','شیمی,سرود خوانی','خوب',' هنر و رسانه,عکس برداری','سینما,اشتغال به‌كار',3,'u14021','علمی','2023-11-06','خیلی زیاد'),(2,'حسین رستمی ','حیدر','همدان','رشد ','','1983-10-30','02545555','09155555555','093715444444','صبح','شیعه','ششم','documents/images_2.jpg','documents/imagesshenams.jpg','rostamirostami','دیپلم','دوستم','همسرم','خیر','تنیس','چهار اثر از فلورانس اسکاول شین ','حمید و سپهر','زبان,نقاشی,قرائت قرآن','شیمی,سرود خوانی','خوب,متوسط','اردویی, کتاب و فرهنگ مطالعه','معاشرت با دوستان, فعالیت های هنری',3,'u14022','هنری','2023-11-07','بسیار بالا');
/*!40000 ALTER TABLE `register_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_users`
--

DROP TABLE IF EXISTS `register_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_users` (
  `user_name` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_role` int unsigned NOT NULL,
  PRIMARY KEY (`user_name`),
  CONSTRAINT `register_users_chk_1` CHECK ((`user_role` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_users`
--

LOCK TABLES `register_users` WRITE;
/*!40000 ALTER TABLE `register_users` DISABLE KEYS */;
INSERT INTO `register_users` VALUES ('hossein','rostami',1330),('u14021','hosseinhossein',1540),('u14022','rostamirostami',1540),('u14023','1234567890',1540),('u14024','testtesttest',1540);
/*!40000 ALTER TABLE `register_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_volunteer`
--

DROP TABLE IF EXISTS `register_volunteer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_volunteer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `anvar_fullName` varchar(30) NOT NULL,
  `anvar_fatherName` varchar(30) NOT NULL,
  `anvar_birthCity` varchar(30) NOT NULL,
  `anvar_schoolName` varchar(30) NOT NULL,
  `anvar_classNumber` varchar(30) NOT NULL,
  `anvar_passField` varchar(50) NOT NULL,
  `anvar_birthDate` date NOT NULL,
  `anvar_nationalCode` varchar(15) NOT NULL,
  `anvar_fatherPhoneNumber` varchar(15) NOT NULL,
  `anvar_motherPhoneNumber` varchar(15) NOT NULL,
  `anvar_schoolShift` varchar(30) NOT NULL,
  `anvar_religion` varchar(30) NOT NULL,
  `anvar_grade` varchar(30) NOT NULL,
  `anvar_whatIsParentsGrade` longtext NOT NULL,
  `anvar_howDidGetToKnowQuranSessions` longtext NOT NULL,
  `anvar_WhoEncourageYouToComeQuranSessions` longtext NOT NULL,
  `anvar_WhichSessionDidYouParticipate` longtext NOT NULL,
  `anvar_WhichSportsDoYouInterestedIn` longtext NOT NULL,
  `anvar_WhichBooksDoYouRecentlyRead` longtext NOT NULL,
  `anvar_WriteTheNamesOfYourTwoFriends` longtext NOT NULL,
  `anvar_WhichCulturalActivitiesDoYouInterested` longtext NOT NULL,
  `anvar_WhichFieldsDoYouTalentedIn` longtext NOT NULL,
  `anvar_HowMuchDoYouFamiliarWithQuran` longtext NOT NULL,
  `anvar_WhichCommitionsDoYouInterestedIn` longtext NOT NULL,
  `anvar_HowDoYouSpendYourHolidays` longtext NOT NULL,
  `anvar_personelPhoto` varchar(100) NOT NULL,
  `anvar_birthCertificate` varchar(100) NOT NULL,
  `anvar_WhichBooksDoYouLikeToRead` longtext NOT NULL DEFAULT (_utf8mb3''),
  `anvar_date` date NOT NULL,
  `anvar_WhatLevelofSkillDoYouHaveInCulturalActivity` longtext NOT NULL DEFAULT (_utf8mb3''),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_volunteer`
--

LOCK TABLES `register_volunteer` WRITE;
/*!40000 ALTER TABLE `register_volunteer` DISABLE KEYS */;
INSERT INTO `register_volunteer` VALUES (6,'شهروز فدایی','جلیل','تهران','هدایت','777','sdsdasdasdasd','2011-02-01','3856666666','09185555555','0966666666','صبح','شیعه','دهم','زیاد','نمیدانم','اطلاعی ندارم','که چه ','نمیدانم','اطلاعی ندارم','اطلاعی ندارم','زبان','شیمی,قصه گویی,حفظ شعر','زیاد,خوب','اردویی,برگزاری جشن, هنر و رسانه','گردش, بازی های گروهی, فعالیت های هنری,سینما,تماشای تلویزیون','documents/images_1.jpg','documents/2289666_695.jpg','نمیدانم','2023-11-08','نمیدانم');
/*!40000 ALTER TABLE `register_volunteer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-29 12:30:08
