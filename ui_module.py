import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
from sqlite_module import SQliteDB

class ExpenseApp:
    def __init__(self):
        self.db = SQliteDB()
        self.db.create_db()

    def run(self):
        # Запуск главного окна приложения
        def update_table():
            for row in tree.get_children():
                tree.delete(row)
            records = self.db.fetch_all_records()
            for record in records:
                tree.insert("", tk.END, values=record[1:])

        def open_add_window():
            def save_new_record():
                try:
                    amount = float(entry_amount.get())
                    category = entry_category.get()
                    description = entry_desc.get()
                    self.db.insert_value(amount, category, description)
                    messagebox.showinfo("Success", "Record added!")
                    add_window.destroy()
                    update_table()
                except ValueError:
                    messagebox.showerror("Error", "Amount must be a number!")

            add_window = tk.Toplevel(root)
            add_window.title("Add record")

            ttk.Label(add_window, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
            entry_amount = ttk.Entry(add_window)
            entry_amount.grid(row=0, column=1, padx=5, pady=5)

            ttk.Label(add_window, text="Category:").grid(row=1, column=0, padx=5, pady=5)
            entry_category = ttk.Entry(add_window)
            entry_category.grid(row=1, column=1, padx=5, pady=5)

            ttk.Label(add_window, text="Description:").grid(row=2, column=0, padx=5, pady=5)
            entry_desc = ttk.Entry(add_window)
            entry_desc.grid(row=2, column=1, padx=5, pady=5)

            ttk.Button(add_window, text="Save", command=save_new_record).grid(row=3, column=0, columnspan=2, pady=10)

        def delete_selected_record():
            selected_item = tree.selection()
            if selected_item:
                record = tree.item(selected_item)["values"]
                self.db.delete_value(record[0], record[1], record[2])  # Передаем данные для удаления
                messagebox.showinfo("Success", "Record deleted!")
                update_table()
            else:
                messagebox.showerror("Error", "Select record for deleting!")

        # Создание главного окна
        root = ThemedTk(theme="adapta")  # Примеры тем: 'breeze', 'equilux', 'adapta', 'arc'
        root.title("Expense")

        # Таблица для отображения записей
        columns = ("Amount", "Category", "Description")
        tree = ttk.Treeview(root, columns=columns, show="headings")
        tree.heading("Amount", text="Amount, $")
        tree.heading("Category", text="Category")
        tree.heading("Description", text="Description")
        tree.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Кнопки
        btn_add = ttk.Button(root, text="Добавить", command=open_add_window)
        btn_add.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        btn_delete = ttk.Button(root, text="Удалить", command=delete_selected_record)
        btn_delete.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Заполнение таблицы при запуске
        update_table()

        root.mainloop()
