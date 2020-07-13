USE northwind;

SELECT order_id, order_date, company, unit_price * quantity * (1 - discount) AS value
FROM orders, order_details, customers
WHERE orders.id = order_details.order_id  AND customers.id = orders.customer_id AND order_date > '2006-03-24';