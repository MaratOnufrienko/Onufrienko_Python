spisok = ['Кирилл', 'Артем', 'Ольга', 'Дима', 'Алла']

def gosti(listt):
    if len(listt) == 0:
        res = 'Никто не пришел на вечеринку'
    elif len(listt) == 1:
        res = f'На вечеринке {listt[0]}'
    elif len(listt) == 2:
        res = f'{listt[0]} и {listt[1]} на вечеринке'
    elif len(listt) >= 3:
        res = f'{listt[0]}, {listt[1]} и {len(listt) - 2} других людей на вечеринке'
    return res

print(gosti(spisok))