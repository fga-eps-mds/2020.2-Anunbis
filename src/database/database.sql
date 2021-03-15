-- this file will run in the first time when docker-compose up
USE db_anunbis;

CREATE TABLE IF NOT EXISTS PROFESSOR (
  reg_professor int UNSIGNED UNIQUE NOT NULL,
  `name` varchar(255) NOT NULL,
  email varchar(255) NOT NULL UNIQUE DEFAULT '',
  `password` varchar(64) NOT NULL DEFAULT '',
  rating float,
  PRIMARY KEY (reg_professor)
);

CREATE TABLE IF NOT EXISTS DISCIPLINE (
  discipline_code varchar(80) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (discipline_code)
);

CREATE TABLE IF NOT EXISTS PROFESSOR_DISCIPLINE (
  discipline_code varchar(80) NOT NULL,
  reg_professor int UNSIGNED NOT NULL,
  PRIMARY KEY (discipline_code, reg_professor),
  FOREIGN KEY (discipline_code)  REFERENCES DISCIPLINE  (discipline_code),
  FOREIGN KEY (reg_professor)  REFERENCES PROFESSOR  (reg_professor)
);
      
CREATE TABLE IF NOT EXISTS COURSE (
  id_course int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (id_course)
)ENGINE InnoDB AUTO_INCREMENT = 0;

CREATE TABLE IF NOT EXISTS COURSE_DISCIPLINE (
  id_course int UNSIGNED NOT NULL,
  discipline_code varchar(80) NOT NULL,
  PRIMARY KEY (id_course, discipline_code),
  FOREIGN KEY (id_course)  REFERENCES COURSE  (id_course)
);

CREATE TABLE IF NOT EXISTS STUDENT (
  reg_student int UNSIGNED NOT NULL UNIQUE,
  `name` varchar(255) NOT NULL,
  email varchar(100) NOT NULL UNIQUE,
  `password` varchar(64) NOT NULL,
  id_course int UNSIGNED NOT NULL,
  PRIMARY KEY (reg_student),
  FOREIGN KEY (id_course) REFERENCES COURSE (id_course)
);

CREATE TABLE IF NOT EXISTS POST (
  id_post int UNSIGNED NOT NULL,
  reg_student int UNSIGNED DEFAULT NULL,
  reg_professor int UNSIGNED NOT NULL,
  content varchar(480) NOT NULL,
  post_date date NOT NULL,
  rating float NOT NULL,
  discipline_code int UNSIGNED NOT NULL,
  PRIMARY KEY (id_post),
  FOREIGN KEY (reg_student) REFERENCES STUDENT (reg_student),
  FOREIGN KEY (reg_professor) REFERENCES PROFESSOR (reg_professor)
)ENGINE InnoDB AUTO_INCREMENT = 0;

CREATE TABLE IF NOT EXISTS DISAGREE_STUDENT_POST (
  id_post int UNSIGNED NOT NULL,
  reg_student int UNSIGNED NOT NULL,
  PRIMARY KEY (id_post, reg_student),
  FOREIGN KEY (id_post) REFERENCES POST (id_post),
  FOREIGN KEY (reg_student) REFERENCES STUDENT (reg_student)
);

CREATE TABLE IF NOT EXISTS AGREE_STUDENT_POST (
  id_post int UNSIGNED NOT NULL,
  reg_student int UNSIGNED NOT NULL,
  FOREIGN KEY (id_post) REFERENCES POST (id_post),
  FOREIGN KEY (reg_student) REFERENCES STUDENT (reg_student)
);

CREATE TABLE IF NOT EXISTS REPORT(
  id_report int AUTO_INCREMENT,
  id_post int UNSIGNED NOT NULL,
  content varchar(120) NOT NULL DEFAULT '',
  report_type enum('L', 'I', 'G', 'O') NOT NULL,
  reg_student int NOT NULL,
  PRIMARY KEY (id_report),
  FOREIGN KEY (id_post) REFERENCES POST (id_post)
)ENGINE InnoDB AUTO_INCREMENT = 0;