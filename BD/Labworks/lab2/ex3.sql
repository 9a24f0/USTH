USE northwind;

SELECT id, product_name, list_price FROM products
WHERE list_price BETWEEN 15 AND 25;