CREATE DATABASE IF NOT EXISTS devopsdb;

USE devopsdb;

CREATE TABLE IF NOT EXISTS visits (
  id INT AUTO_INCREMENT PRIMARY KEY,
  message VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO visits (message) VALUES ('MySQL persistent storage is working');
