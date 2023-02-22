-- creating a database 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating a new user in local host
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- setting a password
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- granting all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
