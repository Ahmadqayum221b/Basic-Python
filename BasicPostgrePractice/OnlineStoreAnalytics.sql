--Online Store Analytics.
CREATE TABLE Customers(
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);
CREATE TABLE Products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT
);
CREATE TABLE Orders(
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customers(customer_id),
    product_id INT REFERENCES Products(product_id),
    quantity INT,
    order_date DATE
);

select * from Orders;
select * from customers;
select * from products;
--Which category generates the most revenue?
select p.category as Category,Sum(p.price * o.quantity) 
as TotalCategoryRevenue
from Products p join orders o on o.product_id = p.product_id
group by Category order by TotalCategoryRevenue DESC;
--Which city spends the most money?
select c.city as City,Sum(p.price * o.quantity) as Money from 
customers c join orders o on o.customer_id = c.customer_id
join Products p on p.product_id = o.product_id 
group by City Order by Money DESC;
--Top 10 Customers
SELECT
    c.customer_name,
    SUM(o.quantity * p.price) AS total_spent
FROM Orders o
JOIN Customers c
ON o.customer_id = c.customer_id
JOIN Products p
ON o.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 10;
--Now Add CTE.
--Find customers who spend above average.
WITH CustomerTotals AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(o.quantity * p.price) AS total_spent
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    JOIN Products p ON o.product_id = p.product_id
    GROUP BY c.customer_id, c.customer_name
),
CategoryTotals as (
	SELECT
        p.category,
        SUM(o.quantity * p.price) AS total_spent
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
    JOIN Products p ON o.product_id = p.product_id
    GROUP BY p.category
)

SELECT customer_name,total_spent
FROM CustomerTotals
WHERE total_spent > (SELECT AVG(total_spent) FROM CustomerTotals);

--Find categories generating above-average revenue.
select Category,total_spent from CategoryTotals
where total_spent > (SELECT AVG(total_spent) FROM CategoryTotals);