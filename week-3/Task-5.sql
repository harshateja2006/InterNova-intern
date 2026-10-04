-- Task 5: SQL Subqueries
-- Write SQL queries using subqueries to solve at least two problems.
-- 1. Find employees earning more than the average salary.
-- 2. Find employees earning more than the average salary of their department.
-- 3. Display the query and output.
USE Week3DB;

SELECT Employee_ID,
       Employee_Name,
       Department,
       Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);

SELECT Employee_ID,
       Employee_Name,
       Department,
       Salary
FROM Employees e
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
    WHERE Department = e.Department
);