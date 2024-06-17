from functools import reduce 

call_numbers = input("Введите числа через пробел: ")
list_numbers = list(map(int, call_numbers.split()))
print(list_numbers)

sum_numbers = lambda lst : sum(lst)
print(sum_numbers(list_numbers))

mult_numbers = reduce((lambda x, y: x*y), list_numbers)
print(mult_numbers)





