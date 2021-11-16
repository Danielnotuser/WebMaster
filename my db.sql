1)
-- Вывести логины тех людей, которые купили Тигровых акул)
SELECT
	(SELECT login FROM Users WHERE user_id = Users.id) AS 'Логин',
	(SELECT name FROM Items WHERE item_id = Items.id) AS 'Название товара'
	FROM Carts WHERE Carts.item_id = 1;
2)
-- Вывести полный список логинов, возраст пользователя, кол-во товара
SELECT 
	(SELECT login FROM Users WHERE Users.id = user_id) AS 'Логин',
	(SELECT substr(DATE('now'), 1, 4) - substr(birth_date, 1, 4) FROM Users WHERE Users.id = user_id) AS 'Возраст',
	(SELECT name FROM Items WHERE Items.id = item_id) AS 'Название товара',
	Carts.num
	FROM Carts;
3)
-- Люди, их скидки в корзине и как долго они зарегистрированы на сайте
SELECT
	(SELECT name FROM Users WHERE id = user_id) AS 'Имя',
	(SELECT login FROM Users WHERE id = user_id) AS 'Логин',
	(SELECT substr(DATE('now'), 1, 4) - substr(reg_date, 1, 4) FROM Users WHERE id = user_id) AS 'Сколько с нами',
	discount AS 'Скидон'
	FROM Carts WHERE (SELECT substr(DATE('now'), 1, 4) - substr(reg_date, 1, 4) FROM Users WHERE id = user_id) > 7 GROUP BY user_id;
	
