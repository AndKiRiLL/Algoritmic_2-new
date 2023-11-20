# Объявляем класс Rectangle
class Rectangle:

    # Инициализируем переменные
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    # Метод для вычисления Площади
    def get_square(self):
        return f'Площадь прямоугольника: {self.lenght * self.width}'

    # Метод для вычисления Периметра
    def get_perimeter(self):
        return f'Периметр прямоугольника: {(self.lenght*2)+(self.width*2)}'

# Задаём класс Rectangle в переменную r
r = Rectangle(2, 4)

# Получаем площадь
print(r.get_square())
# Получаем периметр
print(r.get_perimeter())