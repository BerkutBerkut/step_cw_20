import random

def list_rand_num(N):
    # Создаем случайный список из N в диапазоне от 1 до 100
    numbers = list(random.randint(1, 100) for _ in range (N))
    # Выводим на печать элементы списка
    print(numbers)

    # Определяем в списке нечетные и четные чисела
    od_num = list(number for number in numbers if number % 2 != 0)
    ev_num = list(number for number in numbers if number % 2 == 0)
    
    # Подсчитываем количество нечетных и четных чисел
    od_count = len(od_num)
    ev_count = len(ev_num)
    
    # Выводим четные и нечетные числа
    print("Output")
    print(od_num)
    print(ev_num)
        
    # Сравниваем количество четных и нечетных чисел и выводим результат
    if od_count > ev_count:
        return "Нет"
    else:
        return "Да"

if __name__ == "__main__":
    print("Input")
    N = int(input(" "))
    result = list_rand_num(N)
    print(result)
  