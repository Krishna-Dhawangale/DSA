# Write your MySQL query statement below
Select d.name AS Department, e.name AS Employee, e.salary AS Salary
From Employee e
Join Department d ON e.departmentId = d.id
Where (e.departmentId, e.salary) IN (
    Select departmentId, max(salary)
    From Employee
    Group By departmentId
)