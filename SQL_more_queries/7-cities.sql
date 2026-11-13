-- Create hbtn_0d_usa and its cities table.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create cities with a required state foreign key and name.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states (id)
);
