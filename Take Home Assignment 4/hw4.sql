-- Question 1
SELECT COUNT(*) AS Total_Orders
FROM SALES
JOIN CUSTOMERS ON SALES.Customer_id = CUSTOMERS.Customer_id
WHERE SALES.Date = '2023-03-18'
  AND CUSTOMERS.First_name = 'John'
  AND CUSTOMERS.Last_name = 'Doe';

-- Question 2
SELECT COUNT(DISTINCT SALES.Customer_id) AS Total_Customers,
       AVG(ITEMS.Price) AS Average_Amount_Spent
FROM SALES
JOIN CUSTOMERS ON SALES.Customer_id = CUSTOMERS.Customer_id
JOIN ITEMS ON SALES.Item_id = ITEMS.Item_id
WHERE MONTH(SALES.Date) = 1 AND YEAR(SALES.Date) = 2023;

-- Question 3
SELECT I.department, SUM(S.Revenue) AS total_revenue
FROM SALES S
JOIN ITEMS I ON S.Item_id = I.Item_id
WHERE YEAR(S.Date) = 2022
GROUP BY I.department
HAVING total_revenue < 600;

-- Question 4
SELECT MAX(total_revenue) AS most_revenue,
       MIN(total_revenue) AS least_revenue
FROM (
    SELECT Order_id, SUM(Revenue) AS total_revenue
    FROM SALES
    GROUP BY Order_id
) AS order_totals;

-- Question 5
WITH lucrative_order AS (
    SELECT Order_id
    FROM SALES
    GROUP BY Order_id
    ORDER BY SUM(Revenue) DESC
    LIMIT 1
)
SELECT S.Order_id, S.Item_id, I.Item_name, S.Quantity, S.Revenue
FROM SALES S
JOIN ITEMS I ON S.Item_id = I.Item_id
JOIN lucrative_order L ON S.Order_id = L.Order_id;
