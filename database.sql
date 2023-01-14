/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.3.20-MariaDB : Database - text_sentiment_analysis
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`text_sentiment_analysis` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `text_sentiment_analysis`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `emotion` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`receiver_id`,`message`,`date`,`emotion`,`time`) values (12,2,3,'fe','2023-01-14 09:23:56','No output','09:23:56'),(11,2,3,'hau','2023-01-14 09:23:54','No output','09:23:54'),(10,2,3,'pitty of you','2023-01-14 09:23:49','shame','09:23:49'),(9,2,3,'pitty of you','2023-01-14 09:23:49','shame','09:23:49'),(8,2,3,'hello','2023-01-13 11:44:53','No output','11:44:53'),(13,2,3,'deee','2023-01-14 09:23:58','sadness','09:23:58'),(14,3,2,'odd','2023-01-14 09:27:15','shame','09:27:15'),(15,3,2,'odd','2023-01-14 11:55:15','shame','09:27:15'),(16,2,3,'fe','2023-01-14','No output','12:20:37'),(17,2,3,'fr','2023-01-14','No output','12:20:41');

/*Table structure for table `comment` */

DROP TABLE IF EXISTS `comment`;

CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `emotion` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `comment` */

insert  into `comment`(`comment_id`,`post_id`,`comment`,`emotion`) values (13,7,'pitty of you','shame'),(12,7,'ok','No output'),(11,7,'sanker','No output'),(10,6,'hi','No output'),(9,7,'happy to hear','joy'),(14,9,'poor','sadness'),(15,9,'bad person','sadness'),(16,9,'you cheat','shame'),(17,9,'good','joy'),(18,9,'dirty','shame'),(19,6,'hello','No output'),(20,6,'sad','sadness');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`complaint`,`reply`,`date`) values (1,1,'hi','das','2023-01-11'),(2,1,'hi','das','2023-01-11'),(3,1,'de','pending','2023-01-11');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'san','san','user'),(3,'kal','kal','user');

/*Table structure for table `post` */

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `path` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `post` */

insert  into `post`(`post_id`,`user_id`,`post`,`path`,`date`,`status`) values (8,1,'thursday','/static/uploads/620c3150-f14c-44da-ae73-ab0f306a85a9abc.jpg','2023-01-11','pending'),(6,1,'tuesday','/static/uploads/d98f9ffb-1fe7-41a6-baf8-1d1208f62473abc.jpg','2023-01-11','pending'),(7,1,'wednesday!','/static/uploads/16aa6339-3f79-43e3-8463-ab6c5392341eabc.jpg','2023-01-11','pending'),(5,1,'sunday','/static/uploads/d06a4c4c-4282-47a3-8b33-b7376cb42dc2abc.jpg','2023-01-11','pending'),(9,1,'friday','/static/uploads/6144d4c0-2a85-4939-92cd-8ce5e734935fabc.jpg','2023-01-11','pending'),(11,1,'saturday','/static/uploads/3e9ccdbc-62ee-4e3b-a824-b079f9859022abc.jpg','2023-01-11','pending');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values (1,2,'san','kar','alpy','6238526459','sankusanku001@gmail.com'),(2,3,'kal','lu','kottayam','6238526459','mickumicku00@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
