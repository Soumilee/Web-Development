INSERT INTO
    `IS601_Users` (
        id,
        username,
        email,
        password,
        first_name,
        last_name
    )
VALUES (-1, 'Admin', 'superuser@gmail.com', 'abcd','Super','User') ON DUPLICATE KEY
UPDATE username = username;