INSERT IGNORE INTO students (
    id, first_name, last_name, phone, date_of_birth, address
)
VALUES 
(1, 'ibrahim', 'sherif', 010, '1996-01-01', 'cairo'), 
(2, 'ahmed', 'hossam', 010, '2000-10-10', 'cairo'),
(3, 'omar', 'hassan', 012, '2005-12-12', 'aswan');

INSERT IGNORE INTO courses (
    id, code, name, description
)
VALUES 
(1, 'CC215', 'Applied Programming', 'Programming with C/C++'), 
(2, 'CC415', 'Database Systems', NULL),
(3, 'CC313', 'Numerical Methods', NULL);

INSERT IGNORE INTO sections (
    id, year, semester, room_number, room_building, course_id
)
VALUES
(1, 2022, 1, 202, 'A', 1),
(2, 2022, 1, 203, 'A', 1),
(3, 2022, 1, 102, 'A', 1),
(4, 2022, 1, 103, 'A', 1),
(5, 2021, 2, 404, 'A', 2),
(6, 2021, 2, 401, 'B', 2);

INSERT IGNORE INTO student_sections (
    section_id, student_id, grade
)
VALUES
(1, 1, 'A'),
(1, 2, 'A+'),
(1, 3, 'B+'),
(2, 1, 'C+'),
(2, 2, 'C+'),
(3, 2, 'D+'),
(3, 3, 'A+')
;
