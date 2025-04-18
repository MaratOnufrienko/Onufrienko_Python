# Составить генератор (yield), который преобразует все буквенные символы в заглавные.

def to_upper(text): yield from (char.upper() if char.isalpha() else char for char in text)
print("".join(to_upper(input("Введите строку: "))))