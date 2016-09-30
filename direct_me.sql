CREATE DATABASE  IF NOT EXISTS `direct_me` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `direct_me`;
-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: direct_me
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(45) DEFAULT NULL,
  `weather_location_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (1,'san francisco','5391959'),(2,'houston','4391354'),(3,'new york','5128638'),(4,'chicago','4887398');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` varchar(45) DEFAULT NULL,
  `cities_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_users_cities_idx` (`cities_id`),
  CONSTRAINT `fk_users_cities` FOREIGN KEY (`cities_id`) REFERENCES `cities` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (20,'kenny ko','kenny@gmail.com','$2b$12$K2Zo0Zn8SpIek7bW0dwc1ujeHTG0ZM21ybM.AuIQNDlq8DLdc0DAe','2016-09-28 19:30:49',NULL,1),(21,'queenie ho','queenie@gmail.com','$2b$12$KnrW0tcEY7yPcYC9fOKh9unuPFs16zeDGUcN1DVlxNIYYc4F0NLYy','2016-09-28 19:31:32',NULL,2),(22,'devan wong','devan@gmail.com','$2b$12$xUf7QBIupbh9insDt2C/6.PMqCRJzN22mBe9K5N46.McWZaWftdU6','2016-09-28 19:52:05',NULL,3),(23,'jill robinson','jill@gmail.com','$2b$12$nQV94Ki3GIbJ.ExHJXCuY.cGYkcxGlBvY2BXdaikFwJoRgxVVnwka','2016-09-28 19:52:35',NULL,4),(24,'Daniel','danny@gmail.com','$2b$12$AeZBhqSGYpC1S/NQvetjwujS5S6AFhlrCWlUTl5FQqB14aLrD1NTW','2016-09-29 23:58:43',NULL,1),(27,'zippy','zippy@gmail.com','$2b$12$/1BgAVEEzfCSswfgVe30EO9DbDzhn5N67M0HPfPqsZeroKSwVUc6i','2016-09-30 00:06:05',NULL,3),(29,'noggin','noggin@gmail.com','$2b$12$lelYfaks1GTWnjkRUF74Aev/x.uWhxsjSql7Ns40M.EF9p31HrcAe','2016-09-30 07:25:13',NULL,2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-30  8:54:35
