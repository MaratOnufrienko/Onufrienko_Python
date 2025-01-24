import random

lst = []

number = input("Введите количество элементов списка:")
while type(number) != int:
    try:
        N = int
    except:
        N = input("Введите количество элементов списка именно в виде числа!!!:")

for i in range(N):
    lst.append(random.randint(1, 100))
