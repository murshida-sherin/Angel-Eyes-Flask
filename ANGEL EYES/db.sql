/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - angel_eyes
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`angel_eyes` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `angel_eyes`;

/*Table structure for table `blind_person` */

DROP TABLE IF EXISTS `blind_person`;

CREATE TABLE `blind_person` (
  `V_id` int(20) NOT NULL AUTO_INCREMENT,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Gender` varchar(15) NOT NULL,
  `DOB` date NOT NULL,
  `Place` varchar(20) NOT NULL,
  `Post` varchar(20) NOT NULL,
  `Pin` bigint(15) NOT NULL,
  `Phone` bigint(20) NOT NULL,
  `IMEI_NO` varchar(25) NOT NULL,
  `care_id` int(15) NOT NULL,
  PRIMARY KEY (`V_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `blind_person` */

insert  into `blind_person`(`V_id`,`First_Name`,`Last_Name`,`Gender`,`DOB`,`Place`,`Post`,`Pin`,`Phone`,`IMEI_NO`,`care_id`) values 
(1,'fiyas','rahman','male','2021-11-29','adefsdgf','ffgrthrthyh',457542,9876789787,'754645',2),
(2,'savad','coco','male','2222-02-22','nnjryryruu','jnnjnfutuytgig',678576,6858656851,'685867568756786',2),
(3,'ibru','ashiq','male','2007-02-14','rhryjtyu','deytjytf',968620,8989856523,'4665',7);

/*Table structure for table `care_taker` */

DROP TABLE IF EXISTS `care_taker`;

CREATE TABLE `care_taker` (
  `c_id` int(15) NOT NULL AUTO_INCREMENT,
  `Login_id` int(15) NOT NULL,
  `First_Name` varchar(100) NOT NULL,
  `Last_Name` varchar(100) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `Place` varchar(25) NOT NULL,
  `Post` varchar(25) NOT NULL,
  `Pin` int(15) NOT NULL,
  `Phone` bigint(20) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Status` varchar(25) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `care_taker` */

insert  into `care_taker`(`c_id`,`Login_id`,`First_Name`,`Last_Name`,`Gender`,`DOB`,`Place`,`Post`,`Pin`,`Phone`,`Email`,`Status`) values 
(1,2,'shamnad','pilathodan','male','2000-11-13','irumbuzi','anakkayam',676505,8978654536,'shammi@gmail.com','pending'),
(2,5,'murshida','sherin','female','2020-06-02','olavattoor','srgfdh',564778,9764646464,'mursj@gmail.com','pending'),
(3,6,'anu','minu','female','2021-12-03','tg','rtg',9876,9876543234,'h@gmail.com','pending'),
(4,7,'fazil','pachu','male','1999-11-14','irumbuzi','anakakyam',676509,9689563215,'pachu@gmail.com','pending');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `Complaint_id` int(15) NOT NULL AUTO_INCREMENT,
  `User_id` int(15) NOT NULL,
  `Date` varchar(50) NOT NULL,
  `Complaint` varchar(50) NOT NULL,
  `Replay` varchar(50) NOT NULL,
  PRIMARY KEY (`Complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`Complaint_id`,`User_id`,`Date`,`Complaint`,`Replay`) values 
(1,2,'2021-12-18','QWRERTYYUUI','ok daaa'),
(2,2,'2021-12-19','ok daaa','ok bie'),
(3,2,'2021-12-19','ok daaa','pending'),
(4,2,'2021-12-30','hfffhff','pending'),
(5,2,'2022-01-15','rtyrgh','pending');

/*Table structure for table `familiar_person` */

DROP TABLE IF EXISTS `familiar_person`;

CREATE TABLE `familiar_person` (
  `f_id` int(15) NOT NULL AUTO_INCREMENT,
  `blind_id` int(15) NOT NULL,
  `name` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL,
  `relation` varchar(50) NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `familiar_person` */

insert  into `familiar_person`(`f_id`,`blind_id`,`name`,`image`,`relation`) values 
(2,1,'churutt ibrahim','abigail-keenan-8-s5QuUBtyM-unsplash.jpg','bro'),
(5,1,'bishir mohd','mathias-herheim-mzwMBFUOECQ-unsplash.jpg','annan'),
(7,1,'safwan','admin_bg.jpg','vappa');

/*Table structure for table `help` */

DROP TABLE IF EXISTS `help`;

CREATE TABLE `help` (
  `HELP_ID` int(15) NOT NULL AUTO_INCREMENT,
  `imei` varchar(100) NOT NULL,
  `DATE` date NOT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`HELP_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `help` */

insert  into `help`(`HELP_ID`,`imei`,`DATE`,`latitude`,`longitude`) values 
(1,'754645','2021-12-10','11.111','12.121'),
(2,'685867568756786','2021-12-13','32.332','19.253');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `blind_id` int(15) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`id`,`blind_id`,`latitude`,`longitude`) values 
(1,1,'22.2425','11.234'),
(2,2,'11.987','18.564');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`user_name`,`password`,`type`) values 
(1,'thabsheer','angeleyes','admin'),
(2,'shamnad','angeleyes','caretaker'),
(5,'murshida','123','caretaker'),
(6,'qwerty','123','pending'),
(7,'pachu','Pachu123','caretaker');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
