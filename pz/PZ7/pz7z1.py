def determine_number_type(s):
    """Определяет, является ли строка целым числом, вещественным числом или не числом."""
    try:
        if '.' in s:
            float(s)
            return 2
        else:
            int(s)
            return 1
    except ValueError:
        return 0
# Пример использования
examples = ["623", "4.67", "abob", "12.0.1"]
for ex in examples:
    print(f"'{ex}' -> {determine_number_type(ex)}")
