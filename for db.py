import sqlite3

def NormDate(date):
    if date.count('.') != 0:
        return date[6:] + '-' + date[3:5] + '-' + date[:2]
    else:
        return date

def Inituser(log, psswd, reg, birth, name, lastname):
    cursor.execute(f'''
        INSERT INTO Users(login, password, reg_date, birth_date, name, lastname)
        VALUES ('{log}', '{psswd}', '{NormDate(reg)}', '{NormDate(birth)}', '{name}', '{lastname}');''')
    conn.commit()

conn = sqlite3.connect('sitedb.db')
cursor = conn.cursor()
# login, psswd, reg, birth, name, lastname = input().split()
# Inituser(login, psswd, reg, birth, name, lastname) инициализация нового пользователя
cursor.execute('''
    SELECT (SELECT login FROM Users WHERE user_id = Users.id) AS 'Логин',
    (SELECT name FROM Items WHERE item_id = Items.id) AS 'Название товара'
    FROM Carts WHERE Carts.item_id = 1;''')
print(cursor.fetchall())
cursor.execute('''
    SELECT (SELECT login FROM Users WHERE Users.id = user_id) AS 'Логин',
    (SELECT substr(DATE('now'), 1, 4) - substr(birth_date, 1, 4) FROM Users WHERE Users.id = user_id) AS 'Возраст',
    (SELECT name FROM Items WHERE Items.id = item_id) AS 'Название товара',
    Carts.num
    FROM Carts;''')
print(cursor.fetchall())
cursor.execute('''
    SELECT (SELECT name FROM Users WHERE id = user_id) AS 'Имя',
    (SELECT login FROM Users WHERE id = user_id) AS 'Логин',
    (SELECT substr(DATE('now'), 1, 4) - substr(reg_date, 1, 4) FROM Users WHERE id = user_id) AS 'Сколько с нами',
    discount AS 'Скидон'
    FROM Carts WHERE (SELECT substr(DATE('now'), 1, 4) - substr(reg_date, 1, 4) FROM Users WHERE id = user_id) > 7 GROUP BY user_id;''')
print(cursor.fetchall())
# cursor.execute("SELECT login FROM Users")
# print(cursor.fetchall())
conn.close()