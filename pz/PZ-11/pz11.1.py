# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы до n-1 умножены на элемент n:

import random
l = [" ".join([str(int(random.randint(-100, 100))) for i in range(10)])]
f3 = open('data.txt', 'w')
f3.writelines(l)
f3.close()

# Дублируем список в новый файл
f4 = open('data2.txt', 'w', encoding="utf-8")
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()
# разбиваем строку и ее значения преобразуем в числа
f3 = open('data.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

f3 = open('data.txt')

if len(k) >= 1:
    multiplied = [x * k[-1] for x in k[:-1]]
else:
    multiplied = []

f4 = open('data2.txt', 'a', encoding="utf-8")
f4.write('\n')
print(f'Количество элементов: {len(k)}', f'Сумма элементов: {sum(k)}', f"Элементы до n-1 умножены на элемент n: {multiplied}", sep="\n", file=f4)
f4.close()