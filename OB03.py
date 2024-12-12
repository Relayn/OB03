class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):
        return "Животное издает звук"

    def eat(self):
        return f"{self.name} ест"

# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)  # Вызываем конструктор базового класса
        self.wingspan = wingspan     # Добавляем специфический атрибут

    def make_sound(self):
        return "Чирик!"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Добавляем специфический атрибут

    def make_sound(self):
        return "Ррр!"

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color  # Добавляем специфический атрибут

    def make_sound(self):
        return "Шшш!"

# Полиморфизм
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")

# Класс Zoo с композицией
class Zoo:
    def __init__(self):
        self.animals = []  # Список животных
        self.employees = []  # Список сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} добавлен в сотрудники зоопарка")

    def list_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.__class__.__name__})")

    def list_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee.name} ({employee.__class__.__name__})")

# Классы для сотрудников
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Зоолог")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

# Пример использования:
# Создаем животных
bird = Bird("Попугай", 2, 0.5)
mammal = Mammal("Лев", 5, "Желтый")
reptile = Reptile("Крокодил", 10, "Зеленый")

# Создаем сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Мария")

# Создаем зоопарк
zoo = Zoo()

# Добавляем животных и сотрудников в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_employee(keeper)
zoo.add_employee(vet)

# Выводим список животных и сотрудников
zoo.list_animals()
zoo.list_employees()

# Полиморфизм: вызываем метод make_sound() для всех животных
animal_sound([bird, mammal, reptile])

# Специфические действия сотрудников
keeper.feed_animal(bird)
vet.heal_animal(reptile)