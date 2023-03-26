-- Знайти середній бал, який ставить певний викладач зі своїх предметів

SELECT t.fullname, d.name, ROUND(AVG(g.grade), 3) AS avg_grade
FROM grades g
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 5
GROUP BY d.id
ORDER BY avg_grade DESC;