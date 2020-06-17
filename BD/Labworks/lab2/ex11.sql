USE northwind;

SELECT product_name, list_price
FROM products
WHERE list_price > (SELECT AVG(list_price) FROM products);