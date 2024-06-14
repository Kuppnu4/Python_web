drop table if exists groups;
CREATE TABLE groups (
	id SERIAL PRIMARY key, 
	name VARCHAR(50) NOT NULL
);  

drop table if exists students;
CREATE TABLE students (
	id SERIAL PRIMARY key, 
	fullname VARCHAR(150) NOT NULL,
	group_id INTEGER REFERENCES groups(id)
); 

drop table if exists teachers;
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL
);

drop table if exists subjects;
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
);

drop table if exists grades;
CREATE TABLE grades (
    id SERIAL PRIMARY key,
    student_id INTEGER REFERENCES students(id),
    subject_id INTEGER REFERENCES subjects(id),
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    grade_date DATE NOT NULL
);