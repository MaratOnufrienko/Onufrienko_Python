def sum_between_k_l(arr, k, l):
    """
    Найти сумму элементов списка с номерами от K до L включительно.
    :param arr: Список элементов.
    :param k: Начальный индекс (1 < K < L <= len(arr)).
    :param l: Конечный индекс.
    :return: Сумма элементов от K до L.
    """
    try:
        # Проверка на корректность аргументов
        if not isinstance(arr, list):
            print("Ошибка: Первый аргумент должен быть списком.")
            return None
        
        if not all(isinstance(x, (int, float)) for x in arr):
            print("Ошибка: Список должен содержать только числа.")
            return None
        
        if not (1 < k < l <= len(arr)):
            print("Ошибка: K и L должны удовлетворять условиям: 1 < K < L <= len(arr).")
            return None

        # Вычисление суммы
        return sum(arr[k-1:l])  # Индексы в Python начинаются с 0
    except Exception as e:
        print(f"Произошла ошибка при вычислении суммы: {e}")
        return None


def main():
    try:
        # Пример данных
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k, l = 5, 9  # Заданные индексы

        result = sum_between_k_l(lst, k, l)
        if result is not None:
            print(f"Сумма элементов от {k} до {l}: {result}")
        else:
            print("Не удалось вычислить сумму из-за ошибки.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()
