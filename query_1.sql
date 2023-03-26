-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів

SELECT s.fullname, ROUND(AVG(g.grade), 3) AS avg_grade
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id 
GROUP BY s.id  
ORDER BY avg_grade DESC 
LIMIT 5;
