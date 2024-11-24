import sqlite3
import os

class SQliteDB:
    def __init__(self):
        # Получаем путь к базе данных в %APPDATA%
        self.db_path = os.path.join(os.getenv('APPDATA'), 'ExpenseApp', 'expenses.db')

        # Убедитесь, что папка существует
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        # Если база данных отсутствует, создаем её
        if not os.path.exists(self.db_path):
            self.create_db()

    def create_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                desc TEXT
            )""")
        conn.commit()
        conn.close()

    def insert_value(self, amount,category,desc):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO expenses (amount, category, desc) VALUES (:amount, :category, :desc)""",
                        {'amount': amount,'category': category,'desc': desc}
                       )
        conn.commit()
        conn.close()

    def delete_value(self, amount, category, desc):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE amount = :amount AND category = :category AND desc = :desc",
                       {'amount': amount, 'category': category, 'desc': desc})
        conn.commit()
        conn.close()

    def fetch_category(self, category):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE category=category")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.commit()
        conn.close()

    def fetch_all_records(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        conn.close()
        return rows


