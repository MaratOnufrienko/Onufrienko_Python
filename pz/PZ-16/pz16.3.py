#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют 
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. 
#Использовать модуль pickle для сериализации и десериализации объектов Python в 
#бинарном формате.


import pickle

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def is_honor(self):
        return all(grade == 5 for grade in self.grades)

    def display_info(self):
        avg_grade = self.average_grade()
        honor_status = "Отличник" if self.is_honor() else "Не отличник"
        print(f"Имя: {self.first_name}, Фамилия: {self.last_name}, Средний балл: {avg_grade:.2f}, Статус: {honor_status}")

# Функция для сохранения объектов в файл
def save_def(students, filename):
    with open(filename, 'wb') as file:
        pickle.dump(students, file)

# Функция для загрузки объектов из файла
def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Создание 3 экземпляров класса Student
st1 = Student("Игорь", "Лусенков", [5, 4, 5, 4, 5, 5, 5])
st2 = Student("Владислав", "Дуров", [5, 5, 5, 5, 5, 5, 5])
st3 = Student("Мария", "Соколова", [4, 4, 4, 5, 4, 4, 5])

# Сохраняем в файл
save_def([st1, st2, st3], 'students.pkl')

# Загружаем из файла и выводим информацию
loaded_students = load_def('students.pkl')
for student in loaded_students:
    student.display_info()