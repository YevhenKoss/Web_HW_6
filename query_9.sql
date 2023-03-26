-- Знайти список курсів, які відвідує студент

SELECT s.fullname, d.name 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE s.id = 50
GROUP BY d.id