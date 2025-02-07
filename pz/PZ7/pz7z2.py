#Дана строка, состоящая из русских слов, набранных заглавными буквами и 
#разделенных пробелами (одним или несколькими). Преобразовать каждое слово в 
#строке, заменив в нем все предыдущие вхождения его последней буквы на символ 
#«.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ». 
#Количество пробелов между словами не изменять
def transform_words(s):
    words = s.split()
    transformed_words = []
    for word in words:
        last_char = word[-1]
        new_word = ""
        for c in word[:-1]:
            if c == last_char:
                new_word += "."
            else:
                new_word += c
        new_word += last_char
        transformed_words.append(new_word)
    return transformed_words
sentence = "МИНИМУМ АВАТА"
ws = transform_words(sentence)
for word in ws:
    print(word)