def ShiftLeft3(A, B, C):
    """Выполняет левый циклический сдвиг для чисел A, B, C."""
    A, B, C = B, C, A  # Левый циклический сдвиг
    return A, B, C

# Пример использования:
A1, B1, C1 = 3.0, 2.0, 7.0  # Первый набор данных
A2, B2, C2 = 4.0, 5.0, 6.0  # Второй набор данных

A1, B1, C1 = ShiftLeft3(A1, B1, C1)
A2, B2, C2 = ShiftLeft3(A2, B2, C2)

print(f"После сдвига: A1={A1}, B1={B1}, C1={C1}")
print(f"После сдвига: A2={A2}, B2={B2}, C2={C2}")
