CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    birth_year INTEGER
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
);
