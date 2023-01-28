-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.18-nt


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema mobile
--

CREATE DATABASE IF NOT EXISTS mobile;
USE mobile;

--
-- Definition of table `brand`
--

DROP TABLE IF EXISTS `brand`;
CREATE TABLE `brand` (
  `BrandId` int(10) unsigned NOT NULL auto_increment,
  `BrandName` varchar(45) NOT NULL,
  PRIMARY KEY  (`BrandId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `brand`
--

/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` (`BrandId`,`BrandName`) VALUES 
 (1,'Samsung'),
 (2,'Xiaomi'),
 (3,'Vivo'),
 (4,'Oppo'),
 (5,'Apple');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;


--
-- Definition of table `modeldetails`
--

DROP TABLE IF EXISTS `modeldetails`;
CREATE TABLE `modeldetails` (
  `ModelNumber` varchar(50) NOT NULL,
  `BrandId` varchar(20) NOT NULL,
  `ModelName` varchar(50) NOT NULL,
  `Price` double NOT NULL,
  `Features` varchar(100) NOT NULL,
  `Quantity` int(10) unsigned NOT NULL,
  PRIMARY KEY  (`ModelNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `modeldetails`
--

/*!40000 ALTER TABLE `modeldetails` DISABLE KEYS */;
INSERT INTO `modeldetails` (`ModelNumber`,`BrandId`,`ModelName`,`Price`,`Features`,`Quantity`) VALUES 
 ('1','1','samsung',230000,'8GB',3),
 ('2','2','xioami',19999,'8gb',1),
 ('AP-786YY','5','Apple iphone XR',59000,'storage,ram: 64GB,6GB, Camera: 48MP+5MP Dual primary, Battery:5000mah',4),
 ('OO-987UH','4','OPPO Reno Z',25000,'storage,ram: 256GB,6GB, Camera: 48MP+5MP Dual primary, Battery:5000mah',1),
 ('SG-406M7','1','Samsung Galaxy M40',19990,'storage,ram: 128GB,6GB, Camera:32MP Triple Rear Camera, Battery:4000mah',5),
 ('SM-G610F','1','Samsung Galaxy J7 Prime',18000,'storage,ram: 64GB,4GB, Camera: 13MP+5MP Dual primary, Battery:3300mah',2),
 ('VO-56V6R','3','Vivo Z1 Pro',14990,'storage,ram: 64GB,4GB, Camera: 10MP+4MP Dual primary, Battery:5000mah',3),
 ('VV-43KF4','3','Vivo Y7',18999,'storage,ram: 64GB,4GB, Camera: 10MP+4MP+7MP Triple primary Camera, Battery:5000mah',2),
 ('XM-582ZE','2','Xiaomi MI Mix 3 5G ',25000,'storage,ram: 128GB,6GB, Camera: 24MP+4MP Dual primary, Battery:3800mah',4),
 ('XP-67G4R','2','Xiaomi Poco F1',17999,'storage,ram: 64GB,4GB, Camera: 12MP+5MP Dual primary, Battery:4000mah',8);
/*!40000 ALTER TABLE `modeldetails` ENABLE KEYS */;


--
-- Definition of table `sales`
--

DROP TABLE IF EXISTS `sales`;
CREATE TABLE `sales` (
  `TransactionId` int(10) unsigned NOT NULL auto_increment,
  `ModelNumber` varchar(45) NOT NULL,
  `Quantity` int(10) unsigned NOT NULL,
  `CustomerName` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`TransactionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales`
--

/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` (`TransactionId`,`ModelNumber`,`Quantity`,`CustomerName`,`Email`,`Address`,`Phone`,`Date`) VALUES 
 (1,'AP-786YY',1,'Arina','sameeksha204@gmail.com','ABC-Colony','9415870923','2018-02-19'),
 (2,'SG-406M7',1,'Era','ektayadav204@gmail.com','123-house no.','9792697220','2018-09-15'),
 (3,'VO-56V6R',1,'Nile','vanshajshivhare99@gmail.com','201-colony','7317876980','2019-01-05'),
 (4,'XM-582ZE',1,'Ali','sryadav@gmail.com','tr-colony','9415870923','2019-05-02'),
 (13,'GT456H',2,'ALEA','allea@gmail.com','acv-colony','12457896','2018-05-02');
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
