CREATE DATABASE expenses_tracker;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(30),
    email VARCHAR(50) UNIQUE,
    created_date DATE
);

-- Category table
CREATE TABLE category (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50) unique
);

-- Expenses table
CREATE TABLE expenses (
    expenses_id INT PRIMARY KEY,
    user_id INT,
    category_name varchar(50),
    amount INT,
    payment_method VARCHAR(30),

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_name) REFERENCES category(category_name)
);
