/*
 Navicat Premium Data Transfer

 Source Server         : COMP0035
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : schema_group07

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 08/01/2021 03:20:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments`  (
  `CommentID` int(0) NOT NULL,
  `Time` int(0) NULL DEFAULT NULL,
  `Content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `student_id` int(0) NOT NULL,
  PRIMARY KEY (`CommentID`) USING BTREE,
  INDEX `fk_comments_student1_idx`(`student_id`) USING BTREE,
  CONSTRAINT `fk_comments_student1` FOREIGN KEY (`student_id`) REFERENCES `student` (`StudentID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for enquiresbystudent
-- ----------------------------
DROP TABLE IF EXISTS `enquiresbystudent`;
CREATE TABLE `enquiresbystudent`  (
  `student_id` int(0) NOT NULL,
  `enquiryinfo_EnquiryID` int(0) NOT NULL,
  PRIMARY KEY (`student_id`, `enquiryinfo_EnquiryID`) USING BTREE,
  INDEX `fk_enquiresbystudent_student1_idx`(`student_id`) USING BTREE,
  INDEX `fk_enquiresbystudent_enquiryinfo1_idx`(`enquiryinfo_EnquiryID`) USING BTREE,
  CONSTRAINT `fk_enquiresbystudent_enquiryinfo1` FOREIGN KEY (`enquiryinfo_EnquiryID`) REFERENCES `enquiryinfo` (`EnquiryID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_enquiresbystudent_student1` FOREIGN KEY (`student_id`) REFERENCES `student` (`StudentID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for enquiryinfo
-- ----------------------------
DROP TABLE IF EXISTS `enquiryinfo`;
CREATE TABLE `enquiryinfo`  (
  `EnquiryID` int(0) NOT NULL,
  `OccupationID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `IndustryID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`EnquiryID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for governmentdata
-- ----------------------------
DROP TABLE IF EXISTS `governmentdata`;
CREATE TABLE `governmentdata`  (
  `Year` int(0) NULL DEFAULT NULL,
  `IndustryID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `OccupationID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Location` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `NumOfJobs` int(0) NULL DEFAULT NULL,
  `enquiryinfo_EnquiryID` int(0) NOT NULL,
  INDEX `fk_governmentdata_enquiryinfo1`(`enquiryinfo_EnquiryID`) USING BTREE,
  CONSTRAINT `fk_governmentdata_enquiryinfo1` FOREIGN KEY (`enquiryinfo_EnquiryID`) REFERENCES `enquiryinfo` (`EnquiryID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for images
-- ----------------------------
DROP TABLE IF EXISTS `images`;
CREATE TABLE `images`  (
  `ImageID` int(0) NOT NULL,
  `Content` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ImageID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for occupations
-- ----------------------------
DROP TABLE IF EXISTS `occupations`;
CREATE TABLE `occupations`  (
  `OccupationID` int(0) NOT NULL,
  `OccupationName` varchar(225) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`OccupationID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for occupations_student
-- ----------------------------
DROP TABLE IF EXISTS `occupations_student`;
CREATE TABLE `occupations_student`  (
  `student_id` int(0) NOT NULL,
  `occupations_id` int(0) NOT NULL,
  PRIMARY KEY (`student_id`, `occupations_id`) USING BTREE,
  INDEX `fk_occupations_student_occupations1_idx`(`occupations_id`) USING BTREE,
  CONSTRAINT `fk_occupations_student_occupations1` FOREIGN KEY (`occupations_id`) REFERENCES `occupations` (`OccupationID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_occupations_student_student1` FOREIGN KEY (`student_id`) REFERENCES `student` (`StudentID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for qualification
-- ----------------------------
DROP TABLE IF EXISTS `qualification`;
CREATE TABLE `qualification`  (
  `ID` int(0) NOT NULL,
  `QualificationName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for savedimages
-- ----------------------------
DROP TABLE IF EXISTS `savedimages`;
CREATE TABLE `savedimages`  (
  `student_id` int(0) NOT NULL,
  `images_ImageID` int(0) NOT NULL,
  PRIMARY KEY (`student_id`, `images_ImageID`) USING BTREE,
  INDEX `fk_savedimages_images1_idx`(`images_ImageID`) USING BTREE,
  CONSTRAINT `fk_savedimages_images1` FOREIGN KEY (`images_ImageID`) REFERENCES `images` (`ImageID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_savedimages_student1` FOREIGN KEY (`student_id`) REFERENCES `student` (`StudentID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `StudentID` int(0) NOT NULL,
  `FirstName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `LastName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`StudentID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for student_qualification
-- ----------------------------
DROP TABLE IF EXISTS `student_qualification`;
CREATE TABLE `student_qualification`  (
  `student_id` int(0) NOT NULL,
  `qualification_ID` int(0) NOT NULL,
  PRIMARY KEY (`student_id`, `qualification_ID`) USING BTREE,
  INDEX `fk_Student_Qualification_qualification1_idx`(`qualification_ID`) USING BTREE,
  CONSTRAINT `fk_Student_Qualification_qualification1` FOREIGN KEY (`qualification_ID`) REFERENCES `qualification` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_Student_Qualification_student1` FOREIGN KEY (`student_id`) REFERENCES `student` (`StudentID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
