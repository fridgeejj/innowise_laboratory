-- 1. All grades for Alice Johnson
SELECT subject, grade
FROM grades
WHERE student_id = (SELECT id FROM students WHERE full_name = 'Alice Johnson');

-- 2. Average grade per student
SELECT students.full_name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id;

-- 3. Students born after 2004
SELECT *
FROM students
WHERE birth_year > 2004;

-- 4. Subjects and their average grades
SELECT subject, AVG(grade) AS average_grade
FROM grades
GROUP BY subject;

-- 5. Top 3 students with highest average grade
SELECT students.full_name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 3;

-- 6. Students with any grade below 80
SELECT DISTINCT students.full_name
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grade < 80;
