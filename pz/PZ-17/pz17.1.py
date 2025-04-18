import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Регистрация")
root.geometry("600x700")
root.configure(bg="#f5f5f5")

frame = tk.Frame(root, padx=10, pady=10, bg="white", relief="groove", borderwidth=2)
frame.pack(pady=20)

tk.Label(frame, text="Создание нового сайта", font=("Arial", 16, "bold"), fg="white", bg="#00aaff", pady=10).grid(row=0, column=0, columnspan=2, sticky="we")

fields = [
    ("Email", tk.Entry),
    ("Пароль", lambda master: tk.Entry(master, show="*")),
    ("Имя", tk.Entry),
    ("Фамилия", tk.Entry),
    ("Никнейм", tk.Entry),
]

entries = {}
for i, (label, widget_type) in enumerate(fields, start=1):
    tk.Label(frame, text=label, anchor="w", bg="white", fg="#0077cc").grid(row=i, column=0, sticky="w", pady=5)
    entry = widget_type(frame)
    entry.grid(row=i, column=1, sticky="we", pady=5)
    entries[label] = entry

tk.Label(frame, text="Дата рождения", anchor="w", bg="white", fg="#0077cc").grid(row=6, column=0, sticky="w", pady=5)
dob_frame = tk.Frame(frame, bg="white")
dob_frame.grid(row=6, column=1, sticky="w")

day = ttk.Combobox(dob_frame, width=4, values=[str(i) for i in range(1, 32)])
month = ttk.Combobox(dob_frame, width=8, values=[
    "Янв", "Фев", "Мар", "Апр", "Май", "Июн",
    "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"
])
year = ttk.Combobox(dob_frame, width=6, values=[str(i) for i in range(1950, 2025)])

day.grid(row=0, column=0)
month.grid(row=0, column=1, padx=5)
year.grid(row=0, column=2)

tk.Label(frame, text="Пол", anchor="w", bg="white", fg="#0077cc").grid(row=7, column=0, sticky="w", pady=5)
gender = tk.StringVar()
tk.Radiobutton(frame, text="Мужчина", variable=gender, value="Мужчина", bg="white").grid(row=7, column=1, sticky="w")
tk.Radiobutton(frame, text="Женщина", variable=gender, value="Женщина", bg="white").grid(row=7, column=1)

tk.Label(frame, text="Место проживания", anchor="w", bg="white", fg="#0077cc").grid(row=8, column=0, sticky="w", pady=5)
location = ttk.Combobox(frame, values=["Москва", "Санкт-Петербург", "Другой город..."])
location.grid(row=8, column=1, sticky="we")

tk.Label(frame, text="Код безопасности", anchor="w", bg="white", fg="#0077cc").grid(row=9, column=0, sticky="w", pady=5)
security_code = tk.Entry(frame)
security_code.grid(row=9, column=1, sticky="we")

accept = tk.IntVar()
tk.Checkbutton(frame, text="Подтверждаю условия использования", variable=accept, bg="white").grid(row=10, column=0, columnspan=2, pady=10)

tk.Button(frame, text="Регистрация", bg="#0077cc", fg="white", font=("Arial", 10, "bold")).grid(row=11, column=0, columnspan=2, pady=10)

for i in range(2):
    frame.columnconfigure(i, weight=1)

root.mainloop()
