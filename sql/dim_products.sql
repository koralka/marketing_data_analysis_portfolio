-- SQL Query to categorise products based on their price

SELECT 
    ProductID,  
    ProductName,  
    Price,  
	

    CASE -- Categorises the products into price categories: Low, Medium, or High
        WHEN Price < 50 THEN 'Low' 
        WHEN Price BETWEEN 50 AND 200 THEN 'Medium'  
        ELSE 'High'  
    END AS PriceCategory  -- Name the new column as PriceCategory

FROM 
    dbo.products;  
