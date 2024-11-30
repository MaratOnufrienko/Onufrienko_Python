#Задание: Дано целое число N (> 0). Найти сумму 1N + 2N-1 + ... + N1 .

# Ввод данных
N = input("Введите значение N (целое и больше 0): ")

def summ(l):
    summa = 0
    for element in l:
        summa += element
    return summa

# Обработка исключений для N
while type(N) != int:
    try:
        N = int(N)
        if N < 0:
            print("Число должно быть больше 0")
            N = input("Введите значение N (целое и больше 0): ")
    except ValueError:
        N = input("Введите значение N (целое и больше 0): ")

# Вычисление суммы 1^N + 2^(N-1) + ... + N^1
sum_result = summ(i ** (N - i + 1) for i in range(1, N + 1))

print("Сумма 1^N + 2^(N-1) + ... + N^1 равна:", sum_result)