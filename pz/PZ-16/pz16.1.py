# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент
# отличником.

class Student:
    def __init__(self, first_name, last_name, grades):
        # Инициализация атрибутов
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

st1 = Student("Марат", "Онуфриенко", [5, 4, 5, 3, 5, 5, 5])
st2 = Student("Владимир", "Возняк", [6, 6, 6])
st1.display_info()
st2.display_info()