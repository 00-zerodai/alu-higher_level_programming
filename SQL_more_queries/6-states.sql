-- Create hbtn_0d_usa and its states table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create states with a required auto-generated primary key and name.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
