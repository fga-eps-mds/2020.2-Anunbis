-- this file will run in the first time when docker-compose up
USE db_anunbis;

CREATE TABLE IF NOT EXISTS PROFESSOR (
  id_professor int UNSIGNED AUTO_INCREMENT,
  reg_professor bigint UNSIGNED UNIQUE,
  `name` varchar(255) NOT NULL,
  email varchar(255) UNIQUE,
  `password` varchar(255),
  PRIMARY KEY (id_professor)
)ENGINE InnoDB AUTO_INCREMENT = 0;

CREATE TABLE IF NOT EXISTS DISCIPLINE (
  discipline_code varchar(80) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (discipline_code)
);

CREATE TABLE IF NOT EXISTS PROFESSOR_DISCIPLINE (
  discipline_code varchar(80) NOT NULL,
  id_professor int UNSIGNED NOT NULL,
  PRIMARY KEY (discipline_code, id_professor),
  FOREIGN KEY (discipline_code)  REFERENCES DISCIPLINE  (discipline_code),
  FOREIGN KEY (id_professor)  REFERENCES PROFESSOR  (id_professor)
);
      
CREATE TABLE IF NOT EXISTS COURSE (
  id_course int UNSIGNED AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (id_course)
)ENGINE InnoDB AUTO_INCREMENT = 0;

CREATE TABLE IF NOT EXISTS COURSE_DISCIPLINE (
  id_course int UNSIGNED NOT NULL,
  discipline_code varchar(80) NOT NULL DEFAULT '',
  PRIMARY KEY (id_course, discipline_code),
  FOREIGN KEY (id_course)  REFERENCES COURSE (id_course),
  FOREIGN KEY (discipline_code)  REFERENCES DISCIPLINE (discipline_code)
);

CREATE TABLE IF NOT EXISTS STUDENT (
  reg_student int UNSIGNED NOT NULL UNIQUE,
  `name` varchar(255) NOT NULL,
  email varchar(100) NOT NULL UNIQUE,
  `password` varchar(255) NOT NULL,
  id_course int UNSIGNED NOT NULL,
  PRIMARY KEY (reg_student),
  FOREIGN KEY (id_course) REFERENCES COURSE (id_course)
);

CREATE TABLE IF NOT EXISTS POST (
  id_post int UNSIGNED AUTO_INCREMENT,
  reg_student int UNSIGNED DEFAULT NULL,
  id_professor int UNSIGNED NOT NULL,
  content varchar(480) NOT NULL,
  post_date date NOT NULL,
  rating float NOT NULL,
  discipline_code varchar(80) NOT NULL DEFAULT '',
  is_anonymous TINYINT(1) NOT NULL,
  PRIMARY KEY (id_post),
  FOREIGN KEY (discipline_code) REFERENCES DISCIPLINE (discipline_code),
  FOREIGN KEY (reg_student) REFERENCES STUDENT (reg_student),
  FOREIGN KEY (id_professor) REFERENCES PROFESSOR (id_professor)
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
  id_report int UNSIGNED AUTO_INCREMENT,
  id_post int UNSIGNED NOT NULL,
  content varchar(120) NOT NULL DEFAULT '',
  report_type enum('L', 'I', 'G', 'O') NOT NULL,
  reg_student int UNSIGNED NOT NULL,
  PRIMARY KEY (id_report),
  FOREIGN KEY (id_post) REFERENCES POST (id_post),
  FOREIGN KEY (reg_student) REFERENCES STUDENT (reg_student)
)ENGINE InnoDB AUTO_INCREMENT = 0;