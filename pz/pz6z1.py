def sum_between_k_l(arr, k, l):
    """
    Найти сумму элементов списка с номерами от K до L включительно.
    :param arr: Список элементов.
    :param k: Начальный индекс (1 < K < L < len(arr)).
    :param l: Конечный индекс.
    :return: Сумма элементов от K до L.
    """
    if not (1 < k < l <= len(arr)):
        raise ValueError("K и L должны удовлетворять условиям: 1 < K < L <= N.")
    
    return sum(arr[k-1:l])  # Учитываем, что индексы в Python начинаются с 0

# Пример использования
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k, l = 2, 9
print(f"Сумма элементов от {k} до {l}: {sum_between_k_l(lst, k, l)}")
