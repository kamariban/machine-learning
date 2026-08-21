USE Company_DB;

SELECT * FROM employee_demographics;

SELECT * FROM employee_salary;

SELECT * FROM departments;

-- 1
SELECT first_name, last_name, age
FROM employee_demographics;

-- 2
SELECT first_name, last_name, age
FROM employee_demographics
WHERE age > 40;

-- 3
SELECT *
FROM employee_salary
ORDER BY salary DESC
LIMIT 3;

-- 4
SELECT AVG(salary)
FROM employee_salary;

-- 5
SELECT occupation, AVG(salary)
FROM employee_salary
GROUP BY occupation;

-- 6 
SELECT employee_id, first_name, last_name, occupation, salary, employee_salary.dept_id, dept_name
FROM employee_salary
INNER JOIN departments ON employee_salary.dept_id = departments.dept_id;

-- 7 
SELECT employee_salary.dept_id, AVG(salary), dept_name
FROM employee_salary
INNER JOIN departments ON employee_salary.dept_id = departments.dept_id
GROUP BY dept_id
HAVING AVG(salary) > 70000;


-- HARDER
-- 1
SELECT first_name, last_name, dept_name
FROM employee_salary
INNER JOIN departments ON employee_salary.dept_id = departments.dept_id
WHERE dept_name = 'Administration';

-- 2 
SELECT first_name, last_name, salary, dept_name
FROM employee_salary
INNER JOIN departments ON employee_salary.dept_id = departments.dept_id
WHERE salary >= 55000 AND salary <= 80000;

-- 3
SELECT occupation, SUM(salary) 
FROM employee_salary
GROUP BY occupation;

-- 4 
SELECT occupation, COUNT(occupation)
FROM employee_salary
GROUP BY occupation;


-- 5 
SELECT AVG(age), employee_salary.dept_id, departments.dept_name
FROM employee_demographics
LEFT OUTER JOIN employee_salary ON employee_salary.employee_id = employee_demographics.employee_id
INNER JOIN departments ON employee_salary.dept_id = departments.dept_id
GROUP BY departments.dept_id;


