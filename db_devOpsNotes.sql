create database if not exists db_devOpsNotes;

use db_devOpsNotes;
create table subject
(
	subject_id int not null auto_increment primary key, 
    subject_name varchar(100) null
);

create table candidate
(
	candidate_id int not null auto_increment primary key, 
    first_name varchar(100) null,
    last_name varchar(100) null,
    fun_fact varchar(1000) null
);

create table answer
(
	answer_id int not null auto_increment primary key, 
    answer_text varchar(1000) null
);

create table question
(
	question_id int not null auto_increment primary key, 
    question_text varchar(1000) null,
    subject_id int not null, 
    answer_id int null, 
    CONSTRAINT subject_id FOREIGN KEY (subject_id) references subject(subject_id),
    CONSTRAINT answer_id FOREIGN KEY (answer_id) references answer(answer_id)
);

create table question_answer(
    answer_id int not null, 
    question_id int not null, 
    CONSTRAINT answer_id_ FOREIGN KEY (answer_id) references answer(answer_id),
    CONSTRAINT question_id FOREIGN KEY (question_id) references question(question_id)
);

INSERT INTO candidate (first_name, last_name, fun_fact)
VALUES("Steff", "Potter", "I play rugby!");

INSERT INTO subject (subject_name)
VALUES("Python"), ("Flask"), ("Html"), ("Git"), ("Agile");

SELECT * FROM subject;

INSERT INTO question (question_text, subject_id)
VALUES("What is Flask?", 2);

INSERT INTO answer (answer_text)
VALUES
    ("A popular Python web framework"), 
    ("A database management system"), 
    ("A cloud-based storage solution"), 
    ("A machine learning library");

UPDATE question 
SET answer_id = 1
WHERE question_id = 2;

INSERT INTO question_answer (answer_id, question_id)
VALUES (1, 1), (2, 1), (3, 1), (4, 1);