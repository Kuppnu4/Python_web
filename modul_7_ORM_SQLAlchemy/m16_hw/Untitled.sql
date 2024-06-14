SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    
SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    WHERE g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    
 
select MAX(grade_date)
from grades g 
join students s on s.id = g.student_id 
where g.subject_id = 1 and s.id = 1

select s.id , s.fullname, s.group_id , g.grade, g.grade_date 
from grades g 
join students s on g.student_id = s.id 
where g.subject_id = 2 and s.group_id  = 3 and g.grade_date = (
	select MAX(grade_date)
	from grades g 
	join students s on s.id = g.student_id 
	where g.subject_id = 2 and s.group_id  = 3
)




