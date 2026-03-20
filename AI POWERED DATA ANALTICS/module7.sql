CREATE DATABASE company_db;
USE company_db;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    joining_date DATE
);

INSERT INTO employees VALUES
(1, 'Amit', 'HR', 40000, '2022-01-10'),
(2, 'Neha', 'IT', 60000, '2021-03-15'),
(3, 'Raj', 'IT', 75000, '2020-07-20'),
(4, 'Priya', 'Finance', 50000, '2023-02-11'),
(5, 'Karan', 'HR', 45000, '2021-11-05');

select * from employees;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments VALUES
(101, 'HR', 'Hyderabad'),
(102, 'IT', 'Bangalore'),
(103, 'Finance', 'Mumbai');

select * from departments;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    emp_id INT,
    amount INT,
    order_date DATE,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

INSERT INTO orders VALUES
(201, 2, 5000, '2024-01-10'),
(202, 3, 7000, '2024-01-12'),
(203, 2, 3000, '2024-02-05'),
(204, 5, 4500, '2024-02-10'),
(205, 1, 2000, '2024-03-01');

select * from orders;

select * from employees ;
alter table employees add email varchar(100);

alter table employees  drop column email;

alter table employees  rename column department to dept_name;

CREATE TABLE orders1 (
    order_id INT PRIMARY KEY,
    emp_id INT,
    amount INT,
    order_date DATE,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

insert into orders1 select * from orders;
select * from orders1;

truncate table orders1;


-- Easy

-- Show all employees
select * from employees;

-- Get employees from IT department
select * from employees where department='IT';

-- Find employees with salary > 50000
select * from employees where salary>50000;

-- 🟡 Medium

-- Count employees in each department
SELECT department,count(*) from employees
group by department;

-- Find average salary per department
SELECT department,avg(salary) from employees
group by department;


-- Get highest salary employee
select name,salary from employees
order by salary desc
limit 1;

-- Find employees who joined after 2021
select * from employees where joining_date>'2021-12-31';


-- 🔴 Advanced (INTERVIEW LEVEL)

-- Join employees with departments
select * from employees e
join departments d on
e.department=d.dept_name;

-- Find total order amount per employee
select name,sum(amount) as Total_order_amt from employees e
join orders o on
e.emp_id=o.emp_id
group by name;

-- Get employee with highest total sales

-- Rank employees by salary
-- select name,rank(order by salary desc) from employees 

-- Find second highest salary
select max(salary) from employees
where salary < (select max(salary) from employees);


