CREATE TABLE
    IS601_Transactions(
        id int auto_increment PRIMARY KEY,
        account_src_id INT(12) NOT NULL,
        account_dest_id INT(12) NOT NULL,
        balance_change INT NOT NULL,
        transaction_type VARCHAR(20),
        memo TEXT,
        expected_total INT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (account_src_id) REFERENCES IS601_Accounts(id),
        FOREIGN KEY (account_dest_id) REFERENCES IS601_Accounts(id)
    )