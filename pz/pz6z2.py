def count_unique_elements(arr):
    """
    Найти количество различных элементов в списке.
    :param arr: Список элементов.
    :return: Количество уникальных элементов.
    """
    return len(set(arr))

# Пример использования
lst = [2, 2, 2, 3, 4, 4, 5]
print(f"Количество уникальных элементов: {count_unique_elements(lst)}")
