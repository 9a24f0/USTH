USE northwind;

SELECT CONCAT(first_name, " ", last_name) AS full_name
FROM employees
WHERE first_name LIKE 'A%' OR last_name LIKE 'A%';