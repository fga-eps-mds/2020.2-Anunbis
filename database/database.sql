-- this file will run in the first time when docker-compose up
USE db_anunbis;

CREATE TABLE IF NOT EXISTS professor (
  id_professor int UNSIGNED AUTO_INCREMENT,
  reg_professor bigint UNSIGNED UNIQUE,
  `name` varchar(255) NOT NULL,
  email varchar(255) UNIQUE,
  `password` varchar(255),
  PRIMARY KEY (id_professor)
)ENGINE InnoDB AUTO_INCREMENT = 0;

CREATE TABLE IF NOT EXISTS discipline (
  discipline_code varchar(80) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (discipline_code)
);

CREATE TABLE IF NOT EXISTS professor_discipline (
  discipline_code varchar(80) NOT NULL,
  id_professor int UNSIGNED NOT NULL,
  PRIMARY KEY (discipline_code, id_professor),
  FOREIGN KEY (discipline_code)  REFERENCES discipline  (discipline_code),
  FOREIGN KEY (id_professor)  REFERENCES professor  (id_professor)
);
      
CREATE TABLE IF NOT EXISTS course (
  id_course int UNSIGNED AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (id_course)
);

CREATE TABLE IF NOT EXISTS course_discipline (
  id_course int UNSIGNED NOT NULL,
  discipline_code varchar(80) NOT NULL DEFAULT '',
  PRIMARY KEY (id_course, discipline_code),
  FOREIGN KEY (id_course)  REFERENCES course (id_course),
  FOREIGN KEY (discipline_code)  REFERENCES discipline (discipline_code)
);

CREATE TABLE IF NOT EXISTS student (
  reg_student int UNSIGNED NOT NULL UNIQUE,
  `name` varchar(255) NOT NULL,
  email varchar(100) NOT NULL UNIQUE,
  `password` varchar(255) NOT NULL,
  id_course int UNSIGNED NOT NULL,
  PRIMARY KEY (reg_student),
  FOREIGN KEY (id_course) REFERENCES course (id_course)
);

CREATE TABLE IF NOT EXISTS post (
  id_post int UNSIGNED AUTO_INCREMENT,
  reg_student int UNSIGNED DEFAULT NULL,
  id_professor int UNSIGNED NOT NULL,
  content varchar(480) NOT NULL,
  post_date date NOT NULL,
  didactic TINYINT UNSIGNED NOT NULL,
  metod TINYINT UNSIGNED NOT NULL,
  avaliations TINYINT UNSIGNED NOT NULL,
  disponibility TINYINT UNSIGNED NOT NULL,
  discipline_code varchar(80) NOT NULL DEFAULT '',
  is_anonymous TINYINT(1) NOT NULL,
  PRIMARY KEY (id_post),
  FOREIGN KEY (discipline_code) REFERENCES discipline (discipline_code),
  FOREIGN KEY (reg_student) REFERENCES student (reg_student),
  FOREIGN KEY (id_professor) REFERENCES professor (id_professor)
)ENGINE InnoDB AUTO_INCREMENT = 0;

CREATE TABLE IF NOT EXISTS disagree_student_post (
  id_post int UNSIGNED NOT NULL,
  reg_student int UNSIGNED NOT NULL,
  PRIMARY KEY (id_post, reg_student),
  FOREIGN KEY (id_post) REFERENCES post (id_post),
  FOREIGN KEY (reg_student) REFERENCES student (reg_student)
);

CREATE TABLE IF NOT EXISTS agree_student_post (
  id_post int UNSIGNED NOT NULL,
  reg_student int UNSIGNED NOT NULL,
  FOREIGN KEY (id_post) REFERENCES post (id_post),
  FOREIGN KEY (reg_student) REFERENCES student (reg_student)
);

CREATE TABLE IF NOT EXISTS report(
  id_report int UNSIGNED AUTO_INCREMENT,
  id_post int UNSIGNED NOT NULL,
  content varchar(120) NOT NULL DEFAULT '',
  offensive TINYINT(1) NOT NULL,
  prejudice TINYINT(1) NOT NULL,
  unrelated TINYINT(1) NOT NULL,
  others TINYINT(1) NOT NULL,
  reg_student int UNSIGNED,
  id_professor int UNSIGNED,
  PRIMARY KEY (id_report),
  FOREIGN KEY (id_post) REFERENCES post (id_post),
  FOREIGN KEY (reg_student) REFERENCES student (reg_student),
  FOREIGN KEY (id_professor) REFERENCES professor (id_professor)
)ENGINE InnoDB AUTO_INCREMENT = 0;