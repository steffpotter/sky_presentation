create database if not exists db_devOpsNotes;

use db_devOpsNotes;
create table if not exists subject
(
	subject_id int not null auto_increment primary key, 
    subject_name varchar(100) null,
    subject_logo varchar(1000) null
);

create table if not exists paragraph
(
	paragraph_id int not null auto_increment primary key, 
    paragraph_text varchar(1000) null
);

create table if not exists subject_paragraph(
    paragraph_id int not null, 
    subject_id int not null, 
    CONSTRAINT paragraph_id FOREIGN KEY (paragraph_id) references paragraph(paragraph_id),
    CONSTRAINT subject_id FOREIGN KEY (subject_id) references subject(subject_id)
);

create table if not exists candidate
(
	candidate_id int not null auto_increment primary key, 
    first_name varchar(100) null,
    last_name varchar(100) null,
    fun_fact varchar(1000) null
);

create table if not exists answer
(
	answer_id int not null auto_increment primary key, 
    answer_text varchar(1000) null
);

create table if not exists question
(
	question_id int not null auto_increment primary key, 
    question_text varchar(1000) null,
    subject_id int not null, 
    answer_id int null, 
    CONSTRAINT subject_id_ FOREIGN KEY (subject_id) references subject(subject_id),
    CONSTRAINT answer_id FOREIGN KEY (answer_id) references answer(answer_id)
);

create table if not exists question_answer(
    answer_id int not null, 
    question_id int not null, 
    CONSTRAINT answer_id_ FOREIGN KEY (answer_id) references answer(answer_id),
    CONSTRAINT question_id FOREIGN KEY (question_id) references question(question_id)
);

INSERT INTO candidate (first_name, last_name, fun_fact)
VALUES("Steff", "Potter", "I play rugby!");

INSERT INTO subject (subject_name, subject_logo)
VALUES
    ("Python", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/438px-Python-logo-notext.svg.png"), 
    ("Flask", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/640px-Flask_logo.svg.png"), 
    ("Html", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/480px-HTML5_logo_and_wordmark.svg.png"), 
    ("Git", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/640px-Git-logo.svg.png"), 
    ("Agile", "https://www.svgrepo.com/show/379764/agile.svg");

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