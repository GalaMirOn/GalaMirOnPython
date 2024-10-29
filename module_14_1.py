import sqlite3

connection = sqlite3.connect("not_telegram1.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1,11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)", (f"User{i}", f"exampl{i}@gmail.com", i*10, 1000))
connection.commit()
cursor.execute("CREATE INDEX IF NOT EXISTS idx_balance ON Users (balance)")
cursor.execute("UPDATE Users SET balance=? WHERE id % 2 =?", (500, 1))
connection.commit()
cursor.execute("DELETE FROM Users WHERE id % 3 =?", (1, ))
connection.commit()
cursor.execute("CREATE INDEX IF NOT EXISTS idx_age ON Users (age)")
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age!= ?", (60, ))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection.close()