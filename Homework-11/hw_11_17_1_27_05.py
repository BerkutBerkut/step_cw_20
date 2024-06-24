"""
Домашнее задание №17: Лямбда-функции
Выполните следующие задания:
Задание №1
Реализовать инженерный калькулятор, для всех арифметических действий, включая 
нахождение факториала, Фибоначчи, и всех тригонометрических функций, также возведения 
числа в степени. 
В ходе решения, допустимо использования модуля math, функции определяемой 
пользователем, рекурсивной функции и лямбда-функции. 
Реализуйте диалог с пользователем. 
"""

import math

# Определение функций
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Лямбда-функции для основных арифметических операций
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else 'Infinity',
    'power': lambda x, y: x ** y
}

# Тригонометрические функции
trig_functions = {
    'sin': lambda x: math.sin(math.radians(x)),
    'cos': lambda x: math.cos(math.radians(x)),
    'tan': lambda x: math.tan(math.radians(x)),
    'asin': lambda x: math.degrees(math.asin(x)),
    'acos': lambda x: math.degrees(math.acos(x)),
    'atan': lambda x: math.degrees(math.atan(x))
}

def main():
    while True:
        print("\nИнженерный калькулятор")
        print("1. Основные арифметические операции")
        print("2. Факториал")
        print("3. Число Фибоначчи")
        print("4. Тригонометрические функции")
        print("5. Возведение в степень")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            operation = input("Введите операцию (add, subtract, multiply, divide): ").strip().lower()
            if operation in operations:
                result = operations[operation](x, y)
                print(f"Результат: {result}")
            else:
                print("Неверная операция")

        elif choice == '2':
            n = int(input("Введите число для вычисления факториала: "))
            result = factorial(n)
            print(f"Факториал {n} равен {result}")

        elif choice == '3':
            n = int(input("Введите номер числа Фибоначчи: "))
            result = fibonacci(n)
            print(f"{n}-е число Фибоначчи равно {result}")

        elif choice == '4':
            x = float(input("Введите угол (в градусах) или значение для арксинуса/арккосинуса/арктангенса: "))
            function = input("Введите тригонометрическую функцию (sin, cos, tan, asin, acos, atan): ").strip().lower()
            if function in trig_functions:
                result = trig_functions[function](x)
                print(f"Результат: {result}")
            else:
                print("Неверная функция")

        elif choice == '5':
            x = float(input("Введите число: "))
            y = float(input("Введите степень: "))
            result = math.pow(x, y)
            print(f"{x} в степени {y} равно {result}")

        elif choice == '6':
            print("Выход из программы")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
