def count_unique_elements(arr):
    """
    Найти количество различных элементов в списке.
    :param arr: Список элементов.
    :return: Количество уникальных элементов.
    """
    try:
        if not isinstance(arr, list):
            raise TypeError("Аргумент должен быть списком.")
        
        # Проверка на допустимые типы элементов в списке
        if not all(isinstance(x, (int, float, str, tuple, frozenset)) for x in arr):
            raise ValueError("Список должен содержать только неизменяемые элементы (int, float, str, tuple, frozenset).")
        
        return len(set(arr))
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def main():
    try:
        # Пример данных
        lst = [2, 2, 2, 3, 4, 4, 5]  # Корректный список
        result = count_unique_elements(lst)
        if result is not None:
            print(f"Количество уникальных элементов: {result}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()
