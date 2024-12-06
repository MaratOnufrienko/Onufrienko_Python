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

        # lst = []
        # for x in arr:
        #     lst.append(isinstance(x, (int, float)))
        # return lst
        # all(lst); lst = [True, True, True, True] -> True

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
        import random
        lst = []
        number = input("Введите целое число: ")
        while type(number) != int:
            try:
                number = int(number)
                if number < 0:
                    print("Число должно быть больше 0")
                    number = input("Введите целое число: ")
            except ValueError:
                number = input("Введите целое число: ")
        for i in range(number):
            lst.append(random.randint(1, 100))
        result = reorder_last_element(sorted(lst))
        if result is not None:
            print(f"Упорядоченный список: {result}")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


# Запуск программы
if __name__ == "__main__":
    main()
