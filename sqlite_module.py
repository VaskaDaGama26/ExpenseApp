import sqlite3

class SQliteDB:

    def create_db(self):
        conn = sqlite3.connect('expenses.db')
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
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO expenses (amount, category, desc) VALUES (:amount, :category, :desc)""",
                        {'amount': amount,'category': category,'desc': desc}
                       )
        conn.commit()
        conn.close()

    def delete_value(self, amount, category, desc):
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE amount = :amount AND category = :category AND desc = :desc",
                       {'amount': amount, 'category': category, 'desc': desc})
        conn.commit()
        conn.close()

    def fetch_category(self, category):
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE category=category")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.commit()
        conn.close()

    def fetch_all_records(self):
        conn = sqlite3.connect('expenses.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        conn.close()
        return rows


