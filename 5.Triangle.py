#Объявляем класс Triangle
class Triangle:

        # Инициализируем переменные
        def __init__(self, a, b ,c):
            self.a = a
            self.b = b
            self.c = c

        # Метод получения информации
        def get_info(self):
            if self.a == self.b and self.b == self.c:
                return 'Треугольник равносторонний.'
            elif self.a == self.b and self.b != self.c:
                return 'Треугольник равнобедренный.'
            elif self.a != self.b and self.b == self.c:
                return 'Треугольник равнобедренный.'
            elif self.a == self.c and self.b != self.c:
                return 'Треугольник равнобедренный.'
            elif self.a != self.b and self.b != self.c and self.a != self.c:
                return 'Треугольник разносторонний.'

        # Метод получения площади
        def get_square(self):
            p = (self.a + self.b + self.c) / 2

            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


# Задаём класс Triangle в переменные t1, t2, t3
t1 = Triangle(1, 2, 2)
t2 = Triangle(2, 2, 2)
t3 = Triangle(1, 2, 2.75)

# Получаем тип треугольника
print(t1.get_info())
print(t2.get_info())
print(t3.get_info())
print()
# Получаем площадь треугольника
print(f'Площадь первого треугольника: {t1.get_square()}')
print(f'Площадь второго треугольника: {t2.get_square()}')
print(f'Площадь третьего треугольника: {t3.get_square()}')