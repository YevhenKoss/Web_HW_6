-- Знайти середній бал у групах з певного предмета

SELECT gr.name, d.name, ROUND(AVG(g.grade), 3) AS avg_grade
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 1
GROUP BY gr.id, d.id 
ORDER BY avg_grade DESC;