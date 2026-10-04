-- Task 4: SQL Joins
-- Create or use at least two related tables and perform:
-- 1. INNER JOIN
-- 2. LEFT JOIN
-- 3. RIGHT JOIN
-- 4. Use a common column to join the tables.
-- 5. Display the results.
-- 6. Briefly explain the purpose of each JOIN used.

USE Week3DB;

CREATE TABLE Departments (
    Department_ID INT PRIMARY KEY,
    Department VARCHAR(30),
    Manager VARCHAR(50)
);
INSERT INTO Departments VALUES
(1, 'IT', 'Ramesh'),
(2, 'HR', 'Lakshmi'),
(3, 'Finance', 'Suresh'),
(4, 'Sales', 'Anita');

SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Employees.Salary,
    Departments.Manager
FROM Employees
INNER JOIN Departments
ON Employees.Department = Departments.Department;

SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Employees.Salary,
    Departments.Manager
FROM Employees
LEFT JOIN Departments
ON Employees.Department = Departments.Department;

SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Employees.Salary,
    Departments.Manager
FROM Employees
RIGHT JOIN Departments
ON Employees.Department = Departments.Department;