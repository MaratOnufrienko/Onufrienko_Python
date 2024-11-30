#Задание: Дано вещественное число X и целое число N (> 0). Найти значение выражения X - X 3 /(3!) + X5 /(5!) - ... + (-1)N -X 2-N+1/((2-N+1)!) (N! = 12 ...N). Полученное число является приближенным значением функции sin в точке X. 

import math

#Запрашиваем у пользователя вод данных
X = float(input("Введите значение X: "))
while type(X) != float:
    try:
        X = float(X)
        if X < 0:
            print("Число должно быть больше 0")
            X = float(input("Введите значение X: "))
    except ValueError:
        X = float(input("Введите значение X: "))
N = input("Введите значение N (целое и больше 0): ")

#Обрабатываем исключения для N
while True:
    try:
        N = int(N)
        if N > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print("Неверный ввод! Пожалуйста, введите целое число больше 0.")
        N = input("Введите значение N: ")

#Вычисляем приближенное значение sin(X) через ряд Тейлора
sin_approx = 0
for k in range(N + 1):
    term = ((-1) ** k * X ** (2 * k + 1)) / math.factorial(2 * k + 1)
    sin_approx += term

print("Приближенное значение sin(X):", sin_approx)