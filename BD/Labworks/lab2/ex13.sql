USE northwind;

INSERT INTO products(product_code, supplier_ids, list_price, discontinued, category)
VALUES ('TBTrucBach', 
        (SELECT id FROM suppliers WHERE company = 'Habeco'),
        22, 0, 'Beverages');