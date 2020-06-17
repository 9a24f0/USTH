USE northwind;

SELECT id, CONCAT(first_name, " ", last_name) AS full_name
FROM employees;