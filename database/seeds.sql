USE db_anunbis;
ALTER DATABASE db_anunbis CHARACTER SET utf8 COLLATE utf8_general_ci;

INSERT INTO course (id_course, name) VALUES (1, 'Engenharia de Software');
INSERT INTO course (id_course, name) VALUES (2, 'Engenharia de Energia');
INSERT INTO course (id_course, name) VALUES (3, 'Engenharia Eletronica');
INSERT INTO course (id_course, name) VALUES (4, 'Engenharia Automotiva');
INSERT INTO course (id_course, name) VALUES (5, 'Engenharia Aeroespacial');

INSERT INTO discipline (discipline_code, name) VALUES ('FGA01', 'Metodos Desenvolvimento de Software');
INSERT INTO discipline (discipline_code, name) VALUES ('FGA02', 'Orientação a Objetos');
INSERT INTO discipline (discipline_code, name) VALUES ('FGA03', 'Estrutura de Dados');

INSERT INTO course_discipline (id_course, discipline_code) VALUES(1, 'FGA01');
INSERT INTO course_discipline (id_course, discipline_code) VALUES(1, 'FGA02');
INSERT INTO course_discipline (id_course, discipline_code) VALUES(1, 'FGA03');

INSERT INTO professor (id_professor, name) VALUES (1, 'Professor a');
INSERT INTO professor (id_professor, name) VALUES (2, 'Professor b');
INSERT INTO professor (id_professor, name) VALUES (3, 'Professor c');

INSERT INTO professor_discipline (discipline_code, id_professor) VALUES ('FGA01', 1);
INSERT INTO professor_discipline (discipline_code, id_professor) VALUES ('FGA01', 2);
INSERT INTO professor_discipline (discipline_code, id_professor) VALUES ('FGA01', 3);
INSERT INTO professor_discipline (discipline_code, id_professor) VALUES ('FGA02', 3);
INSERT INTO professor_discipline (discipline_code, id_professor) VALUES ('FGA02', 2);
INSERT INTO professor_discipline (discipline_code, id_professor) VALUES ('FGA03', 1);





