"""
Домашнее задание №16: Функции
Задание №2.
Напишите функцию, которая проверяет является ли число степенью двойки. Если 
истинно выведите True, иначе False. 
"""

def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n - 1)) == 0

# Примеры использования функции
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 8, 16, 18, 32, 64, 100]
    for number in test_numbers:
        print(f"{number} is power of two: {is_power_of_two(number)}")
