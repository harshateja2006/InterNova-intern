-- Task 1: Introduction to Databases & SELECT Statement Using a sample database/table:
-- 1. Understand the basic concept of databases.
-- 2. Create or use a sample table such as Students, Employees, or Sales.
-- 3. Write SQL queries to display all records.
-- 4. Select specific columns using SELECT.
-- 5. Use column aliases where appropriate.

CREATE DATABASE Week3DB;

USE Week3DB;

CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY,
    Employee_Name VARCHAR(50),
    Department VARCHAR(30),
    Salary INT,
    City VARCHAR(30)
);

INSERT INTO Employees VALUES
(101, 'Rahul', 'IT', 55000, 'Hyderabad'),
(102, 'Priya', 'HR', 45000, 'Chennai'),
(103, 'Arjun', 'IT', 65000, 'Bengaluru'),
(104, 'Sneha', 'Finance', 50000, 'Visakhapatnam'),
(105, 'Kiran', 'IT', 70000, 'Hyderabad');

SELECT * FROM Employees;

SELECT Employee_Name, Department, Salary
FROM Employees;

SELECT Employee_Name AS Name,
       Salary AS Monthly_Salary
FROM Employees;