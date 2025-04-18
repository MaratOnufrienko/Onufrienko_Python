# В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.

def f(lst):
    l = len(lst)//3 # если вдруг количество элементов не кратно 3 берется целое число
    return sum(lst[:l])/l

import random
test_list = [random.randint(-100, 100) for i in range(10)]
print(test_list, f(test_list))
