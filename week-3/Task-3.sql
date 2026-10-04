-- Task 3: GROUP BY & HAVING
-- Using a suitable dataset:
-- 1. Group records using GROUP BY.
-- 2. Calculate aggregate values for each group.
-- 3. Use the HAVING clause to filter grouped results.
-- 4. Display and explain the results.

USE Week3DB;

SELECT Department,
       COUNT(*) AS Employee_Count,
       SUM(Salary) AS Total_Salary,
       AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department;

SELECT Department,
       COUNT(*) AS Employee_Count,
       SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department
HAVING SUM(Salary) > 50000;