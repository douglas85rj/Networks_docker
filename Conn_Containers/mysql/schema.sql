CREATE DATABASE flaskdocker;
USE flaskdocker;


CREATE TABLE flaskdocker.users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);