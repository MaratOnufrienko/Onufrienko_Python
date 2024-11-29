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
            print(n)
            steps += 1
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None  # Возвращаем None, если произошла ошибка
    return steps

def main():
    try:
        # Запрашиваем число у пользователя
        number = int(input("Введите целое число: "))
        if number < 0:
            raise ValueError("Число должно быть неотрицательным.")
        steps = process_number(number)
        if steps is not None:
            print(f"Количество операций до нуля для числа {number}: {steps}")
    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()
