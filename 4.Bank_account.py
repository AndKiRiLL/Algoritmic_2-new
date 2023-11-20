#Объявляем класс BankAccount
class BankAccount:

    # Инициализируем переменные
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.balance = balance
        self.account_transactions = []

    # Метод получения информации
    def get_info(self):
        return f'Полное имя: {self.full_name}, Баланс: {self.balance} руб.'

    # Метод получения истории операций со счётом
    def get_account_transactions(self):
        list = []
        for i in range(0, len(self.account_transactions)):
            list.append(f'{i+1}. {self.account_transactions[i]}')
        return list

    # Метод Пополнения баланса
    def replenish_balance(self, quantity):
        self.account_transactions.append(f'На ваш баланс поступило {quantity} руб.')
        self.balance += quantity

    # Метод Снятия баланса
    def withdrawal_balance(self, quantity):
        self.account_transactions.append(f'С вашего баланса снято {quantity} руб.')
        self.balance -= quantity


# Задаём класс BankAccount в переменную ba
ba = BankAccount('Andriyanov Kirill', 15000)

# получаем информацию
print(ba.get_info())
print()

# пополняем счёт на 5000 руб
print(f'На ваш баланс поступило 5000 руб.')
ba.replenish_balance(5000)
print(ba.get_info())
print()

# снимаем со счёта 2500
print(f'С вашего баланса снято 2500 руб.')
ba.withdrawal_balance(2500)
print(ba.get_info())
print()

# Получаем историю операций со счётом
print('История операций со счётом:')
list_transactions = ba.get_account_transactions()

for i in range(0, len(ba.get_account_transactions())):
    print(list_transactions[i])