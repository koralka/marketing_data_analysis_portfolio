-- Common Table Expression (CTE) to identify and tag duplicate records

WITH DuplicateRecords AS (
    SELECT 
        JourneyID,  
        CustomerID,  
        ProductID,  
        VisitDate,  
        Stage, 
        Action,  
        Duration, 
        -- Use ROW_NUMBER() to assign a unique row number to each record within the partition defined below
        ROW_NUMBER() OVER (
            -- PARTITION BY - groups the rows based on the specified columns that should be unique
            PARTITION BY CustomerID, ProductID, VisitDate, Stage, Action  
            ORDER BY JourneyID  
        ) AS row_num  -- new column 'row_num' that numbers each row within its partition
    FROM 
        dbo.customer_journey  
)

-- Select all records from the CTE where row_num > 1 - which indicates duplicate entries
    
SELECT *
FROM DuplicateRecords
-- WHERE row_num > 1  -- filter out the first occurrence (row_num = 1) and only show the duplicates (row_num > 1)
ORDER BY JourneyID

-- Outer query selects the final cleaned and standardised data
    
SELECT 
    JourneyID,  
    CustomerID, 
    ProductID,  
    VisitDate,  
    Stage,  
    Action,  
    COALESCE(Duration, avg_duration) AS Duration  -- replace missing durations with the average duration for the corresponding date
FROM 
    (
        -- Subquery to process and clean the data
        SELECT 
            JourneyID,  
            CustomerID,
            ProductID,  
            VisitDate, 
            UPPER(Stage) AS Stage, 
            Action,  
            Duration,  
            AVG(Duration) OVER (PARTITION BY VisitDate) AS avg_duration,  
            ROW_NUMBER() OVER (
                PARTITION BY CustomerID, ProductID, VisitDate, UPPER(Stage), Action  -- group by these columns to identify duplicate records
                ORDER BY JourneyID  -- order by JourneyID to keep the first occurrence of each duplicate
            ) AS row_num  
        FROM 
            dbo.customer_journey  
    ) AS subquery 
WHERE 
    row_num = 1;  
