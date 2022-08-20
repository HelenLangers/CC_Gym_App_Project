DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS lessons;

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    duration VARCHAR(255),
    instructor VARCHAR(255),
    location VARCHAR(255),
    capacity INT,
    Description VARCHAR(255)
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE
);