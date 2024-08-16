class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    def moneyX(self):
        amount = float(input("Введите сумму для добавления денег на счет: "))
        self._balance += amount
        print(f"На счет добавлено {amount}. Текущий баланс: {self._balance}")

    def _kill(self):
        confirmation = input("Вы хотите обнулить баланс? (да/нет): ")
        if confirmation.lower() == "да":
            self._balance = 0
            print("Баланс обнулен.")
        else:
            print("")

    def __jackpot(self):
        self._balance *= 10
        print(f"ваш выйгрыш умножен! Ваш новый баланс: {self._balance}")

    def _unite_balance(self, other_account):
        self._balance += other_account._balance
        other_account._balance = 0
        print(f"Баланс объединен был объединён . Текущий баланс: {self._balance}")

# Пример использования
acc1 = Bank("tema", 100)
account2 = Bank("danya", 100)

acc1.moneyX()
acc1._kill()
acc1._Bank__jackpot()


acc1._unite_balance(account2)
