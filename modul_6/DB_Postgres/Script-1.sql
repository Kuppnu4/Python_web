select 
	s.id,
	s.fullname,
	round(AVG(g.grade), 2) as average_grade
from students s 
join grades g on s.id = g.student_id 
group by s.id
order by average_grade desc 
limit 5

SELECT 
	s.id, 
	s.fullname, 
	round(AVG(g.grade), 2) AS average_grade
FROM grades g
join students s on s.id = g.student_id   
WHERE g.subject_id = 1
GROUP BY s.id 
ORDER BY average_grade DESC
LIMIT 3;
