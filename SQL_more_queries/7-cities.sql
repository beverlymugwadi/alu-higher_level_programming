--Create database, Create table with constraints
--Creating database
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
--Switch to database
USE hbtn_0d_usa;
--Creating table
CREATE TABLE IF NOT EXIST cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
