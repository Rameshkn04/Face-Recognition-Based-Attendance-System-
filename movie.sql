-- Create database
CREATE DATABASE movie_ticket_booking;
USE movie_ticket_booking;

-- Create tables
CREATE TABLE industry (
    id INT AUTO_INCREMENT PRIMARY KEY,
    industry_name VARCHAR(255) NOT NULL
);

CREATE TABLE language (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lang_name VARCHAR(255) NOT NULL
);

CREATE TABLE genre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);

CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    movie_banner VARCHAR(255) NOT NULL,
    rel_date DATE NOT NULL,
    industry_id INT NOT NULL,
    genre_id INT NOT NULL,
    lang_id INT NOT NULL,
    duration VARCHAR(255),
    FOREIGN KEY (industry_id) REFERENCES industry(id),
    FOREIGN KEY (genre_id) REFERENCES genre(id),
    FOREIGN KEY (lang_id) REFERENCES language(id)
);

CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE show_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    show_date DATETIME NOT NULL,
    cinema_name VARCHAR(255) NOT NULL,
    ticket_price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movie(id)
);
CREATE TABLE show_time (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time TIME NOT NULL
);


CREATE TABLE seat_reserved (
    id INT AUTO_INCREMENT PRIMARY KEY,
    show_id INT NOT NULL,
    customer_id INT NOT NULL,
    seat_number VARCHAR(255) NOT NULL,
    status ENUM('true', 'false') NOT NULL,
    FOREIGN KEY (show_id) REFERENCES show_table(id),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE seat_detail (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cust_id INT NOT NULL,
    show_id INT NOT NULL,
    no_of_tickets INT NOT NULL,
    FOREIGN KEY (show_id) REFERENCES show_table(id),
    FOREIGN KEY (cust_id) REFERENCES customer(id)
);
CREATE TABLE slider (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT
);


CREATE TABLE booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    show_id INT NOT NULL,
    no_of_tickets INT NOT NULL,
    seat_detail_id INT NOT NULL,
    booking_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (show_id) REFERENCES show_table(id),
    FOREIGN KEY (seat_detail_id) REFERENCES seat_detail(id)
);

CREATE TABLE cinema (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE seats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    show_id INT,
    `row` CHAR(1),
    number INT,
    status VARCHAR(10), -- e.g., 'available', 'sold'
    section VARCHAR(20) -- e.g., 'VIP', 'PREMIUM', 'EXECUTIVE', 'NORMAL'
);


ALTER TABLE show_table
ADD COLUMN no_seat INT NOT NULL;
ALTER TABLE show_table
ADD COLUMN cinema_id INT NOT NULL;
ALTER TABLE show_table
ADD COLUMN show_time_id INT NOT NULL;
ALTER TABLE seats ADD INDEX idx_show_id (show_id);
ALTER TABLE seats ADD INDEX idx_status (status);
ALTER TABLE seats ADD price DECIMAL(10, 2) ;-- Added price field for seat price
ALTER TABLE seat_reserved ADD COLUMN status VARCHAR(255) DEFAULT 'available';
ALTER TABLE bookings ADD COLUMN num_tickets INT;
ALTER TABLE seat_reserved
ADD CONSTRAINT fk_show
FOREIGN KEY (show_id) REFERENCES shows(show_id);
ALTER TABLE bookings ADD COLUMN seat_detail_id INT;
DESCRIBE bookings;
ALTER TABLE bookings MODIFY booking_date DATE;





-- Insert sample data
INSERT INTO industry (industry_name) VALUES ('Bollywood'), ('Hollywood'), ('Tollywood');
INSERT INTO language (lang_name) VALUES ('English'), ('Hindi'), ('Telugu');
INSERT INTO genre (genre_name) VALUES ('Action'), ('Comedy'), ('Drama');
INSERT INTO movie (name, movie_banner, rel_date, industry_id, genre_id, lang_id, duration)
VALUES ('Demon', 'images/movie/demon.jpg', '2024-06-30', 1, 1, 1, '2hr 30min');
INSERT INTO customer (username, password, email) VALUES ('john_doe', 'password123', 'john@example.com');
INSERT INTO customer (username, password, email) VALUES ('Ramesh KN', '12345', 'Rameshkn2004@gmail.com');
INSERT INTO show_table (movie_id, show_date, cinema_name, ticket_price)
VALUES (1, '2024-07-12 21:00:00', 'Demon', 600.00);
INSERT INTO show_time (time) VALUES ('12:00:00'), ('15:00:00'), ('18:00:00');
INSERT INTO cinema (name) VALUES ('Cinema Hall 1'), ('Cinema Hall 2'), ('Cinema Hall 3');
INSERT INTO show_table (movie_id, show_date, cinema_name, ticket_price, no_seat)
VALUES (1, '2024-07-01 18:00:00', 'Cinema Hall 1', 600.00, 100);
INSERT INTO show_table (movie_id, show_date, cinema_name, ticket_price, no_seat, cinema_id)
VALUES (1, '2024-07-01 18:00:00', 'Cinema Hall 1', 600.00, 100, 1);
INSERT INTO show_table (movie_id, show_date, cinema_name, ticket_price, no_seat, cinema_id, show_time_id)
VALUES (1, '2024-07-01 18:00:00', 'Cinema Hall 1', 600.00, 100, 1, 1);
INSERT INTO show_table (movie_id, show_date, cinema_name, ticket_price, no_seat, cinema_id, show_time_id)
VALUES (2, '2024-07-25 18:00:00', 'Cinema Hall 1', 200.00, 100, 2, 2);
INSERT INTO show_table (movie_id, show_date, cinema_name, ticket_price, no_seat, cinema_id, show_time_id)
VALUES (7, '2024-07-25 18:00:00', 'Cinema Hall 1', 200.00, 100, 2, 2);
INSERT INTO shows (show_id, movie_name, cinema_name, show_datetime, ticket_price) 
VALUES (7, 'Example Movie', 'Example Cinema', '2024-07-25 19:00:00', 200.00);
SELECT * FROM movie WHERE id = 7;




