# Write your MySQL query statement below
Select score,
DENSE_RANK() OVER (Order By score DESC) AS `rank`
From Scores