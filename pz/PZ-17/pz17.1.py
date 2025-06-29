import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Регистрация")
root.geometry("650x580")
root.configure(bg="white")
root.resizable(False, False)

# Заголовок
tk.Label(root, text="Создание нового сайта", bg="#00AEEF", fg="white",
         font=("Arial", 16, "bold"), pady=10).pack(fill="x")

form = tk.Frame(root, bg="white", padx=30, pady=15)
form.pack(fill="both", expand=True)

# Универсальная функция создания строки ввода
def create_input(label_text, row):
    tk.Label(form, text=label_text, bg="white", anchor="w",
             font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(form, width=40)
    entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")
    return entry

# Поля ввода
email_entry = create_input("Email", 0)
password_entry = create_input("Пароль", 1)
password_entry.config(show="*")
name_entry = create_input("Имя", 2)
surname_entry = create_input("Фамилия", 3)
nick_entry = create_input("Никнейм", 4)

# Дата рождения
tk.Label(form, text="Дата рождения", bg="white",
         font=("Arial", 10)).grid(row=5, column=0, sticky="w", pady=5)

dob_frame = tk.Frame(form, bg="white")
dob_frame.grid(row=5, column=1, sticky="w")

days = ttk.Combobox(dob_frame, values=[str(i) for i in range(1, 32)], width=3)
months = ttk.Combobox(dob_frame, values=[str(i) for i in range(1, 13)], width=3)
years = ttk.Combobox(dob_frame, values=[str(i) for i in range(1950, 2026)], width=5)
days.grid(row=0, column=0, padx=2)
months.grid(row=0, column=1, padx=2)
years.grid(row=0, column=2, padx=2)

# Пол
tk.Label(form, text="Пол", bg="white",
         font=("Arial", 10)).grid(row=6, column=0, sticky="w", pady=5)

gender_var = tk.StringVar(value="Мужчина")
gender_frame = tk.Frame(form, bg="white")
gender_frame.grid(row=6, column=1, sticky="w")
tk.Radiobutton(gender_frame, text="Мужчина", variable=gender_var, value="Мужчина", bg="white").pack(side="left", padx=5)
tk.Radiobutton(gender_frame, text="Женщина", variable=gender_var, value="Женщина", bg="white").pack(side="left", padx=5)

# Место проживания
tk.Label(form, text="Место проживания", bg="white",
         font=("Arial", 10)).grid(row=7, column=0, sticky="w", pady=5)

city_combo = ttk.Combobox(form, values=["Другой город...", "Москва", "Казань", "Минск"])
city_combo.grid(row=7, column=1, sticky="w", pady=5)

# Чекбокс
check_var = tk.IntVar()
tk.Checkbutton(form,
               text="Подтверждаю условия использования UID сообщества",
               variable=check_var, bg="white").grid(row=8, column=1, sticky="w", pady=10)

# Кнопка регистрации
tk.Button(root, text="Регистрация", bg="#007BCE", fg="white", font=("Arial", 12, "bold"),
          padx=20, pady=5).pack(pady=10)

root.mainloop()
