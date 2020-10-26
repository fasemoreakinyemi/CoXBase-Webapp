CREATE DATABASE  IF NOT EXISTS `MLVA` ;
USE `MLVA`;
-- Table structure for table `FlankLengthISPCR`

DROP TABLE IF EXISTS `FlankLengthISPCR`;
CREATE TABLE `FlankLengthISPCR` (
  `ID` varchar(36) NOT NULL,
  `ms01` int DEFAULT NULL,
  `ms03` int DEFAULT NULL,
  `ms20` int DEFAULT NULL,
  `ms21` int DEFAULT NULL,
  `ms22` int DEFAULT NULL,
  `ms23` int DEFAULT NULL,
  `ms24` int DEFAULT NULL,
  `ms26` int DEFAULT NULL,
  `ms27` int DEFAULT NULL,
  `ms28` int DEFAULT NULL,
  `ms30` int DEFAULT NULL,
  `ms31` int DEFAULT NULL,
  `ms33` int DEFAULT NULL,
  `ms34` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `FlankLengthISPCR_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `ProductLengthISPCR` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `MLVAProfile`

DROP TABLE IF EXISTS `MLVAProfile`;
CREATE TABLE `MLVAProfile` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `PanelType` varchar(30) NOT NULL,
  `ms01` float DEFAULT NULL,
  `ms03` float DEFAULT NULL,
  `ms20` float DEFAULT NULL,
  `ms21` float DEFAULT NULL,
  `ms22` float DEFAULT NULL,
  `ms23` float DEFAULT NULL,
  `ms24` float DEFAULT NULL,
  `ms26` float DEFAULT NULL,
  `ms27` float DEFAULT NULL,
  `ms28` float DEFAULT NULL,
  `ms30` float DEFAULT NULL,
  `ms31` float DEFAULT NULL,
  `ms33` float DEFAULT NULL,
  `ms34` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

-- Table structure for table `MST`

DROP TABLE IF EXISTS `MST`;
CREATE TABLE `MST` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `MSTType` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=latin1;

-- Table structure for table `Plasmid`

DROP TABLE IF EXISTS `Plasmid`;
CREATE TABLE `Plasmid` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `PlasmidType` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Table structure for table `ProductLengthISPCR`


DROP TABLE IF EXISTS `ProductLengthISPCR`;
CREATE TABLE `ProductLengthISPCR` (
  `ID` varchar(36) NOT NULL,
  `ms01` int DEFAULT NULL,
  `ms03` int DEFAULT NULL,
  `ms20` int DEFAULT NULL,
  `ms21` int DEFAULT NULL,
  `ms22` int DEFAULT NULL,
  `ms23` int DEFAULT NULL,
  `ms24` int DEFAULT NULL,
  `ms26` int DEFAULT NULL,
  `ms27` int DEFAULT NULL,
  `ms28` int DEFAULT NULL,
  `ms30` int DEFAULT NULL,
  `ms31` int DEFAULT NULL,
  `ms33` int DEFAULT NULL,
  `ms34` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `RepeatNumberISPCR`

DROP TABLE IF EXISTS `RepeatNumberISPCR`;
CREATE TABLE `RepeatNumberISPCR` (
  `ID` varchar(36) NOT NULL,
  `ms01` int DEFAULT NULL,
  `ms03` int DEFAULT NULL,
  `ms20` int DEFAULT NULL,
  `ms21` int DEFAULT NULL,
  `ms22` int DEFAULT NULL,
  `ms23` int DEFAULT NULL,
  `ms24` int DEFAULT NULL,
  `ms26` int DEFAULT NULL,
  `ms27` int DEFAULT NULL,
  `ms28` int DEFAULT NULL,
  `ms30` int DEFAULT NULL,
  `ms31` int DEFAULT NULL,
  `ms33` int DEFAULT NULL,
  `ms34` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `RepeatNumberISPCR_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `ProductLengthISPCR` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `RepeatSizeISPCR`

DROP TABLE IF EXISTS `RepeatSizeISPCR`;
CREATE TABLE `RepeatSizeISPCR` (
  `ID` varchar(36) NOT NULL,
  `ms01` int DEFAULT NULL,
  `ms03` int DEFAULT NULL,
  `ms20` int DEFAULT NULL,
  `ms21` int DEFAULT NULL,
  `ms22` int DEFAULT NULL,
  `ms23` int DEFAULT NULL,
  `ms24` int DEFAULT NULL,
  `ms26` int DEFAULT NULL,
  `ms27` int DEFAULT NULL,
  `ms28` int DEFAULT NULL,
  `ms30` int DEFAULT NULL,
  `ms31` int DEFAULT NULL,
  `ms33` int DEFAULT NULL,
  `ms34` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `RepeatSizeISPCR_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `ProductLengthISPCR` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `SampleMetadata`

DROP TABLE IF EXISTS `SampleMetadata`;
CREATE TABLE `SampleMetadata` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `SampleStrain` varchar(50) DEFAULT NULL,
  `SampleYear` year DEFAULT NULL,
  `SampleHost` varchar(30) DEFAULT NULL,
  `SampleSource` varchar(100) DEFAULT NULL,
  `SampleCountry` varchar(30) DEFAULT NULL,
  `CountryProvince` varchar(100) DEFAULT NULL,
  `Latitude` decimal(10,8) DEFAULT NULL,
  `Longitude` decimal(11,8) DEFAULT NULL,
  `PubmedID` int DEFAULT NULL,
  `PlasmidID` int NOT NULL,
  `MSTID` int NOT NULL,
  `TypingID` int NOT NULL,
  `MLVAID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `PlasmidID` (`PlasmidID`),
  KEY `MSTID` (`MSTID`),
  KEY `TypingID` (`TypingID`),
  KEY `MLVAID` (`MLVAID`),
  CONSTRAINT `SampleMetadata_ibfk_1` FOREIGN KEY (`PlasmidID`) REFERENCES `Plasmid` (`ID`),
  CONSTRAINT `SampleMetadata_ibfk_2` FOREIGN KEY (`MSTID`) REFERENCES `MST` (`ID`),
  CONSTRAINT `SampleMetadata_ibfk_3` FOREIGN KEY (`TypingID`) REFERENCES `TypingMetadata` (`ID`),
  CONSTRAINT `SampleMetadata_ibfk_4` FOREIGN KEY (`MLVAID`) REFERENCES `MLVAProfile` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=latin1;

-- Table structure for table `SubmissionTable`

DROP TABLE IF EXISTS `SubmissionTable`;
CREATE TABLE `SubmissionTable` (
  `ID` varchar(36) NOT NULL,
  `SubmissionDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `User` varchar(100) DEFAULT NULL,
  `AnalysisType` varchar(25) DEFAULT NULL,
  `IPaddress` varbinary(16) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `TypingMetadata`

DROP TABLE IF EXISTS `TypingMetadata`;
CREATE TABLE `TypingMetadata` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ClusterType` varchar(5) DEFAULT NULL,
  `Genotype` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

-- Table structure for table `UserTable`

DROP TABLE IF EXISTS `UserTable`;
CREATE TABLE `UserTable` (
  `ID` varchar(36) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(60) NOT NULL,
  `group` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `adaAProfile`

DROP TABLE IF EXISTS `adaAProfile`;
CREATE TABLE `adaAProfile` (
  `ID` varchar(36) NOT NULL,
  `adaAStatus` tinyint(1) DEFAULT NULL,
  `genotype` varchar(30) DEFAULT NULL,
  `plasmidType` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `alembic_version`

DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Table structure for table `bionumerics_is1111`

DROP TABLE IF EXISTS `bionumerics_is1111`;
CREATE TABLE `bionumerics_is1111` (
  `ky` mediumint unsigned NOT NULL,
  `marker` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `value` tinyint unsigned DEFAULT NULL,
  `isolate_id` smallint unsigned DEFAULT NULL,
  `marker_id` tinyint unsigned DEFAULT NULL,
  `primer_id` tinyint unsigned DEFAULT NULL,
  PRIMARY KEY (`ky`,`marker`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci ROW_FORMAT=DYNAMIC;

-- Table structure for table `is1111Profile`

DROP TABLE IF EXISTS `is1111Profile`;
CREATE TABLE `is1111Profile` (
  `ID` varchar(36) NOT NULL,
  `IS1111_1` tinyint(1) DEFAULT NULL,
  `IS1111_2` tinyint(1) DEFAULT NULL,
  `IS1111_3` tinyint(1) DEFAULT NULL,
  `IS1111_4` tinyint(1) DEFAULT NULL,
  `IS1111_5` tinyint(1) DEFAULT NULL,
  `IS1111_6` tinyint(1) DEFAULT NULL,
  `IS1111_7` tinyint(1) DEFAULT NULL,
  `IS1111_8` tinyint(1) DEFAULT NULL,
  `IS1111_9` tinyint(1) DEFAULT NULL,
  `IS1111_10` tinyint(1) DEFAULT NULL,
  `IS1111_11` tinyint(1) DEFAULT NULL,
  `IS1111_12` tinyint(1) DEFAULT NULL,
  `IS1111_13` tinyint(1) DEFAULT NULL,
  `IS1111_14` tinyint(1) DEFAULT NULL,
  `IS1111_15` tinyint(1) DEFAULT NULL,
  `IS1111_16` tinyint(1) DEFAULT NULL,
  `IS1111_17` tinyint(1) DEFAULT NULL,
  `IS1111_18` tinyint(1) DEFAULT NULL,
  `IS1111_19` tinyint(1) DEFAULT NULL,
  `IS1111_20` tinyint(1) DEFAULT NULL,
  `IS1111_21` tinyint(1) DEFAULT NULL,
  `IS1111_22` tinyint(1) DEFAULT NULL,
  `IS1111_23` tinyint(1) DEFAULT NULL,
  `IS1111_24` tinyint(1) DEFAULT NULL,
  `IS1111_25` tinyint(1) DEFAULT NULL,
  `IS1111_26` tinyint(1) DEFAULT NULL,
  `IS1111_27` tinyint(1) DEFAULT NULL,
  `IS1111_28` tinyint(1) DEFAULT NULL,
  `IS1111_29` tinyint(1) DEFAULT NULL,
  `IS1111_30` tinyint(1) DEFAULT NULL,
  `IS1111_31` tinyint(1) DEFAULT NULL,
  `IS1111_32` tinyint(1) DEFAULT NULL,
  `IS1111_33` tinyint(1) DEFAULT NULL,
  `IS1111_34` tinyint(1) DEFAULT NULL,
  `IS1111_35` tinyint(1) DEFAULT NULL,
  `IS1111_36` tinyint(1) DEFAULT NULL,
  `IS1111_37` tinyint(1) DEFAULT NULL,
  `IS1111_38` tinyint(1) DEFAULT NULL,
  `IS1111_39` tinyint(1) DEFAULT NULL,
  `IS1111_40` tinyint(1) DEFAULT NULL,
  `IS1111_41` tinyint(1) DEFAULT NULL,
  `IS1111_42` tinyint(1) DEFAULT NULL,
  `IS1111_43` tinyint(1) DEFAULT NULL,
  `IS1111_44` tinyint(1) DEFAULT NULL,
  `IS1111_45` tinyint(1) DEFAULT NULL,
  `IS1111_46` tinyint(1) DEFAULT NULL,
  `IS1111_47` tinyint(1) DEFAULT NULL,
  `IS1111_48` tinyint(1) DEFAULT NULL,
  `IS1111_49` tinyint(1) DEFAULT NULL,
  `IS1111_50` tinyint(1) DEFAULT NULL,
  `IS1111_51` tinyint(1) DEFAULT NULL,
  `IS1111_53` tinyint(1) DEFAULT NULL,
  `IS1111_54` tinyint(1) DEFAULT NULL,
  `IS1111_55` tinyint(1) DEFAULT NULL,
  `IS1111_56` tinyint(1) DEFAULT NULL,
  `IS1111_57` tinyint(1) DEFAULT NULL,
  `IS1111_58` tinyint(1) DEFAULT NULL,
  `IS1111_59` tinyint(1) DEFAULT NULL,
  `IS1111_60` tinyint(1) DEFAULT NULL,
  `IS1111_61` tinyint(1) DEFAULT NULL,
  `IS1111_84` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `isolateSubmission`
--

DROP TABLE IF EXISTS `isolateSubmission`;
CREATE TABLE `isolateSubmission` (
  `ID` varchar(36) NOT NULL,
  `submissionType` varchar(10) NOT NULL,
  `SubmissionDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `isolateName` varchar(100) DEFAULT NULL,
  `isolateSource` varchar(100) DEFAULT NULL,
  `isolateHost` varchar(100) DEFAULT NULL,
  `placeOfIsolation` varchar(100) DEFAULT NULL,
  `yearOfIsolation` year DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT NULL,
  `longitude` decimal(11,8) DEFAULT NULL,
  `pubmedID` varchar(50) DEFAULT NULL,
  `genomeAccession` varchar(50) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `submitterName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `isolate_aliases`
--

DROP TABLE IF EXISTS `isolate_aliases`;
CREATE TABLE `isolate_aliases` (
  `isolateid` smallint unsigned NOT NULL,
  `name` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`isolateid`,`name`) USING BTREE,
  CONSTRAINT `FK_isolate_aliases_isolates` FOREIGN KEY (`isolateid`) REFERENCES `isolates` (`isolateid`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Table structure for table `isolate_refs2`
--

DROP TABLE IF EXISTS `isolate_refs2`;
CREATE TABLE `isolate_refs2` (
  `isolate_id` smallint unsigned NOT NULL,
  `pmid` int NOT NULL COMMENT 'PubMed ID',
  `alias` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `mlvaCRC32` int unsigned DEFAULT NULL,
  `incomplete` tinyint unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`isolate_id`,`pmid`) USING BTREE,
  KEY `IDX_refs` (`pmid`,`isolate_id`) USING BTREE,
  CONSTRAINT `FK_isolate_refs2_isolates` FOREIGN KEY (`isolate_id`) REFERENCES `isolates` (`isolateid`) ON UPDATE CASCADE,
  CONSTRAINT `FK_isolate_refs2_pubmed` FOREIGN KEY (`pmid`) REFERENCES `pubmed` (`pmid`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci ROW_FORMAT=DYNAMIC;

--
-- Table structure for table `isolates`
--

DROP TABLE IF EXISTS `isolates`;
CREATE TABLE `isolates` (
  `isolateid` smallint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `key` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `isolateNo` smallint unsigned DEFAULT NULL,
  `imbNo` varchar(14) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `giNo` smallint unsigned DEFAULT NULL,
  `dateOfIsolation` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `yearOfIsolation` smallint unsigned DEFAULT NULL,
  `host` enum('cattle','deer','goat','human','mouse','rodent','sheep','tick','environment','other') DEFAULT NULL,
  `subspecies` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `sample` varchar(100) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `tissue` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `diseasePattern` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `phase` enum('I','II','I/II') CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `zipCode` mediumint unsigned DEFAULT NULL,
  `geographicOrigin` varchar(45) DEFAULT NULL,
  `province` char(3) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `country` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `institution_id` tinyint unsigned DEFAULT NULL,
  `plasmidType` varchar(20) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `adaGene` enum('neg.','pos.','pos.*','pos.S','Q154-del','Q212-del','pos.?') CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `mlvaGenotype` char(3) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `restrictionGroup` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `mstGroup` tinyint unsigned DEFAULT NULL,
  `isGenotype` int unsigned DEFAULT NULL,
  `isGroup` char(1) DEFAULT NULL,
  `mlvaCrc32` int unsigned DEFAULT NULL,
  `genotype` int unsigned DEFAULT NULL,
  `ISO3166_1` smallint unsigned DEFAULT NULL,
  `isRef` tinyint unsigned NOT NULL DEFAULT '0',
  `chronic` tinyint unsigned NOT NULL DEFAULT '0',
  `exclude` tinyint unsigned NOT NULL DEFAULT '0',
  `invalid` tinyint unsigned NOT NULL DEFAULT '0',
  `neighbour` tinyint unsigned NOT NULL DEFAULT '0',
  `snp16` smallint unsigned DEFAULT NULL,
  `snp23` smallint unsigned DEFAULT NULL,
  `dbname` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  PRIMARY KEY (`isolateid`),
  UNIQUE KEY `IDX_name` (`name`) USING BTREE,
  UNIQUE KEY `IDX_key` (`key`),
  KEY `IDX_mst` (`mstGroup`),
  KEY `IDX_genotype` (`genotype`),
  KEY `IDX_iso` (`ISO3166_1`),
  KEY `FK_isolates_snp23` (`snp23`),
  KEY `FK_isolates_snp16` (`snp16`),
  KEY `FK_isolates_institutions` (`institution_id`),
  CONSTRAINT `FK_isolates_countries` FOREIGN KEY (`ISO3166_1`) REFERENCES `countries` (`iso`),
  CONSTRAINT `FK_isolates_institutions` FOREIGN KEY (`institution_id`) REFERENCES `institutions` (`id`),
  CONSTRAINT `FK_isolates_mstgroups` FOREIGN KEY (`mstGroup`) REFERENCES `mstgroups` (`groupid`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=571 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

--
-- Table structure for table `mlvaSubmission`
--

DROP TABLE IF EXISTS `mlvaSubmission`;
CREATE TABLE `mlvaSubmission` (
  `ID` varchar(36) NOT NULL,
  `ms01` float DEFAULT NULL,
  `ms03` float DEFAULT NULL,
  `ms20` float DEFAULT NULL,
  `ms21` float DEFAULT NULL,
  `ms22` float DEFAULT NULL,
  `ms23` float DEFAULT NULL,
  `ms24` float DEFAULT NULL,
  `ms26` float DEFAULT NULL,
  `ms27` float DEFAULT NULL,
  `ms28` float DEFAULT NULL,
  `ms30` float DEFAULT NULL,
  `ms31` float DEFAULT NULL,
  `ms33` float DEFAULT NULL,
  `ms34` float DEFAULT NULL,
  `isolateID` varchar(36) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `isolateID` (`isolateID`),
  CONSTRAINT `mlvaSubmission_ibfk_1` FOREIGN KEY (`isolateID`) REFERENCES `isolateSubmission` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `mlva_normalized`
--

DROP TABLE IF EXISTS `mlva_normalized`;
CREATE TABLE `mlva_normalized` (
  `ID` smallint NOT NULL AUTO_INCREMENT,
  `ms01` float DEFAULT NULL,
  `ms03` float DEFAULT NULL,
  `ms20` float DEFAULT NULL,
  `ms21` float DEFAULT NULL,
  `ms22` float DEFAULT NULL,
  `ms23` float DEFAULT NULL,
  `ms24` float DEFAULT NULL,
  `ms26` float DEFAULT NULL,
  `ms27` float DEFAULT NULL,
  `ms28` float DEFAULT NULL,
  `ms30` float DEFAULT NULL,
  `ms31` float DEFAULT NULL,
  `ms33` float DEFAULT NULL,
  `ms34` float DEFAULT NULL,
  `ngt` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=latin1;

--
-- Table structure for table `mstSpacerResultTable`
--

DROP TABLE IF EXISTS `mstSpacerResultTable`;
CREATE TABLE `mstSpacerResultTable` (
  `ID` varchar(36) NOT NULL,
  `cox18` int DEFAULT NULL,
  `cox2` int DEFAULT NULL,
  `cox20` int DEFAULT NULL,
  `cox22` int DEFAULT NULL,
  `cox37` int DEFAULT NULL,
  `cox5` int DEFAULT NULL,
  `cox51` int DEFAULT NULL,
  `cox56` int DEFAULT NULL,
  `cox57` int DEFAULT NULL,
  `cox61` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `mstSubmission`
--

DROP TABLE IF EXISTS `mstSubmission`;
CREATE TABLE `mstSubmission` (
  `ID` varchar(36) NOT NULL,
  `cox18` int DEFAULT NULL,
  `cox2` int DEFAULT NULL,
  `cox20` int DEFAULT NULL,
  `cox22` int DEFAULT NULL,
  `cox37` int DEFAULT NULL,
  `cox5` int DEFAULT NULL,
  `cox51` int DEFAULT NULL,
  `cox56` int DEFAULT NULL,
  `cox57` int DEFAULT NULL,
  `cox61` int DEFAULT NULL,
  `isolateID` varchar(36) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `isolateID` (`isolateID`),
  CONSTRAINT `mstSubmission_ibfk_1` FOREIGN KEY (`isolateID`) REFERENCES `isolateSubmission` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `mstalignments`
--

DROP TABLE IF EXISTS `mstalignments`;
CREATE TABLE `mstalignments` (
  `mstid` char(5) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `clustal` text CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `png` blob,
  PRIMARY KEY (`mstid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Table structure for table `mstgroups`
--

DROP TABLE IF EXISTS `mstgroups`;
CREATE TABLE `mstgroups` (
  `groupid` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `COX2` tinyint unsigned NOT NULL,
  `COX5` tinyint unsigned NOT NULL,
  `COX18` tinyint unsigned NOT NULL,
  `COX20` tinyint unsigned NOT NULL,
  `COX22` tinyint unsigned NOT NULL,
  `COX37` tinyint unsigned NOT NULL,
  `COX51` tinyint unsigned NOT NULL,
  `COX56` tinyint unsigned NOT NULL,
  `COX57` tinyint unsigned NOT NULL,
  `COX61` tinyint unsigned NOT NULL,
  PRIMARY KEY (`groupid`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Table structure for table `mstgroups2`
--

DROP TABLE IF EXISTS `mstgroups2`;
CREATE TABLE `mstgroups2` (
  `groupid` tinyint unsigned NOT NULL,
  `COX2` tinyint unsigned DEFAULT NULL,
  `COX5` tinyint unsigned DEFAULT NULL,
  `COX18` tinyint unsigned DEFAULT NULL,
  `COX20` tinyint unsigned DEFAULT NULL,
  `COX22` tinyint unsigned DEFAULT NULL,
  `COX37` tinyint unsigned DEFAULT NULL,
  `COX51` tinyint unsigned DEFAULT NULL,
  `COX56` tinyint unsigned DEFAULT NULL,
  `COX57` tinyint unsigned DEFAULT NULL,
  `COX61` tinyint unsigned DEFAULT NULL,
  PRIMARY KEY (`groupid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `primer`
--

DROP TABLE IF EXISTS `primer`;
CREATE TABLE `primer` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `marker_id` smallint unsigned DEFAULT NULL,
  `forward` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `reverse` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `probe` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `probe2` varchar(60) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `range_min` smallint unsigned DEFAULT NULL,
  `range_max` smallint unsigned DEFAULT NULL,
  `forward_code` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `reverse_code` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `probe_code` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `probe2_code` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `description` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `pmid` int DEFAULT NULL COMMENT 'PubMed ID',
  `forward_lot_number` int unsigned DEFAULT NULL,
  `reverse_lot_number` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `IDX_name` (`name`) USING BTREE,
  KEY `FK_primer_pubmed` (`pmid`),
  KEY `FK_primer_marker` (`marker_id`),
  CONSTRAINT `FK_primer_marker` FOREIGN KEY (`marker_id`) REFERENCES `marker` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_primer_pubmed` FOREIGN KEY (`pmid`) REFERENCES `pubmed` (`pmid`)
) ENGINE=InnoDB AUTO_INCREMENT=285 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci ROW_FORMAT=DYNAMIC;

--
-- Table structure for table `primer_refs`
--

DROP TABLE IF EXISTS `primer_refs`;
CREATE TABLE `primer_refs` (
  `primer_id` smallint unsigned NOT NULL,
  `pmid` int NOT NULL COMMENT 'PubMed ID',
  `name` varchar(20) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL COMMENT 'name used in publication',
  `sequence` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `length` smallint unsigned DEFAULT NULL,
  PRIMARY KEY (`primer_id`,`pmid`),
  KEY `IDX_refs` (`pmid`,`primer_id`),
  CONSTRAINT `FK_primer_refs_primer` FOREIGN KEY (`primer_id`) REFERENCES `primer` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_primer_refs_pubmed` FOREIGN KEY (`pmid`) REFERENCES `pubmed` (`pmid`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci ROW_FORMAT=DYNAMIC;

--
-- Table structure for table `pubmed`
--

DROP TABLE IF EXISTS `pubmed`;
CREATE TABLE `pubmed` (
  `pmid` int NOT NULL,
  `title` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `year` smallint unsigned NOT NULL,
  `journal` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `bibtexkey` varchar(45) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`pmid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Table structure for table `snpHornstra`
--

DROP TABLE IF EXISTS `snpHornstra`;
CREATE TABLE `snpHornstra` (
  `ID` varchar(36) NOT NULL,
  `Cox5bp81` varchar(1) DEFAULT NULL,
  `Cox22bp91` varchar(1) DEFAULT NULL,
  `Cox18bp376` varchar(1) DEFAULT NULL,
  `Cox51bp356` varchar(1) DEFAULT NULL,
  `Cox18bp34` varchar(1) DEFAULT NULL,
  `Cox5bp109` varchar(1) DEFAULT NULL,
  `Cox22bp118` varchar(1) DEFAULT NULL,
  `Cox51bp492` varchar(1) DEFAULT NULL,
  `Cox57bp327` varchar(1) DEFAULT NULL,
  `Cox56bp10` varchar(1) DEFAULT NULL,
  `Cox51bp67` varchar(1) DEFAULT NULL,
  `Cox20bp155` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `snppattern`
--

DROP TABLE IF EXISTS `snppattern`;
CREATE TABLE `snppattern` (
  `spid` int unsigned NOT NULL AUTO_INCREMENT,
  `pattern` char(7) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `posDugway` mediumint unsigned NOT NULL,
  `posRSA331` mediumint unsigned NOT NULL,
  `posRSA493` mediumint unsigned NOT NULL,
  `posQ154` mediumint unsigned NOT NULL,
  `posQ212` mediumint unsigned NOT NULL,
  `posQ177` mediumint unsigned NOT NULL,
  `posRSA334` mediumint unsigned NOT NULL,
  `coverage` tinyint unsigned NOT NULL,
  `cntA` tinyint unsigned NOT NULL,
  `cntC` tinyint unsigned NOT NULL,
  `cntG` tinyint unsigned NOT NULL,
  `cntT` tinyint unsigned NOT NULL,
  `cntAlleles` tinyint unsigned NOT NULL,
  `rgRSA493` point NOT NULL,
  PRIMARY KEY (`spid`),
  KEY `IDX_coverage` (`coverage`,`pattern`),
  KEY `IDX_alleles` (`cntAlleles`),
  SPATIAL KEY `SPX_rgRSA493` (`rgRSA493`)
) ENGINE=MyISAM AUTO_INCREMENT=16352 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Table structure for table `snpprofiles`
--

DROP TABLE IF EXISTS `snpprofiles`;
CREATE TABLE `snpprofiles` (
  `spid` smallint unsigned NOT NULL AUTO_INCREMENT,
  `spuid` smallint unsigned DEFAULT NULL,
  `gene` enum('16S','23S') CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `profile` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `snp_count` tinyint unsigned NOT NULL,
  `missing` tinyint unsigned NOT NULL,
  `control` tinyint unsigned DEFAULT NULL,
  PRIMARY KEY (`spid`),
  KEY `IDX_gene` (`gene`),
  KEY `IDX_uid` (`spuid`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci ROW_FORMAT=DYNAMIC;

--
-- Table structure for table `snps`
--

DROP TABLE IF EXISTS `snps`;
CREATE TABLE `snps` (
  `R_DB` int NOT NULL,
  `R_POSITION` int NOT NULL,
  `R_BASE` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `R_CONTIG` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `POSITION_41` int DEFAULT NULL,
  `BASE_41` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `CONTIG_41` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `POSITION_16721` int DEFAULT NULL,
  `BASE_16721` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `CONTIG_16721` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `POSITION_16791` int DEFAULT NULL,
  `BASE_16791` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `CONTIG_16791` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `POSITION_17747` int DEFAULT NULL,
  `BASE_17747` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `CONTIG_17747` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `POSITION_18975` int DEFAULT NULL,
  `BASE_18975` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `CONTIG_18975` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `POSITION_19137` int DEFAULT NULL,
  `BASE_19137` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `CONTIG_19137` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `POSITION_19139` int DEFAULT NULL,
  `BASE_19139` char(1) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
  `CONTIG_19139` varchar(35) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

-- Dump completed on 2020-10-26 13:15:35
