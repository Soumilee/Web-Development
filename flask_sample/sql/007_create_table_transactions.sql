CREATE TABLE
    IS601_Transactions(
        id int auto_increment PRIMARY KEY,
        user_id INT NOT NULL,
        account_src_id INT(12) NOT NULL,
        account_dest_id INT(12) NOT NULL,
        balance_change SMALLINT NOT NULL,
        transaction_type TEXT,
        memo TEXT,
        expected_total SMALLINT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )