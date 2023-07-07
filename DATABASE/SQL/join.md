# JOIN

## INNER JOIN

```
SELECT * FROM dept INNER JOIN employee ON dept.id = employee.dept_id;
SELECT employee.id, employee.name, dept.name FROM employee INNER JOIN dept ON employee.dept_id == dept.id;
```
