#Дан целочисленный список размера N. Найти количество различных элементов в данном списке.
def count_unique_elements(arr: list):
    els = 0
    elWas = []
    for el in arr:
        if not el in elWas:
            els += 1
            elWas.append(el)
    return els

# набор данных
lst = [2, 2, 3, 4, 5, 6, 6, 7]  
result = count_unique_elements(lst)
if result is not None:
    print(f"Количество уникальных элементов: {result}")