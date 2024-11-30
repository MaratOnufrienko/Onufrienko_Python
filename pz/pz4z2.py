#Задание: Дано целое число N (> 0). Найти сумму 1N + 2N-1 + ... + N1 .

# Ввод данных
N = input("Введите значение N (целое и больше 0): ")

# Обработка исключений для N
while type(N) != int or N <= 0:
    try:
        N = int(N)
        if N <= 0:
            raise ValueError
    except ValueError:
        print("Неверный ввод! Пожалуйста, введите целое число больше 0.")
        N = input("Введите значение N: ")

# Вычисление суммы 1^N + 2^(N-1) + ... + N^1
sum_result = sum(i ** (N - i + 1) for i in range(1, N + 1))

print("Сумма 1^N + 2^(N-1) + ... + N^1 равна:", sum_result)