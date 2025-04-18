# В матрице найти среднее арифметическое элементов последних двух столбцов

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

values = list(map(int, sum(list(zip(*matrix))[-2:], ())))
print("Среднее арифметическое последних двух столбцов:", sum(values)/len(values))

# или

rows = len(matrix)
cols = len(matrix[0])

total = 0
count = 0

for row in matrix:
    total += row[-1] + row[-2]  # последние два столбца
    count += 2

average = total / count
print("Среднее арифметическое последних двух столбцов:", average)