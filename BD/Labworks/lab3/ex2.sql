USE northwind;

SELECT products.id, order_id, product_code, unit_price, quantity, unit_price * quantity * (1 - discount) AS value
FROM products, order_details
WHERE products.id = product_id AND order_id = 31;