-- Create database
CREATE DATABASE sst;
USE sst;

-- Create Employee table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    Email VARCHAR(100),
    Salary DECIMAL(10, 2),
    DepartmentID INT  
);

-- Create Department table
CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

-- Insert into Department
INSERT INTO Department (DepartmentID, DepartmentName) VALUES
(1, 'Human Resources'),
(2, 'Engineering'),
(3, 'Finance'),
(4, 'Marketing');

-- Insert into Employee
INSERT INTO Employee (EmployeeID, FirstName, LastName, Gender, Email, Salary, DepartmentID) VALUES
(201, 'Alice', 'Johnson', 'Female', 'alice.j@example.com', 58000, 2),
(202, 'Bob', 'Williams', 'Male', 'bob.w@example.com', 52000, 2),
(203, 'Catherine', 'Lee', 'Female', 'catherine.l@example.com', 61000, 1),
(204, 'David', 'Taylor', 'Male', 'david.t@example.com', 56000, 3),
(205, 'Eva', 'Martinez', 'Female', 'eva.m@example.com', 60000, 4);

-- View: all employee data
CREATE VIEW vwAllEmployee AS
SELECT * FROM Employee;

-- View: limited employee info
CREATE VIEW vwAllEmployeeSalary AS
SELECT EmployeeID, FirstName, Gender, Salary FROM Employee;

-- View: Employee + Department info
CREATE VIEW vwEmployeeDepartmentView AS
SELECT
    e.EmployeeID,
    CONCAT(e.FirstName, ' ', e.LastName) AS FullName,
    e.Gender,
    e.Salary,
    (e.Salary * 12) AS AnnualSalary,
    d.DepartmentName,
    e.DepartmentID
FROM Employee e
JOIN Department d ON e.DepartmentID = d.DepartmentID
WHERE e.Salary > 40000;

select * from vwemployeedepartmentview;

-- View: HR Employees
CREATE VIEW vwHREmployees
AS
SELECT * FROM Employee WHERE DepartmentID = 1
WITH CHECK OPTION;

-- Alter encrypted view (you can't use sp_helptext after encryption)
ALTER VIEW vwHREmployees
WITH ENCRYPTION
AS
SELECT * FROM Employee WHERE DepartmentID = 2
WITH CHECK OPTION;

-- View using another view
CREATE VIEW vwITEmployee AS
SELECT FullName, Gender
FROM vwEmployeeDepartmentView
WHERE DepartmentID = 1;

-- CTE
WITH HighSalaryCTE AS (
    SELECT Name, Department, Salary
    FROM Employee
    WHERE Salary >= 40000
)
SELECT * FROM HighSalaryCTE;


SELECT 
    e.EmployeeID,
    CONCAT(e.FirstName, ' ', e.LastName) AS Name,
    e.Gender,
    e.Salary,
    d.DepartmentName,
    s.TotalEmployees,
    s.TotalSalary,
    s.MinSalary,
    s.MaxSalary,
    s.AverageSalary
FROM Employee e
INNER JOIN Department d ON e.DepartmentID = d.DepartmentID
INNER JOIN (
    SELECT 
        DepartmentID,
        COUNT(*) AS TotalEmployees,
        SUM(Salary) AS TotalSalary,
        MIN(Salary) AS MinSalary,
        MAX(Salary) AS MaxSalary,
        AVG(Salary) AS AverageSalary
    FROM Employee
    GROUP BY DepartmentID
) s ON e.DepartmentID = s.DepartmentID;



SELECT e.EmployeeID,
    CONCAT(e.FirstName, ' ', e.LastName) AS Name,
    e.Salary,
    d.DepartmentName AS Department,
    COUNT(*) OVER(PARTITION BY e.DepartmentID) AS DepartmentTotals,
    SUM(e.Salary) OVER(PARTITION BY e.DepartmentID) AS TotalSalary,
    MIN(e.Salary) OVER(PARTITION BY e.DepartmentID) AS MinSalary,
    MAX(e.Salary) OVER(PARTITION BY e.DepartmentID) AS MaxSalary,
    AVG(e.Salary) OVER(PARTITION BY e.DepartmentID) AS AverageSalary
FROM Employee e
JOIN Department d ON e.DepartmentID = d.DepartmentID;

DELETE FROM Employee;


truncate table employee
select * from Employee


CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10,2)
);


