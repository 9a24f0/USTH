USE northwind;

SELECT order_id, order_date, company, SUM(unit_price * quantity * (1 - discount)) AS sub_total_value
FROM orders, order_details, customers
WHERE orders.id = order_details.order_id  AND customers.id = orders.customer_id AND order_date > '2006-03-24'
GROUP BY order_id
HAVING sub_total_value > 800;