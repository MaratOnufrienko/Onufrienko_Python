def reorder_last_element(arr):
    """
    Сделать список упорядоченным, переместив последний элемент на нужную позицию.
    :param arr: Список, в котором все элементы, кроме последнего, уже упорядочены.
    :return: Упорядоченный список.
    """
    try:
        # Проверка типа аргумента
        if not isinstance(arr, list):
            print("Ошибка: Аргумент должен быть списком.")
            return None
        
        # Проверка содержимого списка
        if not all(isinstance(x, (int, float)) for x in arr):
            print("Ошибка: Список должен содержать только числа (int или float).")
            return None

        # Если в списке 1 или меньше элементов, возвращаем его как есть
        if len(arr) < 2:
            return arr

        # Удаляем последний элемент
        last = arr.pop()

        # Вставляем последний элемент на нужное место
        for i, num in enumerate(arr):
            if num > last:
                arr.insert(i, last)
                break
        else:
            # Если последний элемент больше всех, добавляем его в конец
            arr.append(last)

        return arr
    except Exception as e:
        print(f"Произошла ошибка при упорядочивании: {e}")
        return None


def main():
    try:
        # Пример корректного списка
        lst = [1, 2, 3, 5, 4]
        result = reorder_last_element(lst)
        if result is not None:
            print(f"Упорядоченный список: {result}")

        # Пример некорректного ввода
        lst_invalid = [1, 2, "f", 5, 4]  # Список с некорректным элементом
        result_invalid = reorder_last_element(lst_invalid)
        if result_invalid is not None:
            print(f"Упорядоченный список: {result_invalid}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()
