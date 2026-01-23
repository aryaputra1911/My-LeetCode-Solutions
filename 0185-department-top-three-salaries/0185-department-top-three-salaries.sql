-- Write your PostgreSQL query statement below
with summary as (select d.name as department,e.name as employee,e.salary as salary,dense_rank() over(partition by e.departmentid order by salary desc)as rank from employee as e join department as d on e.departmentid = d.id)
select department,employee,salary from summary where rank <= 3
