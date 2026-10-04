-- Task 2: WHERE, ORDER BY & Aggregate Functions
-- Write SQL queries to:
-- 1. Filter records using the WHERE clause.
-- 2. Use comparison operators in conditions.
-- 3. Sort records using ORDER BY.
-- 4. Perform calculations using aggregate functions:
--    COUNT()
--    SUM()
--    AVG()
--    MIN()
--    MAX()
-- 5. Display the query and its output.

USE Week3DB;

SELECT
    Employee_ID,
    Employee_Name,
    Department,
    Salary,
    City
FROM Employees
WHERE Salary > 50000
ORDER BY Salary DESC;

SELECT
    COUNT(*) AS Total_Employees,
    SUM(Salary) AS Total_Salary,
    AVG(Salary) AS Average_Salary,
    MIN(Salary) AS Minimum_Salary,
    MAX(Salary) AS Maximum_Salary
FROM Employees;
