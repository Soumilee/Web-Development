ALTER TABLE IS601_Users
ADD
    COLUMN username varchar(10) not null unique default (substring_index(email, '@', 1)) COMMENT 'Username field that defaults to the name of the email';
    COLUMN email varchar(60) not null unique;
    