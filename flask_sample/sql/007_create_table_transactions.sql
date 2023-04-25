CREATE TABLE
    IS601_Transactions(
        id int auto_increment PRIMARY KEY,
        account_src INT(12),
        account_dest INT(12),
        balance_change SMALLINT,
        transaction_type TEXT,
        memo TEXT,
        expected_total SMALLINT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )