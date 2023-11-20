# Объявляем класс Student
class Student:

    # Инициализируем переменные
    def __init__(self, name='', age=0, average_point=0):
        self.name = name
        self.age = age
        self.average_point = average_point

    # Получить полную информацию про студента
    def get_info(self):
        return f'Имя студента: {self.name}, Возраст студента {self.age}, Средний балл студента: {self.average_point}'

    # Установить полную, новую информацию про студента
    def set_info(self, new_name, new_age, new_average_point):
        self.name = new_name
        self.age = new_age
        self.average_point = new_average_point

    # Получить Имя студента
    def get_name(self):
        return f'Имя студента: {self.name}.'

    # Получить Возраст студента
    def get_age(self):
        return f'Возраст студента {self.age} лет.'

    # Получить Средний балл студента
    def get_average_point(self):
        return f'Средний бал студента: {self.average_point}.'

    # Установить Имя для Студента
    def set_name(self, new_name):
        self.name = new_name

    # Установить Возраст для Студента
    def set_age(self, new_age):
        self.age = new_age

    # Установить Средний балл для Студента
    def set_average_point(self, new_average_point):
        self.average_point = new_average_point

# Задаём класс Student в переменную "s"
s = Student('Kirill', 17, 3.7)

# Методы Получения информации
print('# Одиночные методы получения информации:')
print(s.get_name())
print(s.get_age())
print(s.get_average_point())

print()

# Методы установки новых значений
print('# Установка новых значений')
s.set_name('Timur')
s.set_age(24)
s.set_average_point(4.2)
print(s.get_info())


# Метод изменения всех значений
s.set_info('Andrey', 16, 4.1)

print()

# Метод получения всех значений
print('# Метод получения всей информации:')
print(s.get_info())


