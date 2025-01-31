WITH Reports AS (
    SELECT reports_to AS manager_id, 
           COUNT(*) AS reports_count, 
           ROUND(AVG(age)) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)
SELECT e.employee_id, e.name, r.reports_count, r.average_age
FROM Reports r
JOIN Employees e ON r.manager_id = e.employee_id
ORDER BY e.employee_id;