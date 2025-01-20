import sqlite3
import tkinter as tk
from tkinter import messagebox

# Функция для добавления данных в базу данных
def add_data():
    title = entry_title.get()
    artist_id = entry_artist_id.get()
    if title and artist_id:
        cursor.execute("INSERT INTO Album (Title, ArtistId) VALUES (?, ?)", (title, artist_id))
        conn.commit()
        messagebox.showinfo("Успех", "Данные добавлены!")
        entry_title.delete(0, tk.END)
        entry_artist_id.delete(0, tk.END)
        update_data_list()
    else:
        messagebox.showwarning("Ошибка", "Введите данные для добавления.")

# Функция для удаления данных из базы данных
def delete_data():
    selected_item = listbox.curselection()
    if selected_item:
        data = listbox.get(selected_item)
        cursor.execute("DELETE FROM Album WHERE Title = ?", (data,))
        conn.commit()
        messagebox.showinfo("Успех", "Данные удалены!")
        update_data_list()
    else:
        messagebox.showwarning("Ошибка", "Выберите данные для удаления.")

# Функция для обновления списка данных
def update_data_list():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT Title FROM Album")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row[0])

# Создание соединения с базой данных
conn = sqlite3.connect('World_Music.sqlite')
cursor = conn.cursor()

# Создание основного окна
root = tk.Tk()
root.title("Управление данными")

# Список для отображения данных
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Кнопка для добавления данных
add_button = tk.Button(root, text="Добавить данные", command=add_data)
add_button.pack(pady=5)

# Поле для ввода названия
entry_title = tk.Entry(root)
entry_title.pack(pady=5)

# Поле для ввода ArtistId
entry_artist_id = tk.Entry(root)
entry_artist_id.pack(pady=5)

# Кнопка для удаления данных
delete_button = tk.Button(root, text="Удалить данные", command=delete_data)
delete_button.pack(pady=5)



# Обновление списка данных при запуске
update_data_list()

# Запуск основного цикла
root.mainloop()

# Закрытие соединения с базой данных при выходе
conn.close()