-- Inserting VIP seats
INSERT INTO seats (show_id, `row`, number, status, section,price) VALUES
(1, 'J', 1, 'available', 'VIP',250),
(1, 'J', 2, 'available', 'VIP',250),
(1, 'J', 3, 'available', 'VIP',250),
(1, 'J', 4, 'available', 'VIP',250),
(1, 'J', 5, 'available', 'VIP',250),
(1, 'J', 6, 'available', 'VIP',250),
(1, 'J', 7, 'available', 'VIP',250),
(1, 'J', 8, 'available', 'VIP',250),
(1, 'J', 9, 'available', 'VIP',250),
(1, 'J', 10, 'available', 'VIP',250);

-- Inserting PREMIUM seats
INSERT INTO seats (show_id, `row`, number, status, section,price) VALUES
(1, 'I', 1, 'available', 'PREMIUM',200),
(1, 'I', 2, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats as needed
(1, 'H', 1, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats for row H
(1, 'G', 1, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats for row G
(1, 'F', 1, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats for row F
(1, 'E', 1, 'available', 'PREMIUM',200);
-- Add more PREMIUM seats for row E

-- Inserting EXECUTIVE seats
INSERT INTO seats (show_id, `row`, number, status, section,price) VALUES
(1, 'D', 1, 'available', 'EXECUTIVE',180),
(1, 'D', 2, 'available', 'EXECUTIVE',180),
-- Add more EXECUTIVE seats as needed
(1, 'C', 1, 'available', 'EXECUTIVE',180);
-- Add more EXECUTIVE seats for row C
INSERT INTO seats (show_id, `row`, number, status, section,price) VALUES
(1, 'J', 1, 'available', 'VIP',250),
(1, 'J', 2, 'available', 'VIP',250),
(1, 'J', 3, 'available', 'VIP',250),
(1, 'J', 4, 'available', 'VIP',250),
(1, 'J', 5, 'available', 'VIP',250),
(1, 'J', 6, 'available', 'VIP',250),
(1, 'J', 7, 'available', 'VIP',250),
(1, 'J', 8, 'available', 'VIP',250),
(1, 'J', 9, 'available', 'VIP',250),
(1, 'J', 10, 'available', 'VIP',250);

-- Inserting PREMIUM seats
INSERT INTO seats (show_id, `row`, number, status, section,price) VALUES
(1, 'I', 1, 'available', 'PREMIUM',200),
(1, 'I', 2, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats as needed
(1, 'H', 1, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats for row H
(1, 'G', 1, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats for row G
(1, 'F', 1, 'available', 'PREMIUM',200),
-- Add more PREMIUM seats for row F
(1, 'E', 1, 'available', 'PREMIUM',200);
-- Add more PREMIUM seats for row E

-- Inserting EXECUTIVE seats
INSERT INTO seats (show_id, `row`, number, status, section,price) VALUES
(2, 'D', 1, 'available', 'EXECUTIVE',180),
(2, 'D', 2, 'available', 'EXECUTIVE',180),
-- Add more EXECUTIVE seats as needed
(2, 'C', 1, 'available', 'EXECUTIVE',180);

-- Inserting NORMAL seats
INSERT INTO seats (show_id, `row`, number, status, section, price) VALUES
(2, 'B', 1, 'available', 'NORMAL',150),
(2, 'B', 2, 'available', 'NORMAL',150),
-- Add more NORMAL seats as needed
(2, 'A', 1, 'available', 'NORMAL',150);
-- Add more NORMAL seats for row A
INSERT INTO booking (cust_id, show_id, num_tickets, seat_detail_id, booking_date, total_amount)
VALUES (1, 1, 2, 1, '2024-07-21', 150.00);


-- Additional insert commands based on your data requirements

