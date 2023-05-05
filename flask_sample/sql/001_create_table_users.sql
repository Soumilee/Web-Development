CREATE TABLE
    IS601_Users(
        id int auto_increment PRIMARY KEY,
        first_name VARCHAR(60) not null,
        last_name VARCHAR(60) not NULL, 
        username VARCHAR(60) unique,
        email VARCHAR(60) unique,
        password VARCHAR(60) not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )