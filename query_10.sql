-- Список курсів, які певному студенту читає певний викладач

SELECT s.fullname, d.name, t.fullname 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 1 AND t.id = 1
GROUP BY d.id