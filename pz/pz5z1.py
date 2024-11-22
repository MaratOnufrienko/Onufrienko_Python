def sum_of_digits(n):
    """Возвращает сумму цифр числа n"""
    return sum(int(digit) for digit in str(abs(n)))

def process_number(n):
    """Вычитает сумму цифр из числа до тех пор, пока результат не станет равным нулю.
       Возвращает количество операций.
    """
    steps = 0
    while n != 0:
        n -= sum_of_digits(n)
        steps += 1
    return steps

# Пример использования:
number = 19  # Заданное число
steps = process_number(number)
print(f"Количество операций до нуля для числа {number}: {steps}")
