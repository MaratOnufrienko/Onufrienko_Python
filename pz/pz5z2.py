#Задание: Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг: значение A переходит в C, значение C — в B, значение B — в A (A, B, C — вещественные параметры, являющиеся одновременно входными и выходными). С помощью этой функции выполнить левый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def ShiftLeft3(A, B, C):
    """
    Выполняет левый циклический сдвиг для чисел A, B, C.
    Проверяет, что все входные параметры являются числами.
    """
    try:
        for x in [A, B, C]:
            if type(x) not in [int, float]:
                print("Все параметры должны быть числами (int или float).")
                return None, None, None
        A, B, C = B, C, A  # Левый циклический сдвиг
    except Exception as e:
        print(f"Произошла ошибка при выполнении сдвига: {e}")
        return None, None, None  # Возвращаем "пустые" значения при ошибке
    return A, B, C

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
    print(f"Неожиданная ошибка!!!!: {e}")