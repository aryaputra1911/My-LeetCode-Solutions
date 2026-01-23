-- Write your PostgreSQL query statement below
SELECT s.score, (
    SELECT count(Distinct s1.score) 
    FROM scores s1 
    WHERE s1.score >= s.score
) as rank
FROM scores s
order by score desc