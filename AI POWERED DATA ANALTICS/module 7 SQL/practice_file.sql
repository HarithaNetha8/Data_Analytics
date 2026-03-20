create database business_dataset;
 use business_dataset;
 CREATE TABLE customers (
customer_id INT,
name VARCHAR(50),
city VARCHAR(50),
registered_date DATE
);
INSERT INTO customers VALUES
(1,'Rahul','Mumbai','2023-01-15'),
(2,'Anita','Delhi','2022-11-20'),
(3,'Suresh','Hyderabad','2024-02-10'),
(4,'Priya','Mumbai','2023-05-12'),
(5,'Arjun','Bangalore','2024-01-01'),
(6,'Meena','Delhi','2022-12-25'),
(7,'Kiran','Hyderabad','2023-03-18'),
(8,'Ravi','Chennai','2024-04-10');
 
CREATE TABLE products (
product_id INT,
product_name VARCHAR(50),
price INT
);
INSERT INTO products VALUES
(101,'Laptop',70000),
(102,'Mobile',20000),
(103,'Headphones',2000),
(104,'Keyboard',1500),
(105,'Mouse',800),
(106,'Monitor',12000),
(107,'Tablet',25000),
(108,'Printer',9000);
 select * from products;
 
CREATE TABLE orders (
order_id INT,
customer_id INT,
product_id INT,
order_amount INT,
order_date DATE
);
INSERT INTO orders VALUES
(1,1,101,70000,'2024-01-10'),
(2,2,102,20000,'2024-01-15'),
(3,1,103,2000,'2024-02-01'),
(4,3,104,1500,'2024-02-10'),
(5,4,101,70000,'2024-02-15'),
(6,5,105,800,'2024-03-01'),
(7,6,106,12000,'2024-03-05'),
(8,2,103,2000,'2024-03-10'),
(9,3,107,25000,'2024-03-20'),
(10,7,108,9000,'2024-04-01'),
(11,1,105,800,'2024-04-03'),
(12,8,102,20000,'2024-04-05');

CREATE TABLE employes (
employee_id INT,
name VARCHAR(50),
department VARCHAR(50),
salary INT
);
INSERT INTO employes VALUES
(1,'Ramesh','Sales',50000),
(2,'Sneha','HR',45000),
(3,'Ajay','IT',70000),
(4,'Kavya','Sales',52000),
(5,'Manoj','IT',75000),
(6,'Divya','HR',48000),
(7,'Vikram','Finance',60000),
(8,'Neha','Sales',53000);

-- 1 Find customers from Hyderabad
select * from customers where city='Hyderabad';

-- 2 Find products above thousand
select * from products where price>1000;
 
-- 3 Find employees older than 30
select * from employees
where age>=30;

-- 4 Find orders between ₹5000–₹20000
select * from products
where price between 5000 and 20000;

-- 5 Find customers from Delhi or Mumbai
select * from customers
where city in('Delhi','Mumbai');

-- 6 Find products not equal to ₹1000
select * from products
where price>=1000;

-- 7 Find customers whose name starts with 'A'
select * from employes
where name like 'A%';

-- 8 Find orders after 2024
select * from orders
where order_date>'2024-12-31';

-- 9 Find customers whose phone is NULL
select * from customers
where phone is null;

-- 10 Find distinct products
select distinct(product_name) from products;

-- Find customers from Mumbai
select * from customers
where city='Mumbai';

-- Find orders above ₹20000
select * from orders
where order_amount>20000;

-- Find employees in Sales department
select * from employes
 where department ='Sales';

-- -GROUP 
-- -- Count customers per city
select city,count(name) from customers
group by city;

select count(*) from customers;

-- -- Total orders per customer
select c.name,sum(order_amount) as Total_orders from customers c
join orders o on 
c.customer_id= o.customer_id
group by name;

-- -- Total sales per product
select product_name,sum(order_amount) as total_sales from products p
join orders o on
p.product_id=o.product_id
group by product_name;

-- -- Average salary per department
select department,avg(salary) from employes 
group by department;

-- -- Maximum salary per department
select department,max(salary) from employes 
group by department;

-- HAVING
-- Customers with more than 1 order
select customer_id,count(order_id) from orders
group by customer_id
having count(*)>1;

-- Departments with average salary > 50000
select department,avg(salary) from employes
group by department
having avg(salary)>50000;

-- Products with total sales > 30000
select product_name,sum(order_amount) as total_sales from products p
join orders o on
p.product_id=o.product_id
group by product_name
having sum(order_amount) > 30000;

-- Cities with more than 2 customers
select city,count(*) from customers
group by city
having count(*)>2;

-- Customers spending more than 50000
select name, sum(order_amount) from customers c
join orders o on 
c.customer_id=o.customer_id
group by name
having sum(order_amount) > 50000;




