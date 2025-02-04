-- Dropping the table if it already exists to avoid conflicts
DROP TABLE IF EXISTS employees;

-- Creating the table if it does not exist
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
  	state VARCHAR(100),
    city VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- Inserting data into the table
INSERT INTO employees (employee_id, first_name, last_name, email, state, city, salary)
VALUES 
    (1, 'John', 'Doe', 'james.madison@hi.com', 'NY', 'Fairport', 1000.00),
    (2, 'Jane', 'Smith', 'john.mclean@hi.com', 'NY', 'New York', 2000.00),
    (3, 'Bob', 'Johnson', 'james.buchanan@hi.com', 'US', 'New York', 3000.00);

-- Selecting all the data from the table
-- SELECT first_name FROM employees;
-- SELECT * FROM employees;
-- SELECT last_name FROM employees;
-- SELECT * FROM employees ORDER BY first_name DESC;
-- SELECT * FROM employees;

-- select all the employees from NY
-- SELECT * FROM employees WHERE state = 'NY';

-- select all the employees from US
-- SELECT * FROM employees WHERE state = 'US';

-- select all the employees from NY and city fair port
-- SELECT * FROM employees WHERE state = 'NY' AND city = 'Fairport';

-- SELECT * from employees WHERE first_name like 'B%';
-- select * FROM employees WHERE first_name LIKE 'J%'

SELECT state, sum(salary) as total FROM employees GROUP BY first_name;