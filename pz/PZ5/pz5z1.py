#Задание: Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?

def sum_of_digits(n):
    """Возвращает сумму цифр числа n"""
    return sum(int(digit) for digit in str(abs(n)))
def process_number(n):
    """
    Вычитает сумму цифр из числа до тех пор, пока результат не станет равным нулю.
    Возвращает количество операций.
    """
    steps = 0
    try:
        while n != 0:
            n -= sum_of_digits(n)
            steps += 1
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None  # Возвращаем None, если произошла ошибка
    return steps

# Запрашиваем число у пользователя
number = input("Введите целое число: ")
while type(number) != int:
    try:
        number = int(number)
        if number < 0:
            print("Число должно быть больше 0")
            number = input("Введите целое число: ")
    except ValueError:
        number = input("Введите целое число: ")
        
steps = process_number(number)
if steps:
    print(f"Количество операций до нуля для числа {number}: {steps}")
