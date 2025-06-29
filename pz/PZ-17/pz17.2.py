#Задание: Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной сумму этих значений, 
# а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных A и B
import tkinter as tk
from tkinter import messagebox

def process():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        if a != b:
            a, b = a + b, a + b
        else:
            a = b = 0
        result_label.config(text=f"Новые значения: A = {a}, B = {b}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа!")

# Окно
root = tk.Tk()
root.title("Обработка переменных A и B")
root.geometry("350x220")
root.resizable(False, False)

# Метки и поля ввода
tk.Label(root, text="Введите значение A:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Введите значение B:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

# Кнопка
tk.Button(root, text="Выполнить", command=process).pack(pady=10)

# Результат
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
