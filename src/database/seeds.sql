USE db_anunbis;
ALTER DATABASE db_anunbis CHARACTER SET utf8 COLLATE utf8_general_ci;

INSERT INTO COURSE (id_course, name) VALUES (1, 'Engenharia de Software');
INSERT INTO COURSE (id_course, name) VALUES (2, 'Engenharia de Energia');
INSERT INTO COURSE (id_course, name) VALUES (3, 'Engenharia Eletronica');
INSERT INTO COURSE (id_course, name) VALUES (4, 'Engenharia Automotiva');
INSERT INTO COURSE (id_course, name) VALUES (5, 'Engenharia Aeroespacial');

INSERT INTO DISCIPLINE (discipline_code, name) VALUES ('FGA01', 'Metodos Desenvolvimento de Software');
INSERT INTO DISCIPLINE (discipline_code, name) VALUES ('FGA02', 'Orientação a Objetos');
INSERT INTO DISCIPLINE (discipline_code, name) VALUES ('FGA03', 'Estrutura de Dados');

INSERT INTO COURSE_DISCIPLINE (id_course, discipline_code) VALUES(1, 'FGA01');
INSERT INTO COURSE_DISCIPLINE (id_course, discipline_code) VALUES(1, 'FGA02');
INSERT INTO COURSE_DISCIPLINE (id_course, discipline_code) VALUES(1, 'FGA03');

INSERT INTO PROFESSOR (id_professor, name) VALUES (1, 'Professor a');
INSERT INTO PROFESSOR (id_professor, name) VALUES (2, 'Professor b');
INSERT INTO PROFESSOR (id_professor, name) VALUES (3, 'Professor c');

INSERT INTO PROFESSOR_DISCIPLINE (discipline_code, id_professor) VALUES ('FGA01', 1);
INSERT INTO PROFESSOR_DISCIPLINE (discipline_code, id_professor) VALUES ('FGA01', 2);
INSERT INTO PROFESSOR_DISCIPLINE (discipline_code, id_professor) VALUES ('FGA01', 3);
INSERT INTO PROFESSOR_DISCIPLINE (discipline_code, id_professor) VALUES ('FGA02', 3);
INSERT INTO PROFESSOR_DISCIPLINE (discipline_code, id_professor) VALUES ('FGA02', 2);
INSERT INTO PROFESSOR_DISCIPLINE (discipline_code, id_professor) VALUES ('FGA03', 1);





