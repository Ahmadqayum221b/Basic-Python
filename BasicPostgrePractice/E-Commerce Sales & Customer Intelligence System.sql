--E-Commerce Sales & Customer Intelligence System
create table customers (
  customer_id int primary key,
  age int,
  country varchar(50),
  signup_date date
);
create table products (
	product_id int primary key,
	category varchar(50),
	price float
);
create table orders (
	order_id int primary key,
	customer_id int references customers(customer_id),
	order_date date
);
create table order_items (
	order_id int references orders(order_id),
	product_id int references products(product_id),
	quantity int,
	unit_price float,
	total_price float
);

select * from orders;
select * from products;
select * from customers;
select * from order_items;

--Total Revenue Generated.
select SUM(oi.total_price) as TotalPrice,p.category as Category, 
Rank() over(
order by SUM(oi.total_price) DESC
) as RankNumber
from products p join order_items oi
on oi.product_id = p.product_id 
group by Category;

--Which month generated the highest revenue.
SELECT 
    TO_CHAR(o.order_date, 'YYYY-MM') AS OrderMonth,
    SUM(oi.total_price) AS TotalPrice 
FROM orders o 
JOIN order_items oi ON oi.order_id = o.order_id 
GROUP BY TO_CHAR(o.order_date, 'YYYY-MM') 
ORDER BY TotalPrice DESC LIMIT 1;
--which month generated the lowest revenue.
SELECT 
    TO_CHAR(o.order_date, 'YYYY-MM') AS OrderMonth,
    SUM(oi.total_price) AS TotalPrice 
FROM orders o 
JOIN order_items oi ON oi.order_id = o.order_id 
GROUP BY TO_CHAR(o.order_date, 'YYYY-MM') 
ORDER BY TotalPrice ASC LIMIT 1;

--Which products generated high revenue despite low sales volume?
With HighRevenueProductGenerate as (
select p.category as Category,SUM(oi.quantity) as TotalQuantity,
SUM(oi.quantity * p.price) as TotalPrice from products p
join order_items oi on oi.product_id = p.product_id
GROUP BY p.product_id
)
select Category,TotalQuantity,TotalPrice from HighRevenueProductGenerate
order by
TotalQuantity ASC,TotalPrice DESC;