INSERT INTO Employee VALUES
(1, 'James', 'IT', 15000),
(2, 'Smith', 'IT', 35000),
(3, 'Rasol', 'HR', 15000),
(4, 'Rakesh', 'Payroll', 35000),
(5, 'Pam', 'IT', 42000),
(6, 'Stokes', 'HR', 15000),
(7, 'Taylor', 'HR', 67000),
(8, 'Preety', 'Payroll', 67000),
(9, 'Priyanka', 'Payroll', 55000),
(10, 'Anurag', 'Payroll', 15000),
(11, 'Marshal', 'HR', 55000),
(12, 'David', 'IT', 96000);

SELECT EmployeeID,Name,Department,Salary,
ROW_NUMBER() OVER(PARTITION BY Department ORDER BY Name)
AS RowNumber From Employee

SELECT EmployeeID,Name,Department,Salary,
ROW_NUMBER() OVER(ORDER BY Name)
AS RowNumber From Employee


Drop table Employee

CREATE TABLE [dbo].[Employee](
	[Id] [int] NOT NULL,
	[Name] [varchar](50) NULL,
	[Department] [varchar](10) NULL,
	[Salary] [int] NULL,
	)
TRUNCATE TABLE Employee;

INSERT INTO Employee VALUES
(1, 'James', 'IT', 15000),
(1, 'James', 'IT', 15000),
(2, 'Rasol', 'HR', 15000),
(2, 'Rasol', 'HR', 15000),
(2, 'Rasol', 'HR', 15000),
(3, 'Stokes', 'HR', 15000),
(3, 'Stokes', 'HR', 15000),
(3, 'Stokes', 'HR', 15000),
(3, 'Stokes', 'HR', 15000);

Select * from Employee;


WITH DeleteDuplicateCTE AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY Name, Department, Salary ORDER BY ID) AS RowNumber
    FROM Employee
)
DELETE FROM Employee
WHERE ID IN (
    SELECT ID FROM DeleteDuplicateCTE WHERE RowNumber = 1
);

select * from Employee;
TRUNCATE TABLE Employee

INSERT INTO Employee VALUES
(1, 'James', 'IT', 80000),
(2, 'Taylor', 'IT', 80000),
(3, 'Pamela', 'HR', 50000),
(4, 'Sara', 'HR', 40000),
(5, 'David', 'IT', 35000),
(6, 'Smith', 'HR', 65000),
(7, 'Ben', 'HR', 65000),
(8, 'Stokes', 'IT', 45000),
(9, 'Taylor', 'IT', 70000),
(10, 'John', 'IT', 68000);

SELECT Name,Department,Salary,
DENSE_RANK() OVER(PARTITION BY Department ORDER BY SALARY desc) AS [Rank]
FROM Employee

WITH EmployeeCTE AS (
    SELECT Salary, RANK() OVER (ORDER BY Salary DESC) AS Rank_Salry
    FROM Employee
)
SELECT TOP 1 Salary FROM EmployeeCTE WHERE Rank_Salry = 2;

WITH EmployeeCTE AS (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS DenseRank_Salry
    FROM Employee
)
SELECT TOP 1 Salary FROM EmployeeCTE WHERE DenseRank_Salry = 2;

WITH EmployeeCTE AS (
    SELECT Salary, Department,
           DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS Salary_Rank
    FROM Employee
)
SELECT TOP 1 Salary 
FROM EmployeeCTE 
WHERE Salary_Rank = 3 AND Department = 'IT';