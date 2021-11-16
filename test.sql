1)
UPDATE Users
SET reg_date = SUBSTR(reg_date, 7, 4) || '-' || SUBSTR(reg_date, 4, 2) || '-' ||SUBSTR(reg_date, 1, 2);
2)
SELECT login FROM Users WHERE id = (SELECT Count(id) FROM Users);
3)
SELECT DISTINCT(SUBSTR(birth_date, 1, 4)) AS 'Уникальные года рождения' FROM Users;
4)
SELECT Count(id) AS 'total_items' FROM Items;
5)
SELECT AVG(substr(DATE('now'), 1, 4) - substr(birth_date, 1, 4)) AS 'Average age' FROM Users;
