-- Знайти оцінки студентів у окремій групі з певного предмета

SELECT gr.name, s.fullname,  d.name, g.grade
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE d.id = 10 AND gr.id = 1
ORDER BY s.fullname;