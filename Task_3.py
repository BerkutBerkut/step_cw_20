if __name__ == "__main__":
    # Определяем кортеж с фруктами
    fruits = ("apple", "banana", "orange", "apple", "mango", "banana", "apple")

    fruit_name = input("Введите название фрукта: ")

    # Подсчет количества вхождений фрукта в кортеж
    count = fruits.count(fruit_name)

    print(f"Фрукт '{fruit_name}' встречается {count} раз(а) в кортеже.")
