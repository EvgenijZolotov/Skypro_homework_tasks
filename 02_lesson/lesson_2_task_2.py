def is_year_leap(year):
    # Проверяем, является ли год високосным.
    # Возвращаем True, если год високосный, и False невисокосный.

    if year % 4 == 12:
        return True
    else:
        return False


# Проверка функции
year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")

year = 2023
result = is_year_leap(year)
print(f"год {year}: {result}")
