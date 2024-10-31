import sqlite3


def initiate_db():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    opis = [" ", "Витамин D-3 10000", "Витамин C 1000", "Цинка пиколинат", "Комплекс EVE", "Комплекс ADAM", "Хром"]
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    photo TEXT
    )
    ''')
    for i in range(1, 7):
        cursor.execute("INSERT INTO Products(title, description, price, photo) VALUES(?,?,?,?)",
                       (f"Продукт {i}", f"Описание: {opis[i]}", i * 100, f"photo_{str(i)}.jpg"))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    for prod in products:
        print(prod[1], prod[2], prod[3], prod[4])
    connection.close()
    return products


if __name__ == '__main__':
    # initiate_db()
    get_all_products()
