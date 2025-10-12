CREATE DATABASE  IF NOT EXISTS `cadastros` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `cadastros`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cadastros
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `cidade`
--

DROP TABLE IF EXISTS `cidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cidade` (
  `id_cidade` int(11) NOT NULL AUTO_INCREMENT,
  `nome_cidade` varchar(100) NOT NULL,
  `id_estado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_cidade`),
  KEY `id_estado` (`id_estado`),
  CONSTRAINT `cidade_ibfk_1` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidade`
--

LOCK TABLES `cidade` WRITE;
/*!40000 ALTER TABLE `cidade` DISABLE KEYS */;
INSERT INTO `cidade` VALUES (1,'São Paulo',1),(2,'Rio de Janeiro',2),(3,'Belo Horizonte',3),(4,'Salvador',4),(5,'Curitiba',5),(6,'Campinas',1),(7,'Niterói',2),(8,'Uberlândia',3),(9,'Feira de Santana',4),(10,'Londrina',5);
/*!40000 ALTER TABLE `cidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nome_cliente` varchar(100) NOT NULL,
  `email_cliente` varchar(100) DEFAULT NULL,
  `telefone_cliente` varchar(20) DEFAULT NULL,
  `id_cidade` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `id_cidade` (`id_cidade`),
  CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`id_cidade`) REFERENCES `cidade` (`id_cidade`)
) ENGINE=InnoDB AUTO_INCREMENT=501 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES
(1,'Cliente 1','cliente1@exemplo.com','6717737005',9),
(2,'Cliente 2','cliente2@exemplo.com','6719314092',2),
(3,'Cliente 3','cliente3@exemplo.com','6717334708',4),
(4,'Cliente 4','cliente4@exemplo.com','6715532625',8),
(5,'Cliente 5','cliente5@exemplo.com','6719107515',5),
(6,'Cliente 6','cliente6@exemplo.com','6713249173',4),
(7,'Cliente 7','cliente7@exemplo.com','6719766655',8),
(8,'Cliente 8','cliente8@exemplo.com','6716323903',1),
(9,'Cliente 9','cliente9@exemplo.com','6712254264',1),
(10,'Cliente 10','cliente10@exemplo.com','6715915894',8),
(11,'Cliente 11','cliente11@exemplo.com','6712113625',7),
(12,'Cliente 12','cliente12@exemplo.com','6716915825',5),
(13,'Cliente 13','cliente13@exemplo.com','6712378065',9),
(14,'Cliente 14','cliente14@exemplo.com','6712940810',1),
(15,'Cliente 15','cliente15@exemplo.com','6714472822',1),
(16,'Cliente 16','cliente16@exemplo.com','6718516326',2),
(17,'Cliente 17','cliente17@exemplo.com','6711554807',4),
(18,'Cliente 18','cliente18@exemplo.com','6712894405',4),
(19,'Cliente 19','cliente19@exemplo.com','6711000433',4),
(20,'Cliente 20','cliente20@exemplo.com','6712958589',6),
(21,'Cliente 21','cliente21@exemplo.com','6717209301',1),
(22,'Cliente 22','cliente22@exemplo.com','6710349423',1),
(23,'Cliente 23','cliente23@exemplo.com','6711755344',8),
(24,'Cliente 24','cliente24@exemplo.com','6710206729',10),
(25,'Cliente 25','cliente25@exemplo.com','6718129766',2),
(26,'Cliente 26','cliente26@exemplo.com','6712604999',9),
(27,'Cliente 27','cliente27@exemplo.com','6716327100',6),
(28,'Cliente 28','cliente28@exemplo.com','6716769915',9),
(29,'Cliente 29','cliente29@exemplo.com','6711684495',4),
(30,'Cliente 30','cliente30@exemplo.com','6711076179',6),
(31,'Cliente 31','cliente31@exemplo.com','6715286950',10),
(32,'Cliente 32','cliente32@exemplo.com','6710766439',6),
(33,'Cliente 33','cliente33@exemplo.com','6716979805',8),
(34,'Cliente 34','cliente34@exemplo.com','6715718350',7),
(35,'Cliente 35','cliente35@exemplo.com','6715830413',10),
(36,'Cliente 36','cliente36@exemplo.com','6719312702',9),
(37,'Cliente 37','cliente37@exemplo.com','6714467629',7),
(38,'Cliente 38','cliente38@exemplo.com','6711070638',5),
(39,'Cliente 39','cliente39@exemplo.com','6710133461',7),
(40,'Cliente 40','cliente40@exemplo.com','6712900023',5),
(41,'Cliente 41','cliente41@exemplo.com','6713899297',6),
(42,'Cliente 42','cliente42@exemplo.com','6717986438',3),
(43,'Cliente 43','cliente43@exemplo.com','6716648651',7),
(44,'Cliente 44','cliente44@exemplo.com','6714446432',2),
(45,'Cliente 45','cliente45@exemplo.com','6714644364',9),
(46,'Cliente 46','cliente46@exemplo.com','6718225038',6),
(47,'Cliente 47','cliente47@exemplo.com','6714476458',5),
(48,'Cliente 48','cliente48@exemplo.com','6711027367',1),
(49,'Cliente 49','cliente49@exemplo.com','6719231858',5),
(50,'Cliente 50','cliente50@exemplo.com','6716158997',7),
(51,'Cliente 51','cliente51@exemplo.com','6713934228',1),
(52,'Cliente 52','cliente52@exemplo.com','6719319364',6),
(53,'Cliente 53','cliente53@exemplo.com','6711659869',1),
(54,'Cliente 54','cliente54@exemplo.com','6717663241',7),
(55,'Cliente 55','cliente55@exemplo.com','6710662765',4),
(56,'Cliente 56','cliente56@exemplo.com','6713623382',9),
(57,'Cliente 57','cliente57@exemplo.com','6712879371',9),
(58,'Cliente 58','cliente58@exemplo.com','6712097613',7),
(59,'Cliente 59','cliente59@exemplo.com','6713940328',2),
(60,'Cliente 60','cliente60@exemplo.com','6715987709',6),(61,'Cliente 61','cliente61@exemplo.com','6718303528',6),(62,'Cliente 62','cliente62@exemplo.com','6713877662',3),(63,'Cliente 63','cliente63@exemplo.com','6718943832',9),(64,'Cliente 64','cliente64@exemplo.com','6715033848',1),(65,'Cliente 65','cliente65@exemplo.com','6715148644',6),(66,'Cliente 66','cliente66@exemplo.com','6712519610',6),(67,'Cliente 67','cliente67@exemplo.com','6711534800',1),(68,'Cliente 68','cliente68@exemplo.com','6716484719',2),(69,'Cliente 69','cliente69@exemplo.com','6719396465',2),(70,'Cliente 70','cliente70@exemplo.com','6710170364',6),(71,'Cliente 71','cliente71@exemplo.com','6718668734',6),(72,'Cliente 72','cliente72@exemplo.com','6713172680',9),(73,'Cliente 73','cliente73@exemplo.com','6712262326',7),(74,'Cliente 74','cliente74@exemplo.com','6714430076',4),(75,'Cliente 75','cliente75@exemplo.com','6713810516',9),(76,'Cliente 76','cliente76@exemplo.com','6712529122',7),(77,'Cliente 77','cliente77@exemplo.com','6713758682',10),(78,'Cliente 78','cliente78@exemplo.com','6718652872',4),(79,'Cliente 79','cliente79@exemplo.com','6710576438',3),(80,'Cliente 80','cliente80@exemplo.com','6713076472',7),(81,'Cliente 81','cliente81@exemplo.com','6713265044',7),(82,'Cliente 82','cliente82@exemplo.com','6714347600',2),(83,'Cliente 83','cliente83@exemplo.com','6713219004',3),(84,'Cliente 84','cliente84@exemplo.com','6712032687',4),(85,'Cliente 85','cliente85@exemplo.com','6719650032',9),(86,'Cliente 86','cliente86@exemplo.com','6715056431',9),(87,'Cliente 87','cliente87@exemplo.com','6719221913',10),(88,'Cliente 88','cliente88@exemplo.com','6719708464',1),(89,'Cliente 89','cliente89@exemplo.com','6711463612',7),(90,'Cliente 90','cliente90@exemplo.com','6710432461',2),(91,'Cliente 91','cliente91@exemplo.com','6715044266',2),(92,'Cliente 92','cliente92@exemplo.com','6711948901',6),(93,'Cliente 93','cliente93@exemplo.com','6711630743',2),(94,'Cliente 94','cliente94@exemplo.com','6713444009',3),(95,'Cliente 95','cliente95@exemplo.com','6710759498',8),(96,'Cliente 96','cliente96@exemplo.com','6713434384',6),(97,'Cliente 97','cliente97@exemplo.com','6718417829',5),(98,'Cliente 98','cliente98@exemplo.com','6719029290',1),(99,'Cliente 99','cliente99@exemplo.com','6715796068',8),(100,'Cliente 100','cliente100@exemplo.com','6718861682',3),(101,'Cliente 101','cliente101@exemplo.com','6716207353',4),(102,'Cliente 102','cliente102@exemplo.com','6718184586',1),(103,'Cliente 103','cliente103@exemplo.com','6719640954',6),(104,'Cliente 104','cliente104@exemplo.com','6719516856',1),(105,'Cliente 105','cliente105@exemplo.com','6714051685',9),(106,'Cliente 106','cliente106@exemplo.com','6711330314',1),(107,'Cliente 107','cliente107@exemplo.com','6718810816',3),(108,'Cliente 108','cliente108@exemplo.com','6715432680',1),(109,'Cliente 109','cliente109@exemplo.com','6713923580',10),(110,'Cliente 110','cliente110@exemplo.com','6715653918',10),(111,'Cliente 111','cliente111@exemplo.com','6712112228',2),(112,'Cliente 112','cliente112@exemplo.com','6719247085',3),(113,'Cliente 113','cliente113@exemplo.com','6716684560',5),(114,'Cliente 114','cliente114@exemplo.com','6713782881',5),(115,'Cliente 115','cliente115@exemplo.com','6711713702',5),(116,'Cliente 116','cliente116@exemplo.com','6718514421',9),(117,'Cliente 117','cliente117@exemplo.com','6716350686',7),(118,'Cliente 118','cliente118@exemplo.com','6714033253',1),(119,'Cliente 119','cliente119@exemplo.com','6719475643',7),(120,'Cliente 120','cliente120@exemplo.com','6713737944',10),(121,'Cliente 121','cliente121@exemplo.com','6715740162',1),(122,'Cliente 122','cliente122@exemplo.com','6715421593',6),(123,'Cliente 123','cliente123@exemplo.com','6711348820',1),(124,'Cliente 124','cliente124@exemplo.com','6716833248',4),(125,'Cliente 125','cliente125@exemplo.com','6717692345',8),(126,'Cliente 126','cliente126@exemplo.com','6714655333',1),(127,'Cliente 127','cliente127@exemplo.com','6719220228',5),(128,'Cliente 128','cliente128@exemplo.com','6713286349',4),(129,'Cliente 129','cliente129@exemplo.com','6719458576',6),(130,'Cliente 130','cliente130@exemplo.com','6710135808',4),(131,'Cliente 131','cliente131@exemplo.com','6717453170',7),(132,'Cliente 132','cliente132@exemplo.com','6710387964',3),(133,'Cliente 133','cliente133@exemplo.com','6710292795',5),(134,'Cliente 134','cliente134@exemplo.com','6712071435',7),(135,'Cliente 135','cliente135@exemplo.com','6716722115',4),(136,'Cliente 136','cliente136@exemplo.com','6719077281',4),(137,'Cliente 137','cliente137@exemplo.com','6711969313',9),(138,'Cliente 138','cliente138@exemplo.com','6715721421',4),(139,'Cliente 139','cliente139@exemplo.com','6710983188',5),(140,'Cliente 140','cliente140@exemplo.com','6717187783',4),(141,'Cliente 141','cliente141@exemplo.com','6717719198',8),(142,'Cliente 142','cliente142@exemplo.com','6711974718',9),(143,'Cliente 143','cliente143@exemplo.com','6718046877',4),(144,'Cliente 144','cliente144@exemplo.com','6715118195',5),(145,'Cliente 145','cliente145@exemplo.com','6714823832',3),(146,'Cliente 146','cliente146@exemplo.com','6715589062',2),(147,'Cliente 147','cliente147@exemplo.com','6712777700',9),(148,'Cliente 148','cliente148@exemplo.com','6712474741',8),(149,'Cliente 149','cliente149@exemplo.com','6712020791',7),(150,'Cliente 150','cliente150@exemplo.com','6716122361',2),(151,'Cliente 151','cliente151@exemplo.com','6718137749',7),(152,'Cliente 152','cliente152@exemplo.com','6719515990',8),(153,'Cliente 153','cliente153@exemplo.com','6717564072',7),(154,'Cliente 154','cliente154@exemplo.com','6718073471',2),(155,'Cliente 155','cliente155@exemplo.com','6715319303',1),(156,'Cliente 156','cliente156@exemplo.com','6718405519',10),(157,'Cliente 157','cliente157@exemplo.com','6711831137',1),(158,'Cliente 158','cliente158@exemplo.com','6719141937',3),(159,'Cliente 159','cliente159@exemplo.com','6717216578',8),(160,'Cliente 160','cliente160@exemplo.com','6714837559',3),(161,'Cliente 161','cliente161@exemplo.com','6716964429',8),(162,'Cliente 162','cliente162@exemplo.com','6718786129',1),(163,'Cliente 163','cliente163@exemplo.com','6714256587',1),(164,'Cliente 164','cliente164@exemplo.com','6711800001',7),(165,'Cliente 165','cliente165@exemplo.com','6715890741',1),(166,'Cliente 166','cliente166@exemplo.com','6715724082',7),(167,'Cliente 167','cliente167@exemplo.com','6715740887',9),(168,'Cliente 168','cliente168@exemplo.com','6717560127',1),(169,'Cliente 169','cliente169@exemplo.com','6711974435',8),(170,'Cliente 170','cliente170@exemplo.com','6719473134',7),(171,'Cliente 171','cliente171@exemplo.com','6712219628',3),(172,'Cliente 172','cliente172@exemplo.com','6716914734',7),(173,'Cliente 173','cliente173@exemplo.com','6711403300',8),(174,'Cliente 174','cliente174@exemplo.com','6714430109',9),(175,'Cliente 175','cliente175@exemplo.com','6711542377',1),(176,'Cliente 176','cliente176@exemplo.com','6719434190',5),(177,'Cliente 177','cliente177@exemplo.com','6715368220',3),(178,'Cliente 178','cliente178@exemplo.com','6717088471',8),(179,'Cliente 179','cliente179@exemplo.com','6716366985',10),(180,'Cliente 180','cliente180@exemplo.com','6717176483',9),(181,'Cliente 181','cliente181@exemplo.com','6719050322',1),(182,'Cliente 182','cliente182@exemplo.com','6717367769',5),(183,'Cliente 183','cliente183@exemplo.com','6718534721',1),(184,'Cliente 184','cliente184@exemplo.com','6715849791',9),(185,'Cliente 185','cliente185@exemplo.com','6714333541',7),(186,'Cliente 186','cliente186@exemplo.com','6719689167',9),(187,'Cliente 187','cliente187@exemplo.com','6715092307',9),(188,'Cliente 188','cliente188@exemplo.com','6719551336',1),(189,'Cliente 189','cliente189@exemplo.com','6715644626',6),(190,'Cliente 190','cliente190@exemplo.com','6711285878',10),(191,'Cliente 191','cliente191@exemplo.com','6713630051',10),(192,'Cliente 192','cliente192@exemplo.com','6717398086',9),(193,'Cliente 193','cliente193@exemplo.com','6717893175',6),(194,'Cliente 194','cliente194@exemplo.com','6713387564',1),(195,'Cliente 195','cliente195@exemplo.com','6713325138',5),(196,'Cliente 196','cliente196@exemplo.com','6712689551',10),(197,'Cliente 197','cliente197@exemplo.com','6711175230',7),(198,'Cliente 198','cliente198@exemplo.com','6718123413',2),(199,'Cliente 199','cliente199@exemplo.com','6713767786',4),(200,'Cliente 200','cliente200@exemplo.com','6718477221',1),(201,'Cliente 201','cliente201@exemplo.com','6717157143',5),(202,'Cliente 202','cliente202@exemplo.com','6719690727',6),(203,'Cliente 203','cliente203@exemplo.com','6719709535',2),(204,'Cliente 204','cliente204@exemplo.com','6717264630',3),(205,'Cliente 205','cliente205@exemplo.com','6710642170',6),(206,'Cliente 206','cliente206@exemplo.com','6716819572',7),(207,'Cliente 207','cliente207@exemplo.com','6713792346',9),(208,'Cliente 208','cliente208@exemplo.com','6710678433',9),(209,'Cliente 209','cliente209@exemplo.com','6718759113',10),(210,'Cliente 210','cliente210@exemplo.com','6710317269',4),(211,'Cliente 211','cliente211@exemplo.com','6717196103',6),(212,'Cliente 212','cliente212@exemplo.com','6713870535',5),(213,'Cliente 213','cliente213@exemplo.com','6718775245',2),(214,'Cliente 214','cliente214@exemplo.com','6711894846',5),(215,'Cliente 215','cliente215@exemplo.com','6717024885',2),(216,'Cliente 216','cliente216@exemplo.com','6716419209',8),(217,'Cliente 217','cliente217@exemplo.com','6718741009',1),(218,'Cliente 218','cliente218@exemplo.com','6718306306',9),(219,'Cliente 219','cliente219@exemplo.com','6719150736',10),(220,'Cliente 220','cliente220@exemplo.com','6719107240',8),(221,'Cliente 221','cliente221@exemplo.com','6710680937',1),(222,'Cliente 222','cliente222@exemplo.com','6710972658',4),(223,'Cliente 223','cliente223@exemplo.com','6712352074',3),(224,'Cliente 224','cliente224@exemplo.com','6715935495',2),(225,'Cliente 225','cliente225@exemplo.com','6711605742',3),(226,'Cliente 226','cliente226@exemplo.com','6717089658',9),(227,'Cliente 227','cliente227@exemplo.com','6710251821',7),(228,'Cliente 228','cliente228@exemplo.com','6710977697',6),(229,'Cliente 229','cliente229@exemplo.com','6716309849',5),(230,'Cliente 230','cliente230@exemplo.com','6711087860',4),(231,'Cliente 231','cliente231@exemplo.com','6713880720',10),(232,'Cliente 232','cliente232@exemplo.com','6713942940',3),(233,'Cliente 233','cliente233@exemplo.com','6719989390',3),(234,'Cliente 234','cliente234@exemplo.com','6714311953',3),(235,'Cliente 235','cliente235@exemplo.com','6712022600',2),(236,'Cliente 236','cliente236@exemplo.com','6719621835',5),(237,'Cliente 237','cliente237@exemplo.com','6714611477',9),(238,'Cliente 238','cliente238@exemplo.com','6711021547',9),(239,'Cliente 239','cliente239@exemplo.com','6717906117',5),(240,'Cliente 240','cliente240@exemplo.com','6711022312',1),(241,'Cliente 241','cliente241@exemplo.com','6718268885',1),(242,'Cliente 242','cliente242@exemplo.com','6717908003',8),(243,'Cliente 243','cliente243@exemplo.com','6715832098',6),(244,'Cliente 244','cliente244@exemplo.com','6719637843',2),(245,'Cliente 245','cliente245@exemplo.com','6710630146',8),(246,'Cliente 246','cliente246@exemplo.com','6715232185',4),(247,'Cliente 247','cliente247@exemplo.com','6713740204',8),(248,'Cliente 248','cliente248@exemplo.com','6713974223',9),(249,'Cliente 249','cliente249@exemplo.com','6711848406',3),(250,'Cliente 250','cliente250@exemplo.com','6719351723',8),(251,'Cliente 251','cliente251@exemplo.com','6711047077',2),(252,'Cliente 252','cliente252@exemplo.com','6715728974',4),(253,'Cliente 253','cliente253@exemplo.com','6719426821',8),(254,'Cliente 254','cliente254@exemplo.com','6717548832',7),(255,'Cliente 255','cliente255@exemplo.com','6718586436',5),(256,'Cliente 256','cliente256@exemplo.com','6715202809',4),(257,'Cliente 257','cliente257@exemplo.com','6711575447',8),(258,'Cliente 258','cliente258@exemplo.com','6713108221',3),(259,'Cliente 259','cliente259@exemplo.com','6714877190',6),(260,'Cliente 260','cliente260@exemplo.com','6714692622',6),(261,'Cliente 261','cliente261@exemplo.com','6715265117',9),(262,'Cliente 262','cliente262@exemplo.com','6717803630',3),(263,'Cliente 263','cliente263@exemplo.com','6710882928',6),(264,'Cliente 264','cliente264@exemplo.com','6716542976',6),(265,'Cliente 265','cliente265@exemplo.com','6716370188',7),(266,'Cliente 266','cliente266@exemplo.com','6712146793',2),(267,'Cliente 267','cliente267@exemplo.com','6713457384',2),(268,'Cliente 268','cliente268@exemplo.com','6716369163',8),(269,'Cliente 269','cliente269@exemplo.com','6719897648',7),(270,'Cliente 270','cliente270@exemplo.com','6710732861',6),(271,'Cliente 271','cliente271@exemplo.com','6714845537',9),(272,'Cliente 272','cliente272@exemplo.com','6715469452',4),(273,'Cliente 273','cliente273@exemplo.com','6710309767',2),(274,'Cliente 274','cliente274@exemplo.com','6716660515',9),(275,'Cliente 275','cliente275@exemplo.com','6713761878',3),(276,'Cliente 276','cliente276@exemplo.com','6711531068',10),(277,'Cliente 277','cliente277@exemplo.com','6715233384',7),(278,'Cliente 278','cliente278@exemplo.com','6715654702',10),(279,'Cliente 279','cliente279@exemplo.com','6710338887',4),(280,'Cliente 280','cliente280@exemplo.com','6715546545',8),(281,'Cliente 281','cliente281@exemplo.com','6712334373',9),(282,'Cliente 282','cliente282@exemplo.com','6714434191',8),(283,'Cliente 283','cliente283@exemplo.com','6713240278',5),(284,'Cliente 284','cliente284@exemplo.com','6711657573',6),(285,'Cliente 285','cliente285@exemplo.com','6712331382',6),(286,'Cliente 286','cliente286@exemplo.com','6719378115',2),(287,'Cliente 287','cliente287@exemplo.com','6717201758',3),(288,'Cliente 288','cliente288@exemplo.com','6712430378',4),(289,'Cliente 289','cliente289@exemplo.com','6711361357',6),(290,'Cliente 290','cliente290@exemplo.com','6713992393',4),(291,'Cliente 291','cliente291@exemplo.com','6713603257',9),(292,'Cliente 292','cliente292@exemplo.com','6712530352',7),(293,'Cliente 293','cliente293@exemplo.com','6715647378',9),(294,'Cliente 294','cliente294@exemplo.com','6714527017',8),(295,'Cliente 295','cliente295@exemplo.com','6715186930',3),(296,'Cliente 296','cliente296@exemplo.com','6717808520',2),(297,'Cliente 297','cliente297@exemplo.com','6711679528',6),(298,'Cliente 298','cliente298@exemplo.com','6711634347',3),(299,'Cliente 299','cliente299@exemplo.com','6715936854',4),(300,'Cliente 300','cliente300@exemplo.com','6718091108',1),(301,'Cliente 301','cliente301@exemplo.com','6710299377',9),(302,'Cliente 302','cliente302@exemplo.com','6712868195',9),(303,'Cliente 303','cliente303@exemplo.com','6711801311',5),(304,'Cliente 304','cliente304@exemplo.com','6718411164',8),(305,'Cliente 305','cliente305@exemplo.com','6713600327',5),(306,'Cliente 306','cliente306@exemplo.com','6712705739',10),(307,'Cliente 307','cliente307@exemplo.com','6719006104',7),(308,'Cliente 308','cliente308@exemplo.com','6716764328',4),(309,'Cliente 309','cliente309@exemplo.com','6717467312',7),(310,'Cliente 310','cliente310@exemplo.com','6710999982',5),(311,'Cliente 311','cliente311@exemplo.com','6711793857',5),(312,'Cliente 312','cliente312@exemplo.com','6715083451',4),(313,'Cliente 313','cliente313@exemplo.com','6710440872',3),(314,'Cliente 314','cliente314@exemplo.com','6712625519',5),(315,'Cliente 315','cliente315@exemplo.com','6715917019',6),(316,'Cliente 316','cliente316@exemplo.com','6718793702',9),(317,'Cliente 317','cliente317@exemplo.com','6713827179',6),(318,'Cliente 318','cliente318@exemplo.com','6713573090',3),(319,'Cliente 319','cliente319@exemplo.com','6713444108',9),(320,'Cliente 320','cliente320@exemplo.com','6713280247',1),(321,'Cliente 321','cliente321@exemplo.com','6711327721',6),(322,'Cliente 322','cliente322@exemplo.com','6715704490',1),(323,'Cliente 323','cliente323@exemplo.com','6716435820',1),(324,'Cliente 324','cliente324@exemplo.com','6710940182',5),(325,'Cliente 325','cliente325@exemplo.com','6719941085',7),(326,'Cliente 326','cliente326@exemplo.com','6710418979',4),(327,'Cliente 327','cliente327@exemplo.com','6718490841',1),(328,'Cliente 328','cliente328@exemplo.com','6717555181',6),(329,'Cliente 329','cliente329@exemplo.com','6717130882',8),(330,'Cliente 330','cliente330@exemplo.com','6717490130',5),(331,'Cliente 331','cliente331@exemplo.com','6718134550',9),(332,'Cliente 332','cliente332@exemplo.com','6717145276',1),(333,'Cliente 333','cliente333@exemplo.com','6712549305',1),(334,'Cliente 334','cliente334@exemplo.com','6714129315',10),(335,'Cliente 335','cliente335@exemplo.com','6715513246',9),(336,'Cliente 336','cliente336@exemplo.com','6717587853',2),(337,'Cliente 337','cliente337@exemplo.com','6714549997',9),(338,'Cliente 338','cliente338@exemplo.com','6718159282',6),(339,'Cliente 339','cliente339@exemplo.com','6714076395',4),(340,'Cliente 340','cliente340@exemplo.com','6714017970',1),(341,'Cliente 341','cliente341@exemplo.com','6719653889',8),(342,'Cliente 342','cliente342@exemplo.com','6717262164',5),(343,'Cliente 343','cliente343@exemplo.com','6711096126',2),(344,'Cliente 344','cliente344@exemplo.com','6715466923',3),(345,'Cliente 345','cliente345@exemplo.com','6714006416',4),(346,'Cliente 346','cliente346@exemplo.com','6716919599',4),(347,'Cliente 347','cliente347@exemplo.com','6715414654',8),(348,'Cliente 348','cliente348@exemplo.com','6710602044',1),(349,'Cliente 349','cliente349@exemplo.com','6712706957',1),(350,'Cliente 350','cliente350@exemplo.com','6716013790',8),(351,'Cliente 351','cliente351@exemplo.com','6719899413',7),(352,'Cliente 352','cliente352@exemplo.com','6713964748',10),(353,'Cliente 353','cliente353@exemplo.com','6716235505',3),(354,'Cliente 354','cliente354@exemplo.com','6712791872',8),(355,'Cliente 355','cliente355@exemplo.com','6716926025',4),(356,'Cliente 356','cliente356@exemplo.com','6716467630',2),(357,'Cliente 357','cliente357@exemplo.com','6710550759',7),(358,'Cliente 358','cliente358@exemplo.com','6712255765',1),(359,'Cliente 359','cliente359@exemplo.com','6717902703',7),(360,'Cliente 360','cliente360@exemplo.com','6719849486',10),(361,'Cliente 361','cliente361@exemplo.com','6716015912',3),(362,'Cliente 362','cliente362@exemplo.com','6715656967',1),(363,'Cliente 363','cliente363@exemplo.com','6713339163',7),(364,'Cliente 364','cliente364@exemplo.com','6712531414',4),(365,'Cliente 365','cliente365@exemplo.com','6718044395',1),(366,'Cliente 366','cliente366@exemplo.com','6710060794',8),(367,'Cliente 367','cliente367@exemplo.com','6718755529',1),(368,'Cliente 368','cliente368@exemplo.com','6715807920',8),(369,'Cliente 369','cliente369@exemplo.com','6711550719',5),(370,'Cliente 370','cliente370@exemplo.com','6717192392',3),(371,'Cliente 371','cliente371@exemplo.com','6712698989',5),(372,'Cliente 372','cliente372@exemplo.com','6716549267',8),(373,'Cliente 373','cliente373@exemplo.com','6710145171',7),(374,'Cliente 374','cliente374@exemplo.com','6713814859',9),(375,'Cliente 375','cliente375@exemplo.com','6711175782',1),(376,'Cliente 376','cliente376@exemplo.com','6718006132',10),(377,'Cliente 377','cliente377@exemplo.com','6711534483',1),(378,'Cliente 378','cliente378@exemplo.com','6717099996',5),(379,'Cliente 379','cliente379@exemplo.com','6711089589',3),(380,'Cliente 380','cliente380@exemplo.com','6716802237',8),(381,'Cliente 381','cliente381@exemplo.com','6719436199',4),(382,'Cliente 382','cliente382@exemplo.com','6718067653',1),(383,'Cliente 383','cliente383@exemplo.com','6718359628',1),(384,'Cliente 384','cliente384@exemplo.com','6716224054',1),(385,'Cliente 385','cliente385@exemplo.com','6713020392',5),(386,'Cliente 386','cliente386@exemplo.com','6711370969',5),(387,'Cliente 387','cliente387@exemplo.com','6718864890',1),(388,'Cliente 388','cliente388@exemplo.com','6716094200',9),(389,'Cliente 389','cliente389@exemplo.com','6716005802',4),(390,'Cliente 390','cliente390@exemplo.com','6719262438',6),(391,'Cliente 391','cliente391@exemplo.com','6711934114',2),(392,'Cliente 392','cliente392@exemplo.com','6713386235',2),(393,'Cliente 393','cliente393@exemplo.com','6716931438',1),(394,'Cliente 394','cliente394@exemplo.com','6711221222',5),(395,'Cliente 395','cliente395@exemplo.com','6710820277',10),(396,'Cliente 396','cliente396@exemplo.com','6714594270',5),(397,'Cliente 397','cliente397@exemplo.com','6719908651',6),(398,'Cliente 398','cliente398@exemplo.com','6716915949',9),(399,'Cliente 399','cliente399@exemplo.com','6712225178',6),(400,'Cliente 400','cliente400@exemplo.com','6710034850',5),(401,'Cliente 401','cliente401@exemplo.com','6710635560',1),(402,'Cliente 402','cliente402@exemplo.com','6711761988',7),(403,'Cliente 403','cliente403@exemplo.com','6717757750',9),(404,'Cliente 404','cliente404@exemplo.com','6711539353',1),(405,'Cliente 405','cliente405@exemplo.com','6719427976',5),(406,'Cliente 406','cliente406@exemplo.com','6715277363',3),(407,'Cliente 407','cliente407@exemplo.com','6715418132',1),(408,'Cliente 408','cliente408@exemplo.com','6715448247',7),(409,'Cliente 409','cliente409@exemplo.com','6714753511',6),(410,'Cliente 410','cliente410@exemplo.com','6711282486',2),(411,'Cliente 411','cliente411@exemplo.com','6711585639',5),(412,'Cliente 412','cliente412@exemplo.com','6718584768',9),(413,'Cliente 413','cliente413@exemplo.com','6718839862',8),(414,'Cliente 414','cliente414@exemplo.com','6710694464',2),(415,'Cliente 415','cliente415@exemplo.com','6713636063',5),(416,'Cliente 416','cliente416@exemplo.com','6712835030',10),(417,'Cliente 417','cliente417@exemplo.com','6711141020',6),(418,'Cliente 418','cliente418@exemplo.com','6716164107',4),(419,'Cliente 419','cliente419@exemplo.com','6716848865',6),(420,'Cliente 420','cliente420@exemplo.com','6714651479',9),(421,'Cliente 421','cliente421@exemplo.com','6716738314',10),(422,'Cliente 422','cliente422@exemplo.com','6716164667',3),(423,'Cliente 423','cliente423@exemplo.com','6716483845',4),(424,'Cliente 424','cliente424@exemplo.com','6717711066',9),(425,'Cliente 425','cliente425@exemplo.com','6718155651',7),(426,'Cliente 426','cliente426@exemplo.com','6715557790',10),(427,'Cliente 427','cliente427@exemplo.com','6712197161',2),(428,'Cliente 428','cliente428@exemplo.com','6711725962',4),(429,'Cliente 429','cliente429@exemplo.com','6713018835',5),(430,'Cliente 430','cliente430@exemplo.com','6711824205',7),(431,'Cliente 431','cliente431@exemplo.com','6717490389',8),(432,'Cliente 432','cliente432@exemplo.com','6715899562',7),(433,'Cliente 433','cliente433@exemplo.com','6714678173',4),(434,'Cliente 434','cliente434@exemplo.com','6715789237',8),(435,'Cliente 435','cliente435@exemplo.com','6717891963',9),(436,'Cliente 436','cliente436@exemplo.com','6717844174',5),(437,'Cliente 437','cliente437@exemplo.com','6718011640',8),(438,'Cliente 438','cliente438@exemplo.com','6711623607',7),(439,'Cliente 439','cliente439@exemplo.com','6718743786',4),(440,'Cliente 440','cliente440@exemplo.com','6711519481',7),(441,'Cliente 441','cliente441@exemplo.com','6710176064',1),(442,'Cliente 442','cliente442@exemplo.com','6719669900',9),(443,'Cliente 443','cliente443@exemplo.com','6712143524',7),(444,'Cliente 444','cliente444@exemplo.com','6713697875',1),(445,'Cliente 445','cliente445@exemplo.com','6710967914',4),(446,'Cliente 446','cliente446@exemplo.com','6715109490',5),(447,'Cliente 447','cliente447@exemplo.com','6718369098',8),(448,'Cliente 448','cliente448@exemplo.com','6713027461',3),(449,'Cliente 449','cliente449@exemplo.com','6712199879',5),(450,'Cliente 450','cliente450@exemplo.com','6714550562',1),(451,'Cliente 451','cliente451@exemplo.com','6716661771',4),(452,'Cliente 452','cliente452@exemplo.com','6715618593',9),(453,'Cliente 453','cliente453@exemplo.com','6716797332',8),(454,'Cliente 454','cliente454@exemplo.com','6718581981',10),(455,'Cliente 455','cliente455@exemplo.com','6711881660',1),(456,'Cliente 456','cliente456@exemplo.com','6718513714',1),(457,'Cliente 457','cliente457@exemplo.com','6714825644',4),(458,'Cliente 458','cliente458@exemplo.com','6715063816',4),(459,'Cliente 459','cliente459@exemplo.com','6712781709',4),(460,'Cliente 460','cliente460@exemplo.com','6717278145',8),(461,'Cliente 461','cliente461@exemplo.com','6713249371',6),(462,'Cliente 462','cliente462@exemplo.com','6716234761',6),(463,'Cliente 463','cliente463@exemplo.com','6719216121',10),(464,'Cliente 464','cliente464@exemplo.com','6718993463',7),(465,'Cliente 465','cliente465@exemplo.com','6717930720',9),(466,'Cliente 466','cliente466@exemplo.com','6719742517',3),(467,'Cliente 467','cliente467@exemplo.com','6713731357',1),(468,'Cliente 468','cliente468@exemplo.com','6713213127',4),(469,'Cliente 469','cliente469@exemplo.com','6717467204',8),(470,'Cliente 470','cliente470@exemplo.com','6712958752',4),(471,'Cliente 471','cliente471@exemplo.com','6719011457',5),(472,'Cliente 472','cliente472@exemplo.com','6714588915',10),(473,'Cliente 473','cliente473@exemplo.com','6716086274',1),(474,'Cliente 474','cliente474@exemplo.com','6714338989',1),(475,'Cliente 475','cliente475@exemplo.com','6717664325',8),(476,'Cliente 476','cliente476@exemplo.com','6716571276',10),(477,'Cliente 477','cliente477@exemplo.com','6715875331',3),(478,'Cliente 478','cliente478@exemplo.com','6712489815',7),(479,'Cliente 479','cliente479@exemplo.com','6714428512',4),(480,'Cliente 480','cliente480@exemplo.com','6711733402',10),(481,'Cliente 481','cliente481@exemplo.com','6713078035',7),(482,'Cliente 482','cliente482@exemplo.com','6712882048',6),(483,'Cliente 483','cliente483@exemplo.com','6717056602',10),(484,'Cliente 484','cliente484@exemplo.com','6718137015',2),(485,'Cliente 485','cliente485@exemplo.com','6711093870',3),(486,'Cliente 486','cliente486@exemplo.com','6717550407',2),(487,'Cliente 487','cliente487@exemplo.com','6713612917',5),(488,'Cliente 488','cliente488@exemplo.com','6710691763',1),(489,'Cliente 489','cliente489@exemplo.com','6710627246',2),(490,'Cliente 490','cliente490@exemplo.com','6715691809',4),(491,'Cliente 491','cliente491@exemplo.com','6712499171',1),(492,'Cliente 492','cliente492@exemplo.com','6716257975',10),(493,'Cliente 493','cliente493@exemplo.com','6716408996',5),(494,'Cliente 494','cliente494@exemplo.com','6715449164',3),(495,'Cliente 495','cliente495@exemplo.com','6715853146',2),(496,'Cliente 496','cliente496@exemplo.com','6712167313',6),(497,'Cliente 497','cliente497@exemplo.com','6718500646',8),(498,'Cliente 498','cliente498@exemplo.com','6712006467',8),(499,'Cliente 499','cliente499@exemplo.com','6711617067',6),(500,'Cliente 500','cliente500@exemplo.com','6712666078',7);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado`
--

DROP TABLE IF EXISTS `estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado` (
  `id_estado` int(11) NOT NULL AUTO_INCREMENT,
  `nome_estado` varchar(100) NOT NULL,
  `sigla_estado` char(2) NOT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado`
--

LOCK TABLES `estado` WRITE;
/*!40000 ALTER TABLE `estado` DISABLE KEYS */;
INSERT INTO `estado` VALUES (1,'São Paulo','SP'),(2,'Rio de Janeiro','RJ'),(3,'Minas Gerais','MG'),(4,'Bahia','BA'),(5,'Paraná','PR');
/*!40000 ALTER TABLE `estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'cadastros'
--

--
-- Dumping routines for database 'cadastros'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

update cliente set telefone_cliente=(insert(telefone_cliente, 3, 0, "9"));

select * from cidade;
select * from estado;

update cidade set id_estado=2 where nome_cidade = 'Curitiba';


update cliente set email_cliente=(replace(email_cliente, 'exemplo.com', 'teste.com')) where id_cliente between 20 and 45;

select * from cliente;



