def reorder_last_element(arr):
    """
    Сделать список упорядоченным, переместив последний элемент на нужную позицию.
    :param arr: Список, в котором все элементы, кроме последнего, уже упорядочены.
    :return: Упорядоченный список.
    """
    try:
        if not isinstance(arr, list):
            raise TypeError("Аргумент должен быть списком.")
        
        if not all(isinstance(x, (int, float)) for x in arr):
            raise ValueError("Список должен содержать только числа (int или float).")

        if len(arr) < 2:
            return arr  # Если в списке 1 или меньше элементов, ничего менять не нужно

        last = arr.pop()  # Удаляем последний элемент
        for i, num in enumerate(arr):
            if num > last:
                arr.insert(i, last)  # Вставляем элемент на правильное место
                break
        else:
            arr.append(last)  # Если последний элемент больше всех, добавляем его в конец

        return arr
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def main():
    try:
        # Пример корректного списка
        lst = [1, 2, 3, 5, 4]
        result = reorder_last_element(lst)
        if result is not None:
            print(f"Упорядоченный список: {result}")

        # Пример некорректного ввода
        lst_invalid = [1, 2, "a", 5, 4]  # Список с некорректным элементом
        print(f"Упорядоченный список: {reorder_last_element(lst_invalid)}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()
