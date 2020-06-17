USE northwind;

DELETE FROM suppliers WHERE company = 'Habeco';

-- Deleting supplier will not affect the product tables --
-- If we want to delete product also --
-- DELETE FROM products WHERE product_code = 'TBTrucBach';