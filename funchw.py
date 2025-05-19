# Функция суммирования
def sum_(a, b):
    print(a + b)

sum_(10, 20)

# Функция умножения
def multiply(a, b):
    print(a * b)

multiply(10, 20)

# Функция деления
def divide(a, b):
    print(a / b)

divide(10, 20)

# Функция с возвратом значений (возвращает цену кефира по названию)
def get_kefir(name):
    products = {
        "Веселый молочник": 100,
        "Белая река": 120,
        "Жети Ата": 140
    }
    print(products)
    return products[name]

kefir_price = get_kefir("Веселый молочник")
kefir_price += get_kefir("Белая река")
kefir_price += get_kefir("Жети Ата")
print("Общая цена кефира:", kefir_price)

# Функция с параметром по умолчанию
def temperature_report(city, temperature=20):
    print(f"The temperature in {city} is {temperature} degrees")

temperature_report("Paris")
temperature_report("London", 10)

# Рекурсивная функция
def recursive_function(n):
    print(n)
    if n == 0:
        return
    recursive_function(n - 1)

recursive_function(5)

# Использование map и lambda
print(
    list(
        map(
            lambda x: x * 2, [1, 2, 3, 4, 5]
        )
    )
)

# Функция для вывода строки заданное число раз
def print_message(message, times):
    for _ in range(times):
        print(message)

print_message("Hello, world!", 3)

# Функция для проверки чётности числа
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# Функция с переменным количеством аргументов (сумма чисел)
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))

# Функция с переменным количеством аргументов (нахождение максимума)
def find_max(*args):
    return max(args)

print(find_max(1, 2, 3, 4_
