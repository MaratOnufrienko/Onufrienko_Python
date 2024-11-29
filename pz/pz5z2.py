def ShiftLeft3(A, B, C):
    """
    Выполняет левый циклический сдвиг для чисел A, B, C.
    Проверяет, что все входные параметры являются числами.
    """
    try:
        if not all(isinstance(x, (int, float)) for x in [A, B, C]):
            raise TypeError("Все параметры должны быть числами (int или float).")
        A, B, C = B, C, A  # Левый циклический сдвиг
    except Exception as e:
        print(f"Произошла ошибка при выполнении сдвига: {e}")
        return None, None, None  # Возвращаем "пустые" значения при ошибке
    return A, B, C

def main():
    try:
        # Первый набор данных
        A1, B1, C1 = 5.0, 7.0, 1.0
        # Второй набор данных
        A2, B2, C2 = 1.0, 9.0, 7.0

        A1, B1, C1 = ShiftLeft3(A1, B1, C1)
        if None in (A1, B1, C1):
            print("Ошибка при обработке первого набора данных.")

        A2, B2, C2 = ShiftLeft3(A2, B2, C2)
        if None in (A2, B2, C2):
            print("Ошибка при обработке второго набора данных.")

        print(f"После сдвига: A1={A1}, B1={B1}, C1={C1}")
        print(f"После сдвига: A2={A2}, B2={B2}, C2={C2}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()
