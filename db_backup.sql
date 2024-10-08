-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: quantum_chat
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.22.04.1

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
-- Table structure for table `curve_prekey`
--

DROP TABLE IF EXISTS `curve_prekey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curve_prekey` (
  `uid` varchar(40) NOT NULL,
  `key_value` text,
  `key_identifier` text,
  `key_signature` text,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`),
  CONSTRAINT `curve_prekey_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curve_prekey`
--

LOCK TABLES `curve_prekey` WRITE;
/*!40000 ALTER TABLE `curve_prekey` DISABLE KEYS */;
/*!40000 ALTER TABLE `curve_prekey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `friend_relation`
--

DROP TABLE IF EXISTS `friend_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `friend_relation` (
  `id` int NOT NULL,
  `uid1` varchar(40) NOT NULL,
  `uid2` varchar(40) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid2` (`uid2`),
  CONSTRAINT `friend_relation_ibfk_2` FOREIGN KEY (`uid2`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friend_relation`
--

LOCK TABLES `friend_relation` WRITE;
/*!40000 ALTER TABLE `friend_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `friend_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `identity_key`
--

DROP TABLE IF EXISTS `identity_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `identity_key` (
  `uid` varchar(40) NOT NULL,
  `key_value` text,
  `key_value_x` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`),
  CONSTRAINT `identity_key_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `identity_key`
--

LOCK TABLES `identity_key` WRITE;
/*!40000 ALTER TABLE `identity_key` DISABLE KEYS */;
/*!40000 ALTER TABLE `identity_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message_sent`
--

DROP TABLE IF EXISTS `message_sent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message_sent` (
  `id` int NOT NULL,
  `receiver` text NOT NULL,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message_sent`
--

LOCK TABLES `message_sent` WRITE;
/*!40000 ALTER TABLE `message_sent` DISABLE KEYS */;
/*!40000 ALTER TABLE `message_sent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `one_time_curve_key`
--

DROP TABLE IF EXISTS `one_time_curve_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `one_time_curve_key` (
  `id` int NOT NULL,
  `uid` varchar(40) NOT NULL,
  `key_value` text,
  `key_identifier` text,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `one_time_curve_key_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one_time_curve_key`
--

LOCK TABLES `one_time_curve_key` WRITE;
/*!40000 ALTER TABLE `one_time_curve_key` DISABLE KEYS */;
/*!40000 ALTER TABLE `one_time_curve_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `one_time_pq_key`
--

DROP TABLE IF EXISTS `one_time_pq_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `one_time_pq_key` (
  `id` int NOT NULL,
  `uid` varchar(40) NOT NULL,
  `key_value` text,
  `key_identifier` text,
  `key_signature` text,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `one_time_pq_key_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one_time_pq_key`
--

LOCK TABLES `one_time_pq_key` WRITE;
/*!40000 ALTER TABLE `one_time_pq_key` DISABLE KEYS */;
/*!40000 ALTER TABLE `one_time_pq_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `otp_verify`
--

DROP TABLE IF EXISTS `otp_verify`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `otp_verify` (
  `id` int NOT NULL,
  `email` text,
  `otp` varchar(6) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `otp_verify`
--

LOCK TABLES `otp_verify` WRITE;
/*!40000 ALTER TABLE `otp_verify` DISABLE KEYS */;
/*!40000 ALTER TABLE `otp_verify` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pq_key`
--

DROP TABLE IF EXISTS `pq_key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pq_key` (
  `uid` varchar(40) NOT NULL,
  `key_value` text,
  `key_identifier` text NOT NULL,
  `key_signature` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`),
  CONSTRAINT `pq_key_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pq_key`
--

LOCK TABLES `pq_key` WRITE;
/*!40000 ALTER TABLE `pq_key` DISABLE KEYS */;
/*!40000 ALTER TABLE `pq_key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `uid` varchar(40) NOT NULL,
  `username` text,
  `email` text,
  `password` text,
  `profile_url` text,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('7a2a9c50977b','Bob','bob@gmail.com','$2b$16$KCt5jXU4enHS16uHKmmQh.iEsWzuyHTu3p4L7ftYUEN8tmPjv2zAK',NULL,'2024-08-31 00:54:45'),('808989c65e4a','Jameson','james2@gmail.com','$2b$16$yw9h/iwID4OK3KQ7EIcrlOU.iHhfSPSgkjDJ/aWybcFF4J3sTB48G',NULL,'2024-08-31 11:31:05'),('ec7eab5dabf3','james','james@gmail.com','$2b$16$24A19KWuGwcGRVOOySzZhu7WQdTIcj/w0.xHp2QOSE4WW3CVf.J.e',NULL,'2024-08-31 00:53:02');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_register`
--

DROP TABLE IF EXISTS `user_register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_register` (
  `id` int NOT NULL,
  `email` text,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_register`
--

LOCK TABLES `user_register` WRITE;
/*!40000 ALTER TABLE `user_register` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-07 12:32:11
