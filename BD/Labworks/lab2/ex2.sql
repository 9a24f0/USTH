USE northwind;

SELECT id, product_name, list_price FROM products
ORDER BY list_price DESC
LIMIT 4;