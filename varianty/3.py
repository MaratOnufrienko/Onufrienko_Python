def w(word):
    listt = []
    words = word.split('')
    for word in words:
        if len(word) >= 5:
            listt.append(word[::-1])
        else:
            listt.append(word)
    return ' '.join(listt)

a = input()
print(w(a))