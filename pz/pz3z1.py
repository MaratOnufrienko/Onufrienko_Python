#Задание:Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара совпадающих».

#Запрашиваем у пользователя ввод данных
a = input("Введите первое число: ")
while type(a) != int:
    try: 
        a = int(a)
    except ValueError: 
        a = input("Введите первое число")
b = int(input("Введите второе число: "))
while type(b) != int:
    try: 
        b = int(b)
    except ValueError: 
        b = input("Введите второе число")
c = int(input("Введите третье число: "))
while type(c) != int:
    try:
        c = int(c)
    except ValueError: 
        c = input("Введите третье число")
#Проверяем числа на совпадения
if a == b or a == c or b == c:
    print("Существует хотя бы одна пара совпадающих чисел.")
else:
    print("Все числа различны.")