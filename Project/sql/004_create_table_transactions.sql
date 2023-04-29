CREATE TABLE
    IS601_Transactions(
        transaction_id INT AUTO_INCREMENT PRIMARY KEY, 
        account_src INT not null UNIQUE, 
        account_dest INT not null UNIQUE, 
        balance_change SMALLINT, 
        transaction_type TEXT, 
        memo TEXT, 
        expected_total INT, 
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )