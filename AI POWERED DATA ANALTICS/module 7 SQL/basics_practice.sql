show databases;
use emp;
select * from departments;
select * from employees;

-- Select only name and salary-- 
select emp_name,salary from employees;

-- Filter employees from a specific city
select * from employees where city='hyderabad';

-- Sort employees by salary (descending)
select * from employees 
order by salary desc;

--  specific columns
select job_title from employees;

-- WHERE conditions
select * from employees where age>=30;

-- ORDER BY sorting
select emp_name from employees 
order by emp_name asc;
select emp_name from employees 
order by emp_name desc;

-- LIMIT top N rows
select * from employees 
order by salary desc
limit 2; 

-- AND, OR, NOT
select * from employees where city='hyderabad' and age>=20 ;
select * from employees where city='hyderabad' or age>=30 ;
select * from employees where city not in ('Mumbai');

-- IN, BETWEEN
select * from employees where salary between 40000 and 50000;
select * from employees where city in ('Mumbai','Ahmedabad');

-- LIKE
select emp_name from employees where emp_name like '%a';
select emp_name from employees where emp_name like 'k%';
select emp_name from employees where emp_name like '%a%';

-- IS NULL
delete from employees WHERE city IS NULL;

-- Aggregate Functions
select count(*) from employees;
select max(salary) from employees;
select min(salary) from employees;
select avg(salary) from employees;
select sum(salary) from employees;
select department,avg(salary) from employees
group by department;

-- GROUP BY + HAVING
select job_title,avg(salary) from employees
group by job_title;

SELECT department,COUNT(*) FROM employees
GROUP BY department
HAVING COUNT(*) > 1;

-- Date & String Functions
-- YEAR(), MONTH(), DAY()

-- CONCAT(), UPPER(), LOWER(), LENGTH()
select CONCAT(emp_name,emp_id) as empcode from employees;
select UPPER(emp_name)  from employees;
select lower(emp_name)  from employees;
select length(emp_name)  from employees;

-- JOINS INNER,LEFT,RIT,OUTER
select e.emp_name,d.department,d.dept_id,d.location from employees e
left join departments d
on 
e.department =d.department;

-- Subqueries-- 
select * from employees where salary > (select avg(salary) from employees);

-- CTEs (WITH Clause) common table expression
with dep_avg as (
select department,avg(salary) as avg_salary from employees 
group by department
)

select * from dep_avg where avg_salary >= 60000;

-- Window Functions
select emp_name,salary,rank() over(order by salary desc) as rank_pos from employees;








