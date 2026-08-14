# Write your MySQL query statement below
select max(num) AS num
from (
    select num
    from MYNumbers
    Group by num
    having count(num) = 1
) AS unique_numbers;
