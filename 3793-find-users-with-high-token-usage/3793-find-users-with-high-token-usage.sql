# Write your MySQL query statement below
select user_id, Count(prompt) as prompt_count, ROUND(AVG(tokens),2) as avg_tokens
from prompts
group by user_id
having count(prompt) >= 3 and MAX(tokens) > AVG(tokens) 
order by avg_tokens DESC, user_id ASC 