# Создание базового класса "Животное" и его наследование для создания классов 
# "Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать" 
# и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства, 
# такие как "гавкать" и "мурлыкать".

# Базовый класс
class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} дышит.")

    def eat(self):
        print(f"{self.name} питается.")

# Класс-наследник: Собака
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} гавкает: Гав-гав!")

    def fetch(self):
        print(f"{self.name} приносит палку.")

# Класс-наследник: Кошка
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def purr(self):
        print(f"{self.name} мурлычет: Мрррр...")

    def climb(self):
        print(f"{self.name} взбирается на дерево.")

# Пример использования
dog = Dog("Барсик", "Овчарка")
cat = Cat("Мурка", "Черная")

dog.breathe()
dog.eat()
dog.bark()
dog.fetch()

print()

cat.breathe()
cat.eat()
cat.purr()
cat.climb()