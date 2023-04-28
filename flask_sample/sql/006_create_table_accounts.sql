CREATE TABLE
    IS601_Accounts(
        id int auto_increment PRIMARY KEY,
        account_number VARCHAR(12) unique,
        user_id INT,
        balance INT DEFAULT 0,
        account_type VARCHAR(20),
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )
