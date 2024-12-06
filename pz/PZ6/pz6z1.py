#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов списка с номерами от K до L включительно.
import random

def sum_between_k_l(arr, k, l):
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
        return sum(arr[k:l+1])  # Индексы в Python начинаются с 0
    except Exception as e:
        print(f"Произошла ошибка при вычислении суммы: {e}")
        return None

lst = []   

number = input("Введите кол-во элементов списка: ")
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

k = input("Введите k: ")
while type(k) != int:
    try:
        k = int(k)
        if k < 0:
            print("Число должно быть больше 0")
            k = input("Введите k: ")
    except ValueError:
        k = input("Введите k: ")
    
l = input("Введите l: ")
while type(l) != int:
    try:
        l = int(l)
        if l < 0:
            print("Число должно быть больше 0")
            l = input("Введите l: ")
    except ValueError:
        l = input("Введите l: ")
        
        result = sum_between_k_l(lst, k, l)
        if result is not None:
            print(f"Сумма элементов от {k} до {l}: {result}")
        else:
            print("Не удалось вычислить сумму из-за ошибки.")
print(lst)
print(sum_between_k_l(lst, k, l))