number = 91132435444
result = 0
multiplier = 1
while number > 0:
    digit = number % 10
    squared_digit = digit * digit
    result + squared_digit * multiplier
    multiplier *= 100
    number //= 10

print(result)