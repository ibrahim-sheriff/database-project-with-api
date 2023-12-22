CREATE TABLE IF NOT EXISTS students (
    id INT NOT NULL,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    phone VARCHAR(45) NULL,
    date_of_birth DATE NULL,
    address VARCHAR(45) NULL,

    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS courses (
    id INT NOT NULL,
    code VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(45) NOT NULL UNIQUE,
    description VARCHAR(100),
    
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS sections (
    id INT NOT NULL,
    year INT NOT NULL,
    semester INT NOT NULL,
    room_number INT,
    room_building VARCHAR(5),
    course_id INT,
    
    PRIMARY KEY (id),

    CONSTRAINT fk_sections_1
        FOREIGN KEY (course_id)
        REFERENCES courses (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS student_sections (
    section_id INT NOT NULL,
    student_id INT NOT NULL,
    grade VARCHAR(3),

    PRIMARY KEY (section_id, student_id),

    CONSTRAINT fk_student_sections_1
        FOREIGN KEY (section_id)
        REFERENCES sections (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_student_sections_2
        FOREIGN KEY (student_id)
        REFERENCES students (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
