# Write your MySQL query statement below
SELECT EmployeeUni.unique_id, Employees.name
FROM Employees LEFT JOIN EmployeeUni ON Employees.id=EmployeeUni.id