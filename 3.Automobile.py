# Объявляем класс Automobile
class Automobile:

    # Инициализируем переменные
    def __init__(self, brand='', model='', year_of_issue=0, mileage=0):
        self.brand = brand
        self.model = model
        self.year_of_issue = year_of_issue
        self.mileage = mileage

    # Метод получения информации о машине
    def get_info(self):
        return f'Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year_of_issue}, Пробег: {self.mileage}'

    # Метод изменения информации о машине
    def set_info(self, new_brand, new_model, new_year_of_issue, new_mileage):
        self.brand = new_brand
        self.model = new_model
        self.year_of_issue = new_year_of_issue
        self.mileage = new_mileage

# Задаём класс Automobile в переменную a
print('# Получаем значения')
a = Automobile('Mercedes-Benz', 'E-Class', 2021, 3000)

# получаем информацию
print(a.get_info())
print()

# изменяем информацию
print('# Устанавливаем новые значения')
a.set_info('Audi', 'A-Class', 2022, 1000)
print()

# получаем информацию
print('# Получаем значения')
print(a.get_info())