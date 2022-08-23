DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS instructors;

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    speciality VARCHAR(255),
    bio VARCHAR(255)
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    date DATE NOT NULL,
    time VARCHAR(255),
    duration VARCHAR(255),
    instructor_id INT REFERENCES instructors(id) ON DELETE CASCADE,
    location VARCHAR(255),
    capacity INT,
    description VARCHAR(255)
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    UNIQUE (lesson_id, member_id)
);