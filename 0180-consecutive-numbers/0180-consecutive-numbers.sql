Select distinct num as ConsecutiveNums
from (
    select num,
    LEAD(num, 1) over (Order by id) as next_num,
    LEAD(num, 2) over (Order by id) as next_next_num
    From Logs
) AS temp
where num = next_num AND num = next_next_num