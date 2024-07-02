-- Crear la base de datos 'test_db'
CREATE DATABASE IF NOT EXISTS test_db;

-- Usar la base de datos 'test_db'
USE test_db;

-- Crear la tabla 'users'
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);
