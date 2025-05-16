def read_books(books):
    if len(books) == 0:
        return('Вы не прочитали ни одной книги')
    if len(books) == 1:
        return f'Вы прочитали 1 книгу: {books[0]}'
    if len(books) == 2:
        return(f'Вы прочитали 2 книги: {books[0]} и {books[1]}')
    if len(books) > 2:
        ost = len(books) - 2
        return(f'Вы прочитали {books[0]}, {books[1]} и еще {ost} книги')



print(read_books(['Преступление и наказание', 'Колобок', 'Мартин Иден', 'Букварь']))