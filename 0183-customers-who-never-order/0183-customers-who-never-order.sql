# Write your MySQL query statement below
SELECT cmp.name AS Customers
FROM Customers cmp
LEFT JOIN Orders ord ON cmp.id = ord.CustomerID
WHERE ord.id IS NULL