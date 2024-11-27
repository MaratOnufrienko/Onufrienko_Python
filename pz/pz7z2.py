def transform_words(s):
    """
    Преобразует каждое слово строки, заменяя все предыдущие вхождения последней буквы на '.'.
    :param s: Входная строка из русских слов, разделенных пробелами.
    :return: Преобразованная строка.
    """
    words = s.split()
    transformed_words = []
    for word in words:
        last_char = word[-1]
        new_word = ''.join('.' if c == last_char else c for c in word[:-1]) + last_char
        transformed_words.append(new_word)
    return ' '.join(transformed_words)

# Пример использования
sentence = "МИНИМУМ"
print(transform_words(sentence))