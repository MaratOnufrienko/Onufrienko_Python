# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря.

avto = {
    "Lada": ["Vesta", "Kalina", "Nyancat"],
    "Wolkswagen": ["Tiguan", "Yaneznayubolshe", "Marka3"],
    "Hundai": ["Solaris", "Goyda", "Abayunda"],
}
for marka in avto:
    print(avto.get(marka)[1])