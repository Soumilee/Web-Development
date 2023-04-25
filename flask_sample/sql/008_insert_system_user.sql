INSERT INTO
    `IS601_Users` (
        id,
        username,
        email,
        password
    )
VALUES (-1, 'Admin', 'superuser@gmail.com', 'abcd') ON DUPLICATE KEY
UPDATE username = username;