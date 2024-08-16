class сalculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return сalculator(self.value + other.value)

    def __sub__(self, other):
        return сalculator(self.value - other.value)

    def __mul__(self, other):
        return сalculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Деление на ноль нельзя")
        return сalculator(self.value / other.value)

    def __str__(self):
        return str(self.value)

num1 = сalculator(3)
num2 = сalculator(2)


response_add = num1 + num2
print("Сложение:", response_add)


response_sub = num1 - num2
print("Вычитание:", response_sub)


response_mul = num1 * num2
print("Умножение:",response_mul)


response_div = num1 / num2
print("Деление:", response_div)
