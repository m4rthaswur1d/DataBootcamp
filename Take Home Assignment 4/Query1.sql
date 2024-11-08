-- Creating the SALES table
CREATE TABLE SALES (
    Date DATE,
    Order_id INT,
    Item_id INT,
    Customer_id INT,
    Quantity INT,
    Revenue DECIMAL(10, 2)
);

-- Inserting data into SALES table
INSERT INTO SALES (Date, Order_id, Item_id, Customer_id, Quantity, Revenue) VALUES
('2023-03-18', 1001, 201, 301, 2, 50.00),
('2023-03-18', 1002, 202, 302, 1, 20.00),
('2023-01-15', 1003, 203, 303, 3, 90.00),
('2023-01-20', 1004, 204, 304, 1, 25.00),
('2022-12-30', 1005, 201, 305, 2, 100.00),
('2023-03-18', 1006, 202, 306, 1, 20.00), 
('2022-11-10', 1007, 205, 307, 1, 30.00);

-- Creating the ITEMS table
CREATE TABLE ITEMS (
    Item_id INT,
    Item_name VARCHAR(50),
    Price DECIMAL(10, 2),
    Department VARCHAR(50)
);

-- Inserting data into ITEMS table
INSERT INTO ITEMS (Item_id, Item_name, Price, Department) VALUES
(201, 'Widget A', 25.00, 'Electronics'),
(202, 'Widget B', 20.00, 'Home Goods'),
(203, 'Widget C', 30.00, 'Outdoors'),
(204, 'Widget D', 25.00, 'Garden'),
(205, 'Widget E', 30.00, 'Electronics');

-- Creating the CUSTOMERS table
CREATE TABLE CUSTOMERS (
    Customer_id INT,
    First_name VARCHAR(50),
    Last_name VARCHAR(50),
    Address VARCHAR(100)
);

-- Inserting data into CUSTOMERS table
INSERT INTO CUSTOMERS (Customer_id, First_name, Last_name, Address) VALUES
(301, 'John', 'Doe', '123 Maple St, NY'),
(302, 'Alice', 'Smith', '456 Oak St, CA'),
(303, 'Bob', 'Johnson', '789 Pine St, TX'),
(304, 'Jane', 'Doe', '321 Birch St, FL'),
(305, 'Carol', 'Williams', '654 Cedar St, WA'),
(306, 'John', 'Doe', '987 Elm St, NY'),
(307, 'Eve', 'Davis', '654 Cedar St, WA');
