SELECT id, name as fullname
FROM contacts as c 
WHERE favorite != TRUE 
ORDER BY fullname 
LIMIT 5;

SELECT name, email
FROM users u  
WHERE age IN (20, 30, 40) 
ORDER BY name;

SELECT name, email
FROM users u  
WHERE age BETWEEN 32 AND 40
ORDER BY name;

SELECT name, email
FROM contacts c  
WHERE name LIKE '_y%'
ORDER BY name;

SELECT name, email
FROM users u  
WHERE age NOT BETWEEN 32 AND 40
ORDER BY name;

SELECT COUNT(user_id) as total, user_id 
FROM contacts c
GROUP BY user_id;

--find all contacts with users which are younger than 32 y.o.--
SELECT *
FROM contacts c 
WHERE user_id IN(
	SELECT  id 
	FROM users u 
	WHERE age < 35
)

SELECT *
FROM contacts c 
JOIN users u WHERE u.id = c.user_id;

SELECT c.name contact_name, c.email contact_email, c.phone contact_phone, u.name, u.email 
FROM contacts c 
JOIN users u WHERE u.id = c.user_id;

SELECT c.name contact_name, c.email contact_email, c.phone contact_phone, u.name, u.email 
FROM contacts c 
LEFT JOIN users u WHERE u.id = c.user_id;

UPDATE contacts SET user_id = 3 WHERE id = 5;

CREATE INDEX idx_name ON contacts (name)












