INSERT INTO IS601_Accounts(
    id, account_number, user_id, balance, account_type) 
    VALUES (-1,'000000000000',-1,0,'world') ON DUPLICATE KEY
UPDATE account_number = account_number;