lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# Фильтруем числа по условиям
result = [num for num in lst if num < 30 and not num % 3]

print("Числа меньше 30, кратные 3:", *result)
