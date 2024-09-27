
CREATE DATABASE IF NOT EXISTS boss;

USE boss;

CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_name VARCHAR(255) NOT NULL,
    job_salary VARCHAR(50),
    experience VARCHAR(100),
    degree VARCHAR(100),
    company_name VARCHAR(255),
    city VARCHAR(100),
    area VARCHAR(100),
    job_skills TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


