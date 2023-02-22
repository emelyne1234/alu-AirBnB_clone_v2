-- creating a database 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating a new user in local host
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- setting a password
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- granting all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
