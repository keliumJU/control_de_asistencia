-- MariaDB dump 10.18  Distrib 10.4.17-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: parcial2
-- ------------------------------------------------------
-- Server version	10.4.17-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asistencia`
--

DROP TABLE IF EXISTS `asistencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistencia` (
  `identificacion` varchar(10) DEFAULT NULL,
  `sesion_id` int(11) DEFAULT NULL,
  KEY `identificacion` (`identificacion`),
  KEY `sesion_id` (`sesion_id`),
  CONSTRAINT `asistencia_ibfk_1` FOREIGN KEY (`identificacion`) REFERENCES `estudiantes` (`identificacion`),
  CONSTRAINT `asistencia_ibfk_2` FOREIGN KEY (`sesion_id`) REFERENCES `sesiones` (`sesion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia`
--

LOCK TABLES `asistencia` WRITE;
/*!40000 ALTER TABLE `asistencia` DISABLE KEYS */;
INSERT INTO `asistencia` VALUES ('1234',1),('1111',1),('1234',1),('1111',1),('1234',1),('1111',1),('1234',1),('1111',1),('1007403404',1),('1111',1),('1007403404',1),('1111',1),('1007403404',1),('1007403404',1),('1007403404',1),('1007403404',1),('1007403404',1),('1111',1),('1007403404',1),('1111',1),('1007403404',1),('1007403404',1),('1007403404',1),('1007403404',1),('1007403404',1),('1234',2),('1234',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1111',4),('1007403404',1),('1111',4),('1111',4),('1111',4),('1007403404',5),('1234',4),('1007403404',4),('1111',4);
/*!40000 ALTER TABLE `asistencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `espacios_academicos`
--

DROP TABLE IF EXISTS `espacios_academicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `espacios_academicos` (
  `espacio_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `semestre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`espacio_id`),
  KEY `semestre_id` (`semestre_id`),
  CONSTRAINT `espacios_academicos_ibfk_1` FOREIGN KEY (`semestre_id`) REFERENCES `semestres` (`semestre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `espacios_academicos`
--

LOCK TABLES `espacios_academicos` WRITE;
/*!40000 ALTER TABLE `espacios_academicos` DISABLE KEYS */;
INSERT INTO `espacios_academicos` VALUES (1,'math',1),(2,'algebra I',2),(3,'Algorithms',1),(4,'IA',10);
/*!40000 ALTER TABLE `espacios_academicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `espacios_academicos_estudiante`
--

DROP TABLE IF EXISTS `espacios_academicos_estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `espacios_academicos_estudiante` (
  `identificacion` varchar(10) DEFAULT NULL,
  `id_espacio` int(11) DEFAULT NULL,
  KEY `identificacion` (`identificacion`),
  KEY `id_espacio` (`id_espacio`),
  CONSTRAINT `espacios_academicos_estudiante_ibfk_1` FOREIGN KEY (`identificacion`) REFERENCES `estudiantes` (`identificacion`),
  CONSTRAINT `espacios_academicos_estudiante_ibfk_2` FOREIGN KEY (`id_espacio`) REFERENCES `espacios_academicos` (`espacio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `espacios_academicos_estudiante`
--

LOCK TABLES `espacios_academicos_estudiante` WRITE;
/*!40000 ALTER TABLE `espacios_academicos_estudiante` DISABLE KEYS */;
INSERT INTO `espacios_academicos_estudiante` VALUES ('1007403404',1),('1007403404',2),('1007403404',3),('1111',1),('1111',3),('1234',1),('1111',2),('1234',2),('1007403404',3),('1111',3),('1234',3),('1007403404',4),('1111',4),('1234',4);
/*!40000 ALTER TABLE `espacios_academicos_estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiantes`
--

DROP TABLE IF EXISTS `estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estudiantes` (
  `identificacion` varchar(10) NOT NULL,
  `nombres` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `celular` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  PRIMARY KEY (`identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiantes`
--

LOCK TABLES `estudiantes` WRITE;
/*!40000 ALTER TABLE `estudiantes` DISABLE KEYS */;
INSERT INTO `estudiantes` VALUES ('1007403404','Kelium','Jean','3203719763','juan@gmail.com'),('1111','federico','perez','3213','fepe@gamil.com'),('1234','rual','rodriguez','321','raul@gmail.com');
/*!40000 ALTER TABLE `estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semestres`
--

DROP TABLE IF EXISTS `semestres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `semestres` (
  `semestre_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) NOT NULL,
  PRIMARY KEY (`semestre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semestres`
--

LOCK TABLES `semestres` WRITE;
/*!40000 ALTER TABLE `semestres` DISABLE KEYS */;
INSERT INTO `semestres` VALUES (1,'Semestre 1'),(2,'Semestre 2'),(3,'Semestre 3'),(4,'Semestre 4'),(5,'Semestre 5'),(6,'Semestre 6'),(7,'Semestre 7'),(8,'Semestre 8'),(9,'Semestre 9'),(10,'Semestre 10');
/*!40000 ALTER TABLE `semestres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sesiones`
--

DROP TABLE IF EXISTS `sesiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sesiones` (
  `sesion_id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `hora_ini` time NOT NULL,
  `hora_fin` time NOT NULL,
  `espacio_academico_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sesion_id`),
  KEY `espacio_academico_id` (`espacio_academico_id`),
  CONSTRAINT `sesiones_ibfk_1` FOREIGN KEY (`espacio_academico_id`) REFERENCES `espacios_academicos` (`espacio_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sesiones`
--

LOCK TABLES `sesiones` WRITE;
/*!40000 ALTER TABLE `sesiones` DISABLE KEYS */;
INSERT INTO `sesiones` VALUES (1,'2021-05-03','05:56:00','08:54:00',1),(2,'2021-05-04','06:54:00','08:59:00',2),(3,'2021-05-05','11:20:00','01:20:00',NULL),(4,'2021-05-06','09:22:00','00:20:00',3),(5,'2021-05-04','10:52:00','02:50:00',4);
/*!40000 ALTER TABLE `sesiones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-02 11:27:56
