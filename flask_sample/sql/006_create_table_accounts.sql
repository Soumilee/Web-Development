CREATE TABLE
    IS601_Accounts(
        id int auto_increment PRIMARY KEY,
        account_number BIGINT(20) unique,
        user_id INT,
        balance SMALLINT DEFAULT 0,
        account_type TEXT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )