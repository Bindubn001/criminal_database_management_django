DROP DATABASE IF EXISTS `dbcriminal`;
CREATE DATABASE `dbcriminal` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dbcriminal`;
SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;
SET FOREIGN_KEY_CHECKS=0;


CREATE TABLE CRIME
(
crime_id INT(4) NOT NULL,
crime_date DATE NOT NULL,
crime_type VARCHAR(30) NOT NULL,
crime_level VARCHAR(30) NOT NULL,  
location VARCHAR(30) NOT NULL,
punishment VARCHAR(30),
PRIMARY KEY (crime_id)
);

CREATE TABLE PRISON
(
prison_id INT(4) NOT NULL,
prison_name VARCHAR(30) NOT NULL,
city VARCHAR(30) NOT NULL,
prison_level VARCHAR(30) NOT NULL,  
PRIMARY KEY (prison_id)
);

CREATE TABLE CRIMINAL
(
criminal_id INT(4) NOT NULL,
cname VARCHAR(30) NOT NULL,
birthdate DATE NOT NULL,
address VARCHAR(30) NOT NULL,  
dependent_name VARCHAR(30),
crime_id INT(4) NOT NULL,
prison_id INT(4) NOT NULL,  
prison_term INT(2),  
PRIMARY KEY (criminal_id),
FOREIGN KEY (prison_id) REFERENCES PRISON(prison_id) ON DELETE CASCADE
);

CREATE TABLE VICTIM
(
victim_id INT(4) NOT NULL,  
vname VARCHAR(30) NOT NULL,
age INT(3) NOT NULL,
address VARCHAR(30) NOT NULL,
phone VARCHAR(10),
crime_id INT(4) NOT NULL,
PRIMARY KEY (victim_id),
FOREIGN KEY (crime_id) REFERENCES CRIME(crime_id) ON DELETE CASCADE
);

CREATE TABLE TRIAL
(
case_id INT(4) NOT NULL,
evidence VARCHAR(30) NOT NULL,
section_of_law VARCHAR(10) NOT NULL,
case_status VARCHAR(30) NOT NULL,
lawyer_id INT(4),
criminal_id INT(4) NOT NULL,
victim_id INT(4) NOT NULL,  
crime_id INT(4) NOT NULL,
PRIMARY KEY (case_id),
CONSTRAINT tfk1 FOREIGN KEY(criminal_id) REFERENCES CRIMINAL(criminal_id) ON DELETE CASCADE,
CONSTRAINT tfk2 FOREIGN KEY(victim_id) REFERENCES VICTIM(victim_id) ON DELETE CASCADE,
CONSTRAINT tfk3 FOREIGN KEY(crime_id) REFERENCES CRIME(crime_id) ON DELETE CASCADE
);

DESC `crime`;
DESC `prison`;
DESC `criminal`;
DESC `victim`;
DESC `trial`;

INSERT INTO `crime` VALUES(101,'2018-08-25','Murder','Felony','Phoenix','Prison term');
INSERT INTO `crime` VALUES(102,'2000-06-21','Murder','Felony','California','Execution');
INSERT INTO `crime` VALUES(103,'1916-05-08','Murder','Felony','Connecticut','Execution');
INSERT INTO `crime` VALUES(104,'1916-05-08','Rape','Second degree','Execution','Mysore');
INSERT INTO `crime` VALUES(105,'1916-05-08','Burglary','Third degree','Prison term','Uttar Pradesh');

INSERT INTO `prison` VALUES(5001,'Arizona State Prison Complex','Arizona','State');
INSERT INTO `prison` VALUES(5002,'Central Jail','San Leonardo','Central');
INSERT INTO `prison` VALUES(5003,'Bangalore Central Prison','Bangalore','Taluk');
INSERT INTO `prison` VALUES(5004,'Mysore Prison','Mysore','Taluk');
INSERT INTO `prison` VALUES(5005,'West Bengal Prison','Uttar Pradesh','State');

INSERT INTO `criminal` VALUES(2001,'Sammantha Allen','1988-06-14','Phoenix','Cynthia Stolzmann',101,5001,24);
INSERT INTO `criminal` VALUES(2002,'Stuart Alexander','1961-03-22','San Leandro','Shirley Eckhart',102,5002,4);
INSERT INTO `criminal` VALUES(2003,'Amy Archer-Gilligan','1982-10-31','Bangalore','Mary J Archer',103,5003,5);
INSERT INTO `criminal` VALUES(2004,'Zaid Shah','1992-11-11','Mysore','Ali Shah',104,5004,null);
INSERT INTO `criminal` VALUES(2005,'Sammer Naik','1989-04-19','Uttar Pradesh','Kiran Naik',105,5005,null);

INSERT INTO `victim` VALUES(3001,'Ame Lynn Deal',10,'Phoenix','5733035360',101);
INSERT INTO `victim` VALUES(3002,'William Shaline',57,'California','4124573399',102);
INSERT INTO `victim` VALUES(3003,'Amy Hosmer',30,'Connecticut','2483412949',103);
INSERT INTO `victim` VALUES(3004,'Maya Seth',37,'West Bengal','9926362718',104);
INSERT INTO `victim` VALUES(3005,'Lohith Joseph',48,'Mysore','8642617822',105);

INSERT INTO `trial` VALUES(4001,'Cadaver','1111','Solved',111,2001,3001,101);
INSERT INTO `trial` VALUES(4002,'Axe','1111','Solved',222,2002,3002,102);
INSERT INTO `trial` VALUES(4003,'Blood sample','1112','Ongoing',111,2003,3003,103);
INSERT INTO `trial` VALUES(4004,'Body','1178','Ongoing',444,2004,3004,104);
INSERT INTO `trial` VALUES(4005,'House','1154','Ongoing',555,2005,3005,105);

