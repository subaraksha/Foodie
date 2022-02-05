-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: foodie
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `Name` varchar(30) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Phone_no` char(10) NOT NULL,
  `Wallet` double(7,2) DEFAULT '0.00',
  PRIMARY KEY (`Phone_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('Thenmozhi','87 Anna Nagar, Karur','8050825989',150.00),('Subbu','87 Karur','9894486843',100.00),('Ravi','47 chettipalayam','9952256646',100.00);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotels`
--

DROP TABLE IF EXISTS `hotels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotels` (
  `Hotel_id` char(4) NOT NULL,
  `Hotel_name` varchar(50) DEFAULT NULL,
  `Phone_no` char(10) DEFAULT NULL,
  `Address` varchar(300) DEFAULT NULL,
  `Wallet` double(7,2) DEFAULT '0.00',
  PRIMARY KEY (`Hotel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotels`
--

LOCK TABLES `hotels` WRITE;
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
INSERT INTO `hotels` VALUES ('H001','Ananda Bhavan','9894400000','Karur',0.00),('H002','Anjappar','9894411111','Karur',400.00);
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `Menu_id` char(4) NOT NULL,
  `Menu_name` varchar(50) DEFAULT NULL,
  `Type` varchar(2) DEFAULT NULL,
  `Category` varchar(30) DEFAULT NULL,
  `Price` double(8,2) DEFAULT NULL,
  `Hotel_id` char(4) NOT NULL,
  PRIMARY KEY (`Menu_id`,`Hotel_id`),
  KEY `Hotel_id` (`Hotel_id`),
  CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`Hotel_id`) REFERENCES `hotels` (`Hotel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES ('M001','Dosa','V','SouthIndian',15.00,'H001'),('M001','Dosa','V','SouthIndian',20.00,'H002'),('M002','Chapathi','V','NorthIndian',10.00,'H001'),('M003','Roti','V','NorthIndian',25.00,'H002'),('M004','Chicken Manjurian','NV','NorthIndian',100.00,'H002');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `Order_id` int NOT NULL AUTO_INCREMENT,
  `Qty` int DEFAULT NULL,
  `Amt` double(7,2) DEFAULT NULL,
  `Date` datetime DEFAULT CURRENT_TIMESTAMP,
  `Pay_status` varchar(20) DEFAULT 'Pending',
  `Menu_id` char(4) DEFAULT NULL,
  `Hotel_id` char(4) DEFAULT NULL,
  `Phone_no` char(10) DEFAULT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `Menu_id` (`Menu_id`,`Hotel_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`Menu_id`, `Hotel_id`) REFERENCES `menu` (`Menu_id`, `Hotel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-25 22:31:45